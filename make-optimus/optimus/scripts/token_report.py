"""token_report.py - how many tokens did a session (or a time window) really use? (Optimus: measure, don't guess)

Usage:
  python token_report.py                       newest session of this project folder
  python token_report.py <session.jsonl>       a given transcript
  python token_report.py --all                 every session in the project folder, one line each
  python token_report.py --since "2026-11-26 20:30" [--until "..."]   only turns in that local-time window
Reads Claude Code's local transcripts (~/.claude/projects/<project>/*.jsonl): every assistant turn carries message.usage
(input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens). Schema is observed, not documented.
"""
import sys, os, json, glob, datetime as dt

PROJ = os.path.expanduser(r'~/.claude/projects/c--Users-cross-Downloads-xc')

def parse_time(s):
    return dt.datetime.strptime(s, '%Y-%m-%d %H:%M')

def scan(path, since=None, until=None):
    tot = dict(turns=0, input=0, output=0, cache_write=0, cache_read=0, images=0)
    seen = set()
    for line in open(path, encoding='utf-8', errors='ignore'):
        try: e = json.loads(line)
        except Exception: continue
        ts = e.get('timestamp')
        if ts and (since or until):
            t = dt.datetime.fromisoformat(ts.replace('Z', '+00:00')).astimezone().replace(tzinfo=None)
            if (since and t < since) or (until and t > until): continue
        m = e.get('message') or {}
        if isinstance(m.get('content'), list):
            tot['images'] += sum(1 for c in m['content'] if isinstance(c, dict) and (c.get('type') == 'image' or
                                 (c.get('type') == 'tool_result' and any(isinstance(x, dict) and x.get('type') == 'image' for x in (c.get('content') or []) if isinstance(c.get('content'), list)))))
        u = m.get('usage') if e.get('type') == 'assistant' else None
        if not u: continue
        mid = m.get('id')
        if mid in seen: continue          # one API response can be split over several transcript lines
        seen.add(mid); tot['turns'] += 1
        tot['input'] += u.get('input_tokens', 0); tot['output'] += u.get('output_tokens', 0)
        tot['cache_write'] += u.get('cache_creation_input_tokens', 0); tot['cache_read'] += u.get('cache_read_input_tokens', 0)
    tot['fresh'] = tot['input'] + tot['cache_write'] + tot['output']      # what really costs: new input + cache writes + output
    return tot

def fmt(name, t):
    k = lambda x: f'{x / 1000:,.0f}k'
    return (f"{name}: {t['turns']} turns | output {k(t['output'])} | new input {k(t['input'] + t['cache_write'])} "
            f"| cache read {k(t['cache_read'])} | images {t['images']} | fresh total {k(t['fresh'])} "
            f"| per turn {t['fresh'] // max(1, t['turns']):,}")

if __name__ == '__main__':
    a = sys.argv[1:]
    since = parse_time(a[a.index('--since') + 1]) if '--since' in a else None
    until = parse_time(a[a.index('--until') + 1]) if '--until' in a else None
    files = sorted(glob.glob(os.path.join(PROJ, '*.jsonl')), key=os.path.getmtime)
    if '--all' in a:
        for f in files: print(fmt(os.path.basename(f)[:8], scan(f)))
    else:
        f = next((x for x in a if x.endswith('.jsonl')), files[-1] if files else None)
        if not f: print('no transcripts found in', PROJ); sys.exit(1)
        print(fmt(os.path.basename(f)[:8] + (f' [{a[a.index("--since") + 1]} .. ]' if since else ''), scan(f, since, until)))

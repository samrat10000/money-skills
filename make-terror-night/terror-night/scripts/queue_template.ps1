$ErrorActionPreference = 'Continue'
$ff = 'C:\Users\cross\AppData\Local\Microsoft\WinGet\Packages\yt-dlp.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-N-121938-g2456a39581-win64-gpl\bin\ffmpeg.exe'
$out = 'C:\Users\cross\Downloads\xc\ep1pc\out\v8'
New-Item -ItemType Directory -Force $out | Out-Null
# cut = name|frames ('' = the cut's own range)
$cuts = [ordered]@{
 '525'='125_brute_jturn|'; '530'='130_overpass_park|'; '535'='135_dash_reveal|'; '540'='140_crash_zoom|'; '550'='150_scream|';
 '552'='152_watcher_bridge|'; '565'='165_rec_end|'; '400'='000_hook|'; '404'='004w_watcher|'; '406'='006_screamer_still|';
 '441'='040_stairwell_ext|313,444'; '450'='050_lobby|'; '455'='055_b1_stairs|'; '471'='070_in_the_car|'; '490'='090_gate_burst|';
 '495'='095_watcher_street|'; '160'='160_empty_seat|' }
$expect = @{ '525'=144; '530'=72; '535'=60; '540'=48; '550'=60; '552'=36; '565'=36; '400'=168; '404'=60; '406'=96;
 '441'=132; '450'=120; '455'=70; '471'=84; '490'=84; '495'=60; '160'=252 }
Set-Location C:\Users\cross\Downloads\xc\ep1pc\ep1
foreach ($c in $cuts.Keys) {
  $nm, $fr = $cuts[$c].Split('|')
  $mp4 = "$out\$($nm)_v8_silent.mp4"
  if (Test-Path $mp4) { "SKIP $c (done)"; continue }
  while (tasklist | findstr /i blender.exe) { Start-Sleep 20 }
  $env:CUT=$c; $env:RES='1'; $env:SAMP='32'; $env:PERSIST='0'; $env:VSTEP='10'; $env:DEVICE='GPU'; $env:MB='.2'; $env:STEP='1'; $env:OUTROOT=$out
  # 2026-11-26: render in 25-frame chunks, one fresh Blender per chunk (VRAM creep took c400 from 19 s to 8 min/frame overnight)
  if ($fr) { $f0, $f1 = $fr.Split(',') | ForEach-Object { [int]$_ } } else { $f0 = 1; $f1 = $expect[$c] }
  $t = Get-Date
  for ($a = $f0; $a -le $f1; $a += 25) {
    $b = [Math]::Min($a + 24, $f1)
    $have = @(($a..$b) | Where-Object { $p_ = "$out\c$c\f{0:D4}.png" -f $_; (Test-Path $p_) -and ((Get-Item $p_).Length -gt 0) }).Count
    if ($have -eq ($b - $a + 1)) { continue }
    Get-ChildItem "$out\c$c\*.png" -ErrorAction SilentlyContinue | Where-Object Length -eq 0 | Remove-Item
    while (tasklist | findstr /i blender.exe) { Start-Sleep 10 }
    $env:FR = "$a,$b"
    & C:\Users\cross\Downloads\xc\blender501\blender.exe -b --python shots2.py *>> "$out\r$c.log"
  }
  $sec = ((Get-Date) - $t).TotalSeconds
  $pngs = @(Get-ChildItem "$out\c$c\*.png" -ErrorAction SilentlyContinue | Sort-Object Name)
  $n = $pngs.Count
  $err = (Select-String -Path "$out\r$c.log" -Pattern 'Traceback' | Select-Object -First 1).Line
  "CUT $c frames=$n secs=$([int]$sec) spf=$(if($n){[math]::Round($sec/$n,1)}else{'-'}) err=$err"
  if ($n -eq 0) { "FAILED $c"; Get-Content "$out\r$c.log" -Tail 30; continue }
  $want = $expect[$c]
  if ($want -and $n -lt $want) { "PARTIAL $c $n/$want (no mp4; re-run queue to resume)"; continue }
  $start = [int]($pngs[0].BaseName.Substring(1))
  & $ff -y -loglevel error -framerate 24 -start_number $start -i "$out\c$c\f%04d.png" -vf scale=1080:1920 -c:v libx264 -crf 14 -pix_fmt yuv420p -an $mp4
  "MP4 $c $(Test-Path $mp4)"
}
"QUEUE DONE"

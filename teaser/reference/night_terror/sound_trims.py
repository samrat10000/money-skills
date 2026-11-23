# earshot `find` best moments (2026-11-23), seconds into each recording
TR.update(ping_4=(0, 1.5), ping_0=(39.25, 41.22), rain_7=(5, 40), rainroof_4=(72.5, 77.5), siren_8=(10, 25),
          rev_4=(.749, 3.745), rev2_9=(26.495, 28.475), rev2_9b=(2.5, 7.5), splash_0=(1.113, 2.796), rev2_0=(2.677, 5.354),
          bear_6=(0, 2.593), breath_2=(8.949, 12.528), breath_2b=(12.528, 16.108), growl_1=(3.3, 5.75),
          passby_1=(5.013, 10.026), glass_2=(2.355, 4.015), thunder_5=(1.9, 12), thunder_2=(3.366, 7.855),
          boom_2=(.031, 4.0), debris2_2=(1.867, 3.864), whoosh_0=(.193, 2.193), hit_5=(.78, 3.0), roar_5=(0, 2.5),
          heart_2=(0, 3.606), subdrop_4=(1.36, 4.11), elk_0=(0, 2.5), lion_5=(3.0, 6.5), tiger_3=(0, 2.195),
          lion_1=(4.125, 6.0), drift_1=(3.714, 7.428), drift2_0=(9.637, 12.39), drift_6=(52.5, 57.5), drift2_9=(5.49, 9.15),
          hit_6=(.102, 1.774), tapestop_1=(3.849, 4.3), static_5=(0, 2.2))
def _peak(k):
    a, b = TR[k]; x = load(k)[int(a * SR):int(b * SR)].mean(1)
    e = np.convolve(np.abs(x), np.ones(2400) / 2400, 'same'); return float(e.argmax() / SR)
TR['whoosh_peak'] = _peak('whoosh_0'); TR['passby_peak'] = _peak('passby_1'); TR['subdrop_lead'] = _peak('subdrop_4')
print('peaks', TR['whoosh_peak'], TR['passby_peak'], TR['subdrop_lead'])

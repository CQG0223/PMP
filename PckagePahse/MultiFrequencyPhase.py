import numpy as np

def MutiFrequencyPhase(pha1,T1,pha2,T2):
    if T1 < T2:
        pha1,pha2 = pha2,pha1
        T1,T2 = T2,T1
    T12 = (T1 * T2)/(T1 - T2)
    assert T12 > 0,"error"

    mask1 = pha1 > pha2
    mask2 = ~mask1
    delta11 = mask1 * (pha1 - pha2)
    deltal2 = mask2 *(2*np.pi -(pha2 - pha1))

    delta = delta11 + deltal2
    m = np.round((delta*T2/(T2 - T1) - pha1) / (2*np.pi))
    pha12 = pha1 + m*2*np.pi
    return pha12,T12

def StdPhase(idealPhase,actualPhase = None):
    e = 0.2
    pha_min = idealPhase.min()
    pha_max = idealPhase.max()
    idealPhase = (idealPhase - pha_min) / (pha_max - pha_min + e) * 2 * np.pi
    if actualPhase is not None:
        actualPhase = (actualPhase - pha_min) / (pha_max - pha_min + e) * 2 * np.pi
        return idealPhase,actualPhase
    else:
        return idealPhase
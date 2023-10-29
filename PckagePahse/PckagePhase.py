#Wrapped phase unwrapping
import numpy as np
class PckagePhase(object):
    def __init__(self,N,B_min):
        self.N = N
        self.Bmin = B_min
    
    def calPhase(self,MitrixList):
        assert len(MitrixList) == self.N,"The number of imgaes cause a error!"
        sin_sum = 0
        cos_sum = 0

        for index,img in enumerate(MitrixList):
            pk = 2*index*np.pi/self.N
            sin_sum = sin_sum + img * np.sin(pk)
            cos_sum = cos_sum + img * np.cos(pk)
        
        phase = -np.arctan2(sin_sum,cos_sum)
        B = np.sqrt(sin_sum * sin_sum + cos_sum*cos_sum)*2/self.N
        B_mask = B > self.Bmin
        phase = phase * B_mask
        B = B_mask
        return phase,B

    
        
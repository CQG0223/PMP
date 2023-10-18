import numpy as np

PARAKEYS = ['A','B','W','H','T','N']

def check_dict_keys_values(dictionary, expected_keys):
    if len(dictionary.keys()) != len(expected_keys):
        return False
    for key, _ in dictionary.items():
        if key not in expected_keys:
            return False
    return True

class makePattern(object):
    def __init__(self,para):
        self.para = para

    def getPatten(self,show=False):
        img = []
        dictionary = self.para
        if check_dict_keys_values(dictionary,PARAKEYS):
            img = self._createPatten(dictionary['A'],dictionary['B'],dictionary['W'],
                                    dictionary['H'],dictionary['T'],dictionary['N'])
            if show:
                show(img[0],dictionary['H'],dictionary['W'])
        else:
            raise KeyError("Keyerror!")
        return img

    def _createPatten(self,A,B,W,H,T,N):
        img = []
        f_2pi = 1/np.double(T) * 2 * np.pi
        xs = np.linspace(0,W-1,W)
        for k in range(N):
            Is = A + B*np.cos(f_2pi*xs + (2*k/N)*np.pi)
            Is_img = np.tile(Is,(H,1))
            img.append(Is_img)
        return img
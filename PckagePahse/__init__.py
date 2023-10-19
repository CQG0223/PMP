import matplotlib.pyplot as plt
import numpy as np
from .makePatterns import makePattern
from .MultiFrequencyPhase import MutiFrequencyPhase,StdPhase
from .PckagePhase import PckagePhase

def SingleImgshow(h=None,img=None):
    assert img != None and h != None,"img error!!"
    for hh in h:
        plt.figure()
        for image in img:
            H,W = image.shape
            if hh > H:
                hh = H/2
            xs = np.reshape(np.linspace(0,W-1,W),(W,1))
            value = np.transpose(image[hh,:])
            plt.plot(xs,value)
            plt.title('Title')
            plt.xlabel('X Label'), plt.ylabel('Y Label')
    for image in img:
        plt.figure()
        plt.imshow(image,cmap='gray')
        plt.title('Title')
    plt.show()
    
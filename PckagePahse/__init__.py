import matplotlib.pyplot as plt
import numpy as np
from .makePatterns import makePattern
from .MultiFrequencyPhase import MutiFrequencyPhase,StdPhase
from .PckagePhase import PckagePhase

def SingleImgshow(h,img=None):
    assert img != None,"img error!!"
    for image in img:
        H,W = image.shape
        if h > H:
            h = H / 2
        plt.figure()
        xs = np.reshape(np.linspace(0,W-1,W),(W,1))
        value = np.transpose(image[h,:])
        plt.plot(xs,value)
        plt.title('Title')
        plt.xlabel('X Label'), plt.ylabel('Y Label')
        plt.figure()
        plt.imshow(image,cmap='gray')
        plt.title('Title')
    plt.show()
    
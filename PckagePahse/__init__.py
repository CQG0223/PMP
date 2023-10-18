import matplotlib.pyplot as plt
import numpy as np
from .makePatterns import makePattern
from .MultiFrequencyPhase import MutiFrequencyPhase,StdPhase
from .PckagePhase import PckagePhase

def show(img,H,W):
    plt.figure()
    xs = np.reshape(np.linspace(0,W-1,W),(W,1))
    h = 900
    value = np.transpose(img[h,:])
    plt.plot(xs,value)
    plt.title('Title')
    plt.xlabel('X Label'), plt.ylabel('Y Label')
    plt.figure()
    plt.imshow(img,cmap='gray')
    plt.title('Title')
    plt.show()
    
from DataLoader import getDataLoader
from PckagePahse import *

if __name__ == "__main__":
    para1 = {'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':28}
    para2 = {'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':26}
    para3 = {'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':24}
    path = r'./data'
    actualImgLoader = getDataLoader(path)
    NumImg = len(actualImgLoader)
    N = 4
    img = []
    imgList = []
    for left,lpath,right,rpath in actualImgLoader:
        img.append(left)
        if N == 1:
            N = 4
            imgList.append(img)
            img = []
            continue
        N = N -1
    
    print(len(imgList))
    actualImg1,actualImg2,actualImg3 = imgList[0],imgList[1],imgList[2]


    img = makePattern(para1).getPatten(show=False)
    phaseIdeal1,BIdeal1 = PckagePhase(N=4,B_min=1).calPhase(img)

    img = makePattern(para2).getPatten(show=False)
    phaseIdeal2,BIdeal2 = PckagePhase(N=4,B_min=1).calPhase(img)

    img = makePattern(para3).getPatten(show=False)
    phaseIdeal3,BIdeal3 = PckagePhase(N=4,B_min=1).calPhase(img)

    phaseActual1,BActual1 = PckagePhase(N=4,B_min=1).calPhase(actualImg1)
    phaseActual2,BActual2 = PckagePhase(N=4,B_min=1).calPhase(actualImg2)
    phaseActual3,BActual3 = PckagePhase(N=4,B_min=1).calPhase(actualImg3)

    phaseActual12,T12 = MutiFrequencyPhase(phaseActual1,28,phaseActual2,26)
    phaseActual23,T23 = MutiFrequencyPhase(phaseActual2,26,phaseActual3,24)

    phaseIdeal12,T12 = MutiFrequencyPhase(phaseIdeal1,28,phaseIdeal2,26)
    phaseIdeal23,T23 = MutiFrequencyPhase(phaseIdeal2,26,phaseIdeal3,24)

    phaseIdeal12,phaseActual12 = StdPhase(phaseIdeal12,phaseActual12)
    phaseIdeal23,phaseActual23 = StdPhase(phaseIdeal23,phaseActual23)

    phaseIdeal123,T123 = MutiFrequencyPhase(phaseIdeal12,T12,phaseIdeal23,T23)
    phaseActual123,T123 = MutiFrequencyPhase(phaseActual12,T12,phaseActual23,T23)

    phaseIdeal123,phaseActual123 = StdPhase(phaseIdeal123,phaseActual123)
    right_mask1 = phaseActual123 <= 2 * np.pi
    right_mask2 = phaseActual123 >= 0
    phaseActual123 = phaseActual123 * right_mask1 * right_mask2
    phaseActual123 = phaseActual123 * BActual1 * BActual2 * BActual3

    H,W = phaseActual123.shape
    show(phaseActual123,H,W)

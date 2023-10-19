from PckagePahse import *
from DataLoader import getDataLoader
import os
from PIL import Image

class TwoPhaseShiftWithThreeFreq(object):
    def __init__(self,para,datapath,savepath):
        self.datapath = datapath
        self.savepath = savepath
        assert len(para) == 3,"Wrong number of parameters(3)"
        assert os.path.exists(datapath) and os.path.exists(savepath),"wrong path!!!"
        self.paraFirstFreq,self.paraSecondFreq,self.paraThirdFreq = para[0],para[1],para[2]
        
    
    def _MaxMinProcess(self,image):
        _min = image.min()
        _max = image.max()
        image = ((image - _min)/(_max - _min))*255
        return np.uint8(image)
    
    def _saveBMP(self,root,imagedict):
        for key,Value in imagedict.items():
            im = Image.fromarray(self._MaxMinProcess(Value))
            filename = f"{key}.bmp"
            Path = os.path.join(root,filename)
            im.save(Path)
    
    def run(self,imshow=False,imsave=False):
        imgListL,imgListR = getDataLoader(self.datapath,4,3)
        actualImg1,actualImg2,actualImg3 = imgListL[0],imgListL[1],imgListL[2]


        img = makePattern(self.paraFirstFreq).getPatten(show=False)
        phaseIdeal1,_ = PckagePhase(N=4,B_min=1).calPhase(img)

        img = makePattern(self.paraSecondFreq).getPatten(show=False)
        phaseIdeal2,_ = PckagePhase(N=4,B_min=1).calPhase(img)

        img = makePattern(self.paraThirdFreq).getPatten(show=False)
        phaseIdeal3,_ = PckagePhase(N=4,B_min=1).calPhase(img)

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

        saveListIdeal = dict(phaseIdeal1 = phaseIdeal1,phaseIdeal2 = phaseIdeal2,phaseIdeal3 = phaseIdeal3,
                         phaseIdeal12 = phaseIdeal12,phaseIdeal23 = phaseIdeal23,phaseIdeal123 = phaseIdeal123)
    
        saveListActual = dict(phaseActual1 = phaseActual1,phaseActual2 = phaseActual2,phaseActual3 = phaseActual3,
                            phaseActual12 = phaseActual12,phaseActual23 = phaseActual23,phaseActual123 = phaseActual123)
        if imsave:
            self._saveBMP(self.savepath,saveListIdeal)
            self._saveBMP(self.savepath,saveListActual)
        if imshow:
            #showlist = [phaseActual1,phaseActual2,phaseActual3,phaseActual12,phaseActual23,phaseActual123]
            showlist = [phaseActual123]
            SingleImgshow(900,showlist)

if __name__ == '__main__':
    para = []
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':28})
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':26})
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':24})
    datapath = r'../data'
    savepath = r'../Resourse'
    TwoPhaseShiftWithThreeFreq(para,datapath,savepath)
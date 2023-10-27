from PckagePahse import *
from DataLoader import getDataLoader
import os
from PIL import Image
import cv2

def getPhaseK(para,FreqList,LorR,rootSeed,datapath,savepath,imshow=False,imsave=False,testSave=False):
    ideal,actual = TwoPhaseShiftWithThreeFreq(para,datapath,savepath).run(rootSeed,imshow=imshow,imsave=testSave)
    kk1 = (ideal['phaseIdeal1'][200,1] - ideal['phaseIdeal1'][200,2])/(ideal['phaseIdeal123'][200,1] - ideal['phaseIdeal123'][200,2])
    kk2 = (ideal['phaseIdeal2'][200,1] - ideal['phaseIdeal2'][200,2])/(ideal['phaseIdeal123'][200,1] - ideal['phaseIdeal123'][200,2])
    kk3 = (ideal['phaseIdeal3'][200,1] - ideal['phaseIdeal3'][200,2])/(ideal['phaseIdeal123'][200,1] - ideal['phaseIdeal123'][200,2])
    roundImgk = []
    for kk,actualimg in zip([kk1,kk2,kk3],[actual['phaseActual1'],actual['phaseActual2'],actual['phaseActual3']]):
        img = actual['phaseActual123']*kk

        ImgK = (img - actualimg)/(2*np.pi)
        kernel = np.ones((7, 7), np.uint8)
        ImgK = cv2.morphologyEx(ImgK, cv2.MORPH_OPEN, kernel)
        _roundImgk = np.round(ImgK)
        #Tested by CQG 20231019
        #SingleImgshow([800,1000],[ImgK,_roundImgk])
        roundImgk.append([_roundImgk,actualimg])
    if imsave:
        saveReslt(roundImgk,FreqList,rootSeed,savepath,LorR)
    return roundImgk

def saveReslt(dataList,FreqencyList,rootNum,savepath,LorR):
        assert len(dataList) == len(FreqencyList),"error result"
        assert os.path.exists(savepath),"path error"
        for index,data in enumerate(dataList):
            assert len(data) == 2,"error result data"
            filenameWarred = "{}_{}".format(rootNum,FreqencyList[index]) + LorR + ".bmp"
            filenameK = "{}_{}".format(rootNum,FreqencyList[index]) + LorR + ".bmp"
            imgK = Image.fromarray((np.uint8(data[0])))
            imgWarred = Image.fromarray(MaxMinProcess(data[1]))

            Path = os.path.join(savepath,'gtFine','train',filenameK)
            imgK.save(Path)

            Path = os.path.join(savepath,'leftImg8bit','train',filenameWarred)
            imgWarred.save(Path)
            '''
            with open(os.path.join(savepath,'ImageSets','train.txt'),"a") as f:
                 f.writelines("{}_{}\n".format(rootNum,FreqencyList[index]))
                 '''

def MaxMinProcess(image):
        _min = image.min()
        _max = image.max()
        image = ((image - _min)/(_max - _min))*255
        return np.uint8(image)


class TwoPhaseShiftWithThreeFreq(object):
    def __init__(self,para,datapath,savepath):
        self.datapath = datapath
        self.savepath = savepath
        assert len(para) == 3,"Wrong number of parameters(3)"
        assert os.path.exists(datapath) and os.path.exists(savepath),"wrong path!!!"
        self.paraFirstFreq,self.paraSecondFreq,self.paraThirdFreq = para[0],para[1],para[2]
        
    def _saveBMP(self,root,imagedict):
        for key,Value in imagedict.items():
            im = Image.fromarray(MaxMinProcess(Value))
            filename = f"{key}.bmp"
            Path = os.path.join(root,filename)
            im.save(Path)
    
    
    def run(self,rootNum,imshow=False,imsave=False):
        imgListL = getDataLoader(self.datapath,rootNum)
        #f = lambda a:map(lambda b:a[b:b+4],range(0,len(a),4))
        b = [imgListL[i:i+4] for i in range(0,len(imgListL),4)]

        actualImg1 = b[0]
        actualImg2 = b[1]
        actualImg3 = b[2]

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
        phaseActual123 = phaseActual123 * right_mask1 * right_mask2 * BActual1*BActual2*BActual3

        saveListIdeal = dict(phaseIdeal1 = phaseIdeal1,phaseIdeal2 = phaseIdeal2,phaseIdeal3 = phaseIdeal3,
                         phaseIdeal12 = phaseIdeal12,phaseIdeal23 = phaseIdeal23,phaseIdeal123 = phaseIdeal123)
    
        saveListActual = dict(phaseActual1 = phaseActual1,phaseActual2 = phaseActual2,phaseActual3 = phaseActual3,
                            phaseActual12 = phaseActual12,phaseActual23 = phaseActual23,phaseActual123 = phaseActual123)
        if imsave:
            self._saveBMP(self.savepath,saveListIdeal)
            self._saveBMP(self.savepath,saveListActual)
        if imshow:
            #showlist = [phaseActual1,phaseActual2,phaseActual3,phaseActual12,phaseActual23,phaseActual123]
            showlist = [phaseActual123,phaseActual1,phaseActual12]
            SingleImgshow([900],showlist)
        return saveListIdeal,saveListActual
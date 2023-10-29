from PhaseShiftWithMulFreq import getPhaseK
import os

if __name__ == "__main__":
    para = [{'A':130,'B':90,'N':4,'W':2448,'H':2048,'T':18}]
    para.append({'A':130,'B':90,'N':4,'W':2448,'H':2048,'T':17})
    para.append({'A':130,'B':90,'N':4,'W':2448,'H':2048,'T':16})
    #datapath = r'H:/CQGData/3L3DR_PLUS/20231027(2)Data/data'
    #savepath = r'H:/CQGData/3L3DR_PLUS/ProcessedData'
    datapath = r'H:/CQGData/3L3DR_PLUS/20231028Data'
    savepath = r'H:/CQGData/3L3DR_PLUS/ProcessedData'
    FreqList = [18,17,16]

    dataleft = os.path.join(datapath,'L')
    dataright = os.path.join(datapath,'R')
    #getPhaseK(para,FreqList,'L',1,datapath,savepath,imshow=True,imsave=False,testSave=False)
    for k,path in zip(['L','R'],[dataleft,dataright]):
        for seed in range(1,101):
            getPhaseK(para,FreqList,k,seed,path,savepath,imshow=False,imsave=True,testSave=False)
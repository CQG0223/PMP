from PhaseShiftWithMulFreq import getPhaseK
import os

if __name__ == "__main__":
    para = [{'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':28}]
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':26})
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':24})
    datapath = r'./data'
    savepath = r'./result'
    FreqList = [28,26,24]

    dataleft = os.path.join(datapath,'L')
    dataright = os.path.join(datapath,'R')
    for k,path in zip(['L','R'],[dataleft,dataright]):
        for seed in range(1):
            getPhaseK(para,FreqList,k,seed,path,savepath,imshow=False,imsave=True,testSave=False)
    
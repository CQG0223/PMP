from PhaseShiftWithMulFreq import TwoPhaseShiftWithThreeFreq

if __name__ == "__main__":
    para = []
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':28})
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':26})
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':24})
    datapath = r'./data'
    savepath = r'./Resourse'
    TwoPhaseShiftWithThreeFreq(para,datapath,savepath).run(imshow=True,imsave=False)
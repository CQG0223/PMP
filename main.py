from PhaseShiftWithMulFreq import getPhaseK


if __name__ == "__main__":
    para = [{'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':28}]
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':26})
    para.append({'A':130,'B':90,'N':4,'W':1024,'H':1024,'T':24})
    datapath = r'F:/CQG_data/SL3DR/data'
    savepath = r'./Resourse'
    FreqList = [28,26,24]
    for seed in range(1):
        getPhaseK(para,FreqList,'{:0>4d}'.format(seed),datapath,savepath,imshow=False,imsave=True,testSave=False)
    getPhaseK(para,FreqList,'{:0>4d}'.format(0),datapath,savepath,imshow=False,imsave=False,testSave=True)
    
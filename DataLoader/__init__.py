from .DataLoader import DataItern


def getDataLoader(path,N,NumFrequency,rootNum):
    DataObject = DataItern(path,rootNum)
    assert len(DataObject) == N*NumFrequency,"data error!!!Plase check your data!!!"
    actualN = N
    imgL = []
    imgR = []
    imgListL = []
    imgListR = []
    for left,lpath,right,rpath in DataObject:
            imgL.append(left)
            imgR.append(right)
            if N == 1:
                N = actualN
                imgListL.append(imgL)
                imgListR.append(imgR)
                imgL = []
                imgR = []
                continue
            N = N -1
    return imgListL
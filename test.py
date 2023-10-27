from DataLoader import DataItern
from PckagePahse import SingleImgshow
import os

def Test(path):
    DataObj = DataItern(path)
    for left,lpath in DataObj:
        boolSave = TestProcess(left,lpath)

def TestProcess(image,imgPath):
    W,H = image.shape
    minVal,maxVal = image.min(),image.max()
    print("shape:{} {},min:{} max:{}".format(W,H,minVal,maxVal))
    SingleImgshow([1000],[image])
    return True

if __name__ == '__main__':
    path = r'F:/CQG_data/SL3DR/newProcessed/gtFine'
    Test(path)
    pass
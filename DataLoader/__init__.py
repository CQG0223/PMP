from .DataLoader import DataItern


def getDataLoader(path,rootNum):
    DataObject = DataItern(path,rootNum)
    imglist  = []
    for img in DataObject:
        imglist.append(img)
    return imglist
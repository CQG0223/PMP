import os
from typing import Any
from PIL import Image
import numpy as np

IMG_EXTENSIONS = ['.jpg', '.png','.bmp']

def load_image(file):
    return Image.open(file)

def is_image(filename):
    return any(filename.endswith(ext) for ext in IMG_EXTENSIONS)

def image_path(root,basename,extension):
    return os.path.join(root,f'{basename}{extension}')

def image_path_city(root, name):
    return os.path.join(root, f'{name}')

def image_basename(filename):
    return os.path.basename(os.path.splitext(filename)[0])

class DataItern(object):
    def __init__(self,root,rootNum):
        self.image_left = root
        self.filenameleft = [os.path.join(dp,f) for dp,dn,fn in os.walk(os.path.expanduser(self.image_left))for f in fn if is_image(f) and int(f[0:f.rfind("_")]) == rootNum]
        assert len(self.filenameleft)!=0,"file done!!!"
        self.filenameleft.sort(key=self._takeSecond)
        print("DataLoader success! left:{} rootNum:{}".format(len(self.filenameleft),rootNum))
        if len(self.filenameleft) == 0:
            pass
    
    def _takeSecond(self,elem):
        return int(elem[elem.rfind("_")+1:elem.rfind(".")])
    def __getitem__(self,index):
        filenameL = self.filenameleft[index]
        with open(filenameL, 'rb') as f:
            leftImg = load_image(f).convert('L')
        leftImg = self._sync_transform(leftImg)
        return leftImg
    
    def __len__(self):
        return len(self.filenameleft)
    
    def _sync_transform(self,left):
        return np.array(left)

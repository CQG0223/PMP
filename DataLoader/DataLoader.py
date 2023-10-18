import os
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
    def __init__(self,root):
        self.image_left = os.path.join(root,'L/')
        self.image_right = os.path.join(root,'R/')

        self.filenameleft = [os.path.join(dp,f) for dp,dn,fn in os.walk(os.path.expanduser(self.image_left))for f in fn if is_image(f)]
        self.filenameleft.sort()
        self.filenameright = [os.path.join(dp,f) for dp,dn,fn in os.walk(os.path.expanduser(self.image_left))for f in fn if is_image(f)]
        self.filenameright.sort()
        assert len(self.filenameleft) == len(self.filenameright),"The number of images in the subdirectories L and R is inconsistent."
        print("DataLoader success! left:{} right:{}".format(len(self.filenameleft),len(self.filenameright)))
    
    def __getitem__(self,index):
        filenameL = self.filenameleft[index]
        filenameR = self.filenameright[index]

        with open(filenameL, 'rb') as f:
            leftImg = load_image(f).convert('L')
        
        with open(filenameR, 'rb') as f:
            rightImg = load_image(f).convert('L')
        
        leftImg,rightImg = self._sync_transform(leftImg,rightImg)

        return leftImg,filenameL,rightImg,filenameR
    def __len__(self):
        return len(self.filenameleft)
    
    def _sync_transform(self,left,right):
        return np.array(left),np.array(right)

if __name__ == '__main__':
    root = r'./data'
    jk = DataItern(root)
    
    for left,lpath,right,rpath in jk:
        print("left:{} type:{} size:{}\n".format(lpath,type(left),left.shape))
        print("right:{} type:{} size:{}\n".format(rpath,type(right),right.shape))

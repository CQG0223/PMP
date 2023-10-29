import os
import random

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

class ReadDir(object):
    def __init__(self,filepath) -> None:
        self.filepath = filepath
    
    def __is_image_file(self,filename):
        return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

    def read_data(self,name):
        all_img = []

        data_path = os.path.join(self.filepath,name)

        for dd in os.listdir(data_path):
            if self.__is_image_file(dd):
                all_img.append(dd)
        return all_img

def rename_bmp_file(old_name, new_name):
    if not old_name.endswith(".bmp"):
        print("Invalid file format. Only BMP files are supported.")
        return
    if not os.path.exists(old_name):
        print(f"File '{old_name}' doesn't exist.")
        return
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except OSError as e:
        print(f"Error while renaming file: {e}")

def DataRename(path,name):
    filepath = path
    my_dir = ReadDir(filepath)
    img = my_dir.read_data(name)
    print('image:{}'.format(len(img)))
    for i in range(len(img)):
        old_name = img[i]

        new_name = name + '_' + old_name
        new_name = os.path.join(filepath,new_name)
        old_name = os.path.join(filepath,old_name)
        print('old:{}\tnew:{}'.format(old_name,new_name))
        rename_bmp_file(old_name,new_name)
class DatasetSegmentation(object):
    def __init__(self,filepath):
        self.filepath = filepath
        self.dirData = self.DataRead(os.path.join(self.filepath,'GroundTruth'))
        subdata04,subdata06 = self.dataSplit(self.dirData,0.4,shuffle=True)
        subtest,subval = self.dataSplit(subdata04,0.5,shuffle=True)
        self.fileTxtWrite(subtest,os.path.join(self.filepath,'ImageSets','test.txt'))
        self.fileTxtWrite(subval,os.path.join(self.filepath,'ImageSets','val.txt'))
        self.fileTxtWrite(subdata06,os.path.join(self.filepath,'ImageSets','train.txt'))
    def DataRead(self,path):
        my_dir = ReadDir(path)
        DataFolder = [Folder for Folder in os.listdir(path)]
        image = []
        for Folder in DataFolder:
            image.extend(my_dir.read_data(Folder))
        return image
    
    def fileTxtWrite(self,imageList,path):
        assert os.path.exists(path),'path error: {}'.format(path)
        with open(path,'w') as f:
            for image in imageList:
                f.writelines(image)
                f.writelines('\n')
    
    def dataSplit(self,fullList,ratio,shuffle = False):
        '''
        数据集拆分: 将列表fullList按比例ratio(随机)划分为两个子列表sublist1与sublist2
        para fullList   数据列表
        para ratio      划分比例
        para shuffle    将列表中的元素打乱顺序 
        return          sublist1与sublist2
        '''
        n_total = len(fullList)
        offset = int(n_total * ratio)
        if n_total == 0 or offset < 1:
            return [],fullList
        if shuffle:
            random.shuffle(fullList)
        sublist1 = fullList[:offset]
        sublist2 = fullList[offset:]
        return sublist1,sublist2

if __name__ == '__main__':
    filepath = r'H:/CQGData/3L3DR_PLUS/ProcessedData'
    #DataRename(filepath,'C0004')
    DatasetSegmentation(filepath)

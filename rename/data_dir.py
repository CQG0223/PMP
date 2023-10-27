import os

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]

class ReadDir(object):
    def __init__(self,filepath) -> None:
        self.filepath = filepath
    
    def __is_image_file(self,filename):
        return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

    def read_data(self):
        all_left_img = []
        all_right_img = []

        train_path = [self.filepath + str('/L'),
                      self.filepath + str('/R')]
        
        for path,ddd in zip(train_path,[all_left_img,all_right_img]):
            for dd in os.listdir(path):
                if self.__is_image_file(dd):
                    ddd.append(path + '/' + dd)
        
        return all_left_img,all_right_img

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

def convert_to_4_digit_str(number):
    return str(number).zfill(4)

def DataRename(path):
    filepath = path
    my_dir = ReadDir(filepath)
    left,right = my_dir.read_data()
    print('left:{}\nright:{}'.format(len(left),len(right)))
    img = right
    for i in range(len(img)):
        old_name = img[i]
        try:
            last_underscore_index = old_name.rfind("/")
            file_extension_index = old_name.rfind(".")
            num = (old_name[last_underscore_index + 1:file_extension_index])
            num1 = int(num[0:3])
            num2 = int(num[5:8])
        except:
            raise NameError('name error!!!')
        new_name = str(num1) + '_' + str(num2) + '.bmp'
        #new_name = convert_to_4_digit_str(num%12)+ '_' + convert_to_4_digit_str(num//12) + '_R.bmp'
        new_name = filepath + '/R/' + new_name
        print('old:{}\tnew:{}'.format(old_name,new_name))
        rename_bmp_file(old_name,new_name)

if __name__ == '__main__':
    filepath = r'F:/CQG_data/SL3DR/data'
    DataRename(filepath)
   


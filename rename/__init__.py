from .data_dir import ReadDir

def get_dir(filepath):
    my_dir = ReadDir(filepath)
    return my_dir.read_data()
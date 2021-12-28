import os
from resize import Icons, Images, BaseImage


if __name__ == '__main__':

    name = input("What is the name of your file?")

    if os.path.exists(name + '.jpg'):
        obj = BaseImage(name)
        Icons.resize(obj)
        Images.resize(obj)    
    else:
        print("File does not exist!!")
import os
from PIL import Image as Img
from datetime import datetime
from random import choice
from string import ascii_lowercase, digits

class BaseImage:
    def __init__(self, img_name, img_ext, img_type, img_sizes):
        self.__img_name = img_name
        self.__img_ext = img_ext
        self.__img_parent_dir = img_type
        self.__img_sizes = img_sizes

        now = datetime.now()

        self.__year = str(now.year)
        self.__month = str(now.month)

    def create_path(self):
        path = os.path.join(self.__img_parent_dir, self.__year, self.__month)

        if not os.path.exists(path):
            os.makedirs(path)

        return path
    
    def resize(self):
        img = Img.open(self.__img_name + self.__img_ext)
        img.thumbnail(self.__img_sizes)

        img_path = f"{self.__img_name}_{BaseImage.random_str()}{self.__img_ext}"

        out_img = os.path.join(
            self.create_path(), 
            img_path,
        )

        print(out_img)
        img.save(out_img)

        print("successfully resized {}".format(out_img))

    @staticmethod
    def random_str():
        return ''.join(choice(ascii_lowercase + digits) for _ in range(6))


class Icon(BaseImage):
    img_sizes = (300, 300)
    img_type = 'icons'

    def __init__(self, img_name, img_ext):
        super().__init__(
            img_name=img_name,
            img_ext=img_ext, 
            img_type=Icon.img_type,
            img_sizes=Icon.img_sizes
        )
    

class Image(BaseImage):
    img_sizes = (600, 600)
    img_type = 'images'

    def __init__(self, img_name, img_ext):
        super().__init__(
            img_name=img_name,
            img_ext=img_ext,
            img_type=Image.img_type,
            img_sizes=Image.img_sizes
        )

from PIL import Image
from random import randint


class BaseImage:

    @classmethod
    def __init__(cls):
        with Image.open('CH-Subway.jpg') as img:
            cls.img = img.copy()
        with open('CH-Subway.jpg') as img_for_name:
            cls.img_name = img_for_name.name[:-4]


class ConvertToImage(BaseImage):
    def __init__(self, path):
        super().__init__()
        resized_name = f'{self.img_name}_{randint(100,999)}_600*600.png'
        self.img.resize((600, 600)).save(f'images/{path}/{resized_name}')


class ConvertToIcon(BaseImage):
    def __init__(self, path):
        super().__init__()
        resized_name = f'{self.img_name}_{randint(100,999)}_300*300.png'
        self.img.resize((300, 300)).save(f'icons/{path}/{resized_name}')

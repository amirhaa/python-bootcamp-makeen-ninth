from PIL import Image
import os
import string
import datetime
import random


class BaseImage:
    def __init__(self, image_name):
        self.image_name = image_name
        self.year = str(datetime.datetime.now().year)
        self.month = str(datetime.datetime.now().month)
        self.random_ch = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))


class Images(BaseImage):

    def __init__(self, image_name):
        super().__init__(image_name)

    def resize(self):
        img =Image.open(f'{self.image_name}.jpg')
        img.thumbnail((600, 600))
        
        directory = f'Images/{self.year}/{self.month}'
        file_name = self.image_name + '_' + self.random_ch + '_' + '600x600' + '.jpg'

        os.makedirs(directory)
        img.save('/'.join([directory, file_name]))


class Icons(BaseImage):

    def __init__(self, image_name):
        super().__init__(image_name)

    def resize(self):
        img =Image.open(f'{self.image_name}.jpg')
        img.thumbnail((300, 300))

        directory = f'Icons/{self.year}/{self.month}'
        file_name = self.image_name + '_' + self.random_ch + '_' + '300x300' + '.jpg'

        os.makedirs(directory)
        img.save('/'.join([directory, file_name]))
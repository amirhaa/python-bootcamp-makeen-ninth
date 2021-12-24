import os
import datetime
from os.path import exists
from Resizer import ConvertToImage, ConvertToIcon


class PathGenerator:

    @classmethod
    def generate_path(cls):
        dt = datetime.date.today()
        year = dt.year
        month = dt.month
        for directory in ['icons', 'images']:
            if not exists(f'{directory}/{year}'):
                os.mkdir(f'{directory}/{year}')
                os.mkdir(f'{directory}/{year}/{month}')

            elif exists(f'{directory}/{year}'):
                if not exists(f'{directory}/{year}/{month}'):
                    os.mkdir(f'{directory}/{year}/{month}')
        return f'{year}/{month}'


if __name__ == '__main__':
    path = PathGenerator.generate_path()
    icon_converter_test = ConvertToIcon(path=path)
    image_converter_test = ConvertToImage(path=path)

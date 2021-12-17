class MyOpener:
    def __init__(self, name, mode='r', encoding='utf-8'):
        self.file_name = name
        self.mode = mode
        self .encoding = encoding

    def __enter__(self):
        try:
            self.file = open(self.file_name, mode=self.mode, encoding=self.encoding)
            return self.file
        except FileNotFoundError:
            print('----------------------------------------------------------------------------------------')
            if input(f'There is no file called {self.file_name}. Do you Want to override?[y,n]:\n') == 'y':
                return open(self.file_name, mode='w+')
            else:
                pass

    def __exit__(self, *args):
        self.file.close()


with MyOpener('test_file.txt') as test:
    test.seek(0)
    print(test.read())

class FlashCard:
    def __init__(self, word = input('tell me a word plz: \n'), meaning = input('what does that mean?\n')):
        self.word = word
        self.meaning = meaning

    # def __str__(self):
    #     return f"'{self.word}' is: '{self.meaning}'"


fc1 = FlashCard()
print(fc1)


# class MyClass:
#     x = 0
#     y = ""
#
#     def __init__(self, anyNumber, anyString):
#         self.x = anyNumber
#         self.y = anyString
#     def __str__ (self):
#         return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'
# myObject = MyClass(12345, "Hello")
#
# print(myObject.__str__())
# print(myObject)
# print(str(myObject))
# print(myObject.__repr__())


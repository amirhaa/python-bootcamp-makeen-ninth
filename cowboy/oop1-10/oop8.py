class Rectangle:
    def __init__(self,length,width):
        self.length = int(length)
        self.width = int(width)
    def Perimeter(self) :
        perimeter = 2*(self.width + self.length)
        return perimeter
    def Area(self):
        area = (self.length * self.width)
        return area
    def display(self):
        return [self.length,self.width,self.Area(),self.Perimeter()]

rec_1 = Rectangle(50,25)

print(rec_1.display())


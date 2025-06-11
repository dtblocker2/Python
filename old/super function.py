#super function can be used to assign  line of code from parent class to children classes
class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class square(rectangle):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)
    def area(self):
        return print(self.length * self.breadth)

class cube(rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height
    def volume(self):
        return print(self.breadth * self.height * self.length)

cube_1 = cube(2,3,4)
square_1 = square(2,4)

cube_1.volume()
square_1.area()
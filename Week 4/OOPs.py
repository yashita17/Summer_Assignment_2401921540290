from abc import ABC, abstractmethod

class Test(ABC):
    @abstractmethod
    def square(self, x):
        pass

class Arithemetic(Test):
    def square(self, x):
        return x*x

class ToTestInt(Arithemetic):
    sq = Arithemetic()
    print(sq.square(4))

#2
class Outer:
    def display(self):
        print("It's outer class")
        
    class Inner:
        def display(self):
            print("It's inner class")
    
class main():
    obj1 = Outer()
    obj1.display()

    obj2 = Outer.Inner()
    obj2.display()

#3
class Point:
    def __init__(self, x =0, y=0):
        self.__x = x
        self.__y = y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def display(self):
        print("x=", self.__x)
        print("y=", self.__y)

p1 = Point()
p1.display()

p2 = Point(10, 20)
p2.display()

p2.setX(30)
p2.setY(40)
p2.display()

p2.setXY(50, 60)
p2.display()

#4
class box:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area (self):
        return ("area =" , self.length * self.breadth)


class box3d(box):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height

    def volume(self):
        return ("volume=" , self.length * self.breadth * self.height)
    
b1 = box(3,4)
print(b1.area())

b2 = box3d(3,4,5)
print(b2.volume())

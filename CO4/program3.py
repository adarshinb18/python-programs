class Rectangle:
    def __init__(self,length,width):
        self.__lenth=length
        self.__width=width
    def area(self):
        return(self.__lenth*self.__width)
    def __lt__(self, other):
        return self.area() > other.area()
    l1=int(input("enter the length of first traingle:"))
    w1 = int(input("enter the width of first traingle:"))
    rectangle1=(l1, w1)
    l2 = int(input("enter the length of second traingle:"))
    w2=int(input("enter the width of second traingle:"))
    rectangle2=(l2,w2)
    if rectangle1 < rectangle2:
        print("area of rectangle1 is smaller")
    else:
        print("area of rectangle2 is smaller")



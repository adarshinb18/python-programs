class Rectangle():
    def __init__(self,length,breadth):
        self.lenth=length
        self.breadth=breadth
    def area(self):
        return(self.lenth*self.breadth)
    def perimeter(self):
        return(2*(self.lenth+self.breadth))
r1=Rectangle(4,5)
r2=Rectangle(5,7)
a1=r1.area()
a2=r2.area()
p1=r1.perimeter()
p2=r2.perimeter()
print("Area of Rectangle 1:",a1)
print("Perimeter of Rectangle 1:",p1)
print("Area of Rectangle 2:",a2)
print("Perimeter of Rectangle 2:",p2)
if(a1>a2):
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")


class reactangle:
    def __init__(self, l, b):
        self.length = l  
        self.breadth = b 

    def area(self):
        return self.length* self.breadth

    def __lt__(self, other):
        return self.area() < other.area()

R1 = reactangle(9, 5)
R2 = reactangle(2, 8)

if R1 < R2:
    print("Rectangle 1 has a smaller area.")
else:
    print("Rectangle 2 has a smaller area.")

print("Area of rectangle 1:", R1.area())
print("Area of rectangle 2:", R2.area())


             


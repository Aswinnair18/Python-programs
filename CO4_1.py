class rectangle: 
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.length*self.breadth
     
    def perimeter(self):
        return 2*(self.length*self.breadth)
    
R1 = rectangle(5,10)
R2 = rectangle(10,15)
print("\n area of first rectangle =",R1.area())
print("\n perimeter of first rectangle =",R1.perimeter())

print("\n area of second rectangle =",R2.area())
print("\n perimeter of the second rectangle =",R2.perimeter())

if R1.area()<R2.area():
    print("\n Largest is",R2.area())
else:
    print("\n Largest is ",R1.area())

    





      
      

     

 

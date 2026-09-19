# write lambda functions to find area of square,rectangle and triangle
square=lambda a: a* a
rectangle=lambda l, b: l* b
triangle=lambda b, h: 0.5* b* h

s =float (input("square side: "))
print("area of a square :",square(s))
l =float(input("rectangle length:"))
b =float(input("rectangle breadth"))
print ("area of the rectangle:",rectangle(l,b))
b =float(input("triangle base:"))
h =float(input("trinagle height:"))
print(" area of triangle:",triangle(b,h))
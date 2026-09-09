#Generate a list 4 digit number in a given range with all their even and the  number is a perfect squre
import math

for i in range(1000, 10000):
    sqroot=int(math.sqrt(i))
    if sqroot*sqroot==i:
        if all(int(digit)%2==0 for digit in str(i)):
            print(i)



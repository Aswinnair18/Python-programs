#Find the fibonacci series of a term

num=int(input("enter a number"))
b=0
c=1
for i in range(1,num+1):
    print(b)
    d=b+c
    b=c
    c=d

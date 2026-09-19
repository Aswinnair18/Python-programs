#generate all factors of a number

number = int(input("Enter a number: "))
print("factors are:")
for i in range(1,number+1):
    if number % i ==0:
        print(i)
        
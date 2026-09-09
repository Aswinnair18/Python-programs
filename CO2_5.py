#Display the given pyramid step number accepted from the user
L=int(input("Enter a number"))
for i in range(1, L+1):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()
    
# count the number of the characters(character frequency) in a string.

string=input("Enter a string:")
d={}
for i in string:
    if i in d:
        d[i]+1
    else:
        d[i]=1
print ("Charcter frequnency=",d)



 
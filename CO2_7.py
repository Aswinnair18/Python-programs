#Add 'ing' at the end of the given string if already ends with 'ing' then add 'iy'

string=input("Enter a string==>")
length=len(string)
if length>2:
    if string[-3]=="ing":
        string+="ly"
    else:
        string+="ing"
    print("The string=>,string") 
else:
    print("string is too short")
           


li=[]
limit=int(input("Enter the range=>"))
for i in range(limit):
    word=input("Enter a word=>")
    li.append(word)
length=0
longword=""
for i in li:
    if len(i)>length:
        length=len(i)
        longword=i
print("length of the longest word is =>",length,longword)


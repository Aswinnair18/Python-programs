#list comprehension
#(a) generate positive list of numbers from a given list of integers

numbers=[-9,13,-20,5,35,18]
positive_number=[x for x in numbers if x>0]
print("Positive number:",positive_number)

#square of N number
n=5
squares=[x*x for x in range (1,n+1)]
print("square of n number:",squares)

#form a list of vowels selected from a given word
word="python programming"
vowels=[char for char in word if char in "aeiouAEIOU"]
print("Vowels in the word:",vowels)

#list ordinary valu of each element of a word
word="hello"
ordinal_values=[ord(char) for char in word]
print("ordinal values:",ordinal_values)

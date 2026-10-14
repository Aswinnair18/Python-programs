d = {'a' : 3, 'b' : 1, 'c' : 2}
ascending = dict(sorted(d.items()))
descending = dict(sorted(d.items(), reverse=True))
print("ascending:", ascending)
print("descending:", descending)
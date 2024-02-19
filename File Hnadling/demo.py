import os
os.path('data.txt')
f = open("data.txt" , mode = "r")
words = 0
chars = 0
lines = 0
for line in f:
    lines += 1
    line = line.strip("\n")
    chars += len(line)
    lst1 = line.split()
    words += len(lst1)
f.close()
print("Number of lines = ",lines)
print("Number of characters = ",chars)
print("Number of words = ",words)
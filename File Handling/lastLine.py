fin = open("data.txt" , "r")
lineList = fin.readlines()
print("Last line = ",lineList[-1])
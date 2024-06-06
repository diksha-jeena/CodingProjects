
s = 0
drr = {"aa" : 12 , "xyz" : 33 , "Turkey" : 77 , "Istanbul" : 23}
for i in drr:
    if(len(i) > 3):
        s += drr[i]
print(s)

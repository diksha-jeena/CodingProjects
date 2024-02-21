tpl1 = (11 , 21 , 31 , 42 , 51)
t1 = list(tpl1)
t1[-2] = 41
tpl = tuple(t1)
print("Original tuple = " ,tpl1)
print("Modified tuple = " ,tpl)
A={10,20,30,40,50}
B={70,60,40,100,80}
sets.add(10)
sets.clear()
sets.copy()
print(A.difference(B))
print(B.difference(A))
A.difference_update(B)
print(A)


l1 = ["Accounts", "English", "Computer"]
l2 = ["S.Aswal", "G.Sah", "M.Harbola"]
dict1 = {}
n = len(l1)
for i in range(n):
  dict1[l1[i]] = l2[i]
print(dict1)

l3 = []
l4 = []
k = dict1.keys()
v = dict1.values()
l3.extend(k)
l4.extend(v)
print(l3,l4)

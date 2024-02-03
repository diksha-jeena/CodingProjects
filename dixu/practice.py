x,y=5,6
x,y=y,x
print(x,y)

dict={"one":"I","two":"II","three":"III","five":"V","ten":"X","fifty":"L","hundred":"C"}
print(dict["hundred"]+dict["fifty"]+dict["ten"]+dict["ten"]+dict["ten"]+dict["one"]+dict["five"])
print(dict["fifty"]+dict["ten"]+dict["one"]+dict["five"])
print(dict["fifty"]+dict["ten"]+dict["ten"]+dict["ten"]+dict["five"]) 
print(dict["ten"]+dict["hundred"]+dict["five"]+dict["three"])
print(dict["hundred"]+dict["two"])


twoDArr=[ 
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
]
twoDStr = ""
for i in twoDArr:
    for j in i:
        twoDStr += str(j)
print(twoDStr)

num = [
    [1,6,54],
    [22,29,5],
    [87,52,65]
]
even = []
odd = []
evenStr = ""
for i in num:
    for j in i:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
print(even,odd)
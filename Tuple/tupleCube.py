tpl = eval(input("Enter a list of some random numbers inside parentheses:"))
cubed_elemnts = []
c = 1
for i in tpl:
    c = i ** 3
    cubed_elemnts.append(c)
print(cubed_elemnts)
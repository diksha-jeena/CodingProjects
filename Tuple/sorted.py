tpl = eval(input("Enter a tuple :"))
n = len(tpl)
mid = n // 2
if(n % 2 == 1):
    mid += 1
half = tpl[:mid]
if(sorted(half) == list(tpl[:mid])):
    print("The first half of the tuple is sorted ")
else:
    print("The first half of the tuple is not sorted ")


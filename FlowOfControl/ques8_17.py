#difference between break and continue
print("The loop with 'Break' statement looks like this :")
for i in range(0,11):
    if(i == 5):
        break
    else:
        print(i)

print("The loop with 'Continue' statement looks like this :")
for i in range(0,11):
    if(i <= 9):
        continue
    else:
        print(i)
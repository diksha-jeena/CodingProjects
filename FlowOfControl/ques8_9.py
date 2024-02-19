char = input("Enter a single character : ")
if(char >= "A" and char <= "Z"):
    print("This is a uppercase character ")
elif(char >= "a" and char <= "z"):
    print("This is a lowercase letter ")
elif(char >= "0" and char <= "9"):
    print("You entered a digit")
else:
    print("You entered a special character")


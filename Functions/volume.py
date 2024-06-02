def volCuboid(L , W , H):
    volume = L * W * H
    return volume


#main
L = float(input("Enter the lenght :"))
W = float(input("Enter the Width :"))
H = float(input("Enter the Height :"))
print(volCuboid(L , W , H))
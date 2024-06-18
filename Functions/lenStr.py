def lenWords(STRING):
    L = []
    for words in STRING.split():
        L.append(len(words))
    T = tuple(L)
    return T
STRING = input("Enter any string :")
print(lenWords(STRING))
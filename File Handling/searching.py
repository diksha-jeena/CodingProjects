with open('example.txt', 'w') as fh:
    fh.write("bdhseafgyij")


with open('example.txt', 'r') as fh:
    for i in fh.read():
        if 'a' == i:
            print(i)

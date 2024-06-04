with open('notes2.txt' , 'w') as fh :
    fh.write(" If someone says that  the output is to be ")
    fh.write("  displayed you know which device it will be displayed on . ")

with open('notes2.txt' , 'r') as fh :
    content = fh.read()
processed_content = ' '.join(content.split())

with open('notes2.txt' , 'w') as fh :
    fh.write(processed_content)

print(processed_content)

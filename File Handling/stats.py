with open('stats.txt' , 'w') as fh :
    fh.write("read() - it reads the entire file and return it in a string \n" )
    fh.write("readline() - it reads a single line at a time\n") 
    fh.write("readlines() - it reads all the lines from file and returns it in a list")


def stats (filename) :
    longest = ""
    with open(filename , 'r') as file :
        for line in file:
            if(len(line) > len(longest)) :
                longest = line
    print("Longest line's length = " , len(longest))
    print(longest)

stats('stats.txt')
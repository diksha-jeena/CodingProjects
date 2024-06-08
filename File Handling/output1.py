with open('output1.txt' , 'w') as file :
    file.writelines("God made the earth"  '\n'  'Man made confining countries'  '\n'  'and their fancy- frozen boundaries' 
               '\n'  "But with unfound boundless love " '\n' "I behold the borderLand of my India " '\n' "Expanding into the world" '\n' "Hail , mother of religions , lotus , scenic beauty , and sages!")
    
obj1 = open("output1.txt" , 'r')
s1 = obj1.readline()
s2.readline(10)
s3 = obj1.read(15)
print(s3)
print(obj1.readline())
obj1.close()
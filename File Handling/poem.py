with open('poemBTH.txt' , 'w') as file :
    file.writelines("God made the earth"  '\n'  'Man made confining countries'  '\n'  'and their fancy- frozen boundaries' 
               '\n'  "But with unfound boundless love " '\n' "I behold the borderLand of my India " '\n' "Expanding into the world" '\n' "Hail , mother of religions , lotus , scenic beauty , and sages!")

with open('poemBTH.txt' , 'r') as file:
    temp = file.read(100)
    print(temp)
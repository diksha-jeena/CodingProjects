#tc=O(N)
#sc=O(1)
dict={"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z"}
aplha=input("enter any aplhabet")
for i in dict:
    if(aplha==i):
        print(dict[i])

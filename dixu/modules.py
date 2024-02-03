def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a//b
def mul(a,b):
    return a*b
def pow(a,b):
    return a**b
def fact(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return product
def sumTillN(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i
    return sum
def printTable(n):
    for i in range(1,11):
        print(n*i)
def circleArea(r):
    ans=1
    ans=3.14**r
    return round(ans,2)
def circleCircumference(r):
    ans=1
    ans=2*3.14*r
    return round(ans,2)
def square(n):
    ans=1
    ans=n*n
    return ans
def cube(n):
    ans=1
    ans=n**3
    return ans
def rectangleArea(l,b):
    ans=1
    ans=l*b
    return ans
def rectanglePerimeter(l,b):
    ans=1
    ans=2*(l+b)
    return ans
def lowerToUpper(alpha):
    dict={"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z"}
    n=len(dict)
    for i in dict:
        if(alpha==i):
            return dict[i]
def upperToLower(alpha):
    dict={"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g","H":"h","I":"i","J":"j","K":"k","L":"l","M":"m","N":"n","O":"o","P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u","V":"v","W":"w","X":"x","Y":"y","Z":"z"}
    n=len(dict)
    for i in dict:
        if(alpha==i):
            return dict[i]
def even(n):
    even=0
    if(n%2==0):
        return True
def odd(n):
    odd=0
    if(n%2!=0):
        return False
def evenTill(n):
    for i in range(1,n+1):
        if(i%2==0):
            print(i)
def oddTill(n):
    for i in range(1,n+1):
        if(i%2!=0):
            print(i)
def numDivBy2(n):
    if(n%2==0):
        return True
def numDivBy3(n):
    if(n%3==0):
        return True
def numDivBy5(n):
    if(n%5==0):
        return True
def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
def celToFeh(c):
    f=1
    f=(c*(9/5))+32
    return f
def fehToCel(f):
    c=1
    c=(f-32)*(5/9)
    return c
def validNumber(n):
    if(n<0):
        return "negative"
    elif(n>0):
        return "positive"
    elif(n==0):
        return "zero"
def divisibilityTest(a,b):
    if(a%b==0):
        return True
    return False
def ar(a,b):
    c=1
    c=(1/2)*(a*b)
    return c
def length(arr):
        n=0
        for i in arr:
            n=n+1
        return n

    

def print10():
    i=1
    while(i<=10):
        print(i)
        i=i+1

        

print(validNumber(0))
print(celToFeh(100))
print(fehToCel(212))
print(add(2,3))
print(sub(5,3))
print(div(4,2))
print(mul(2,4))
print(pow(2,3))
print(fact(5))
print(sumTillN(2))
printTable(5)
print(circleArea(3))
print(circleCircumference(2))
print(square(3))
print(cube(2))
print(rectangleArea(2,4))
print(rectanglePerimeter(3,4))
print(lowerToUpper("r"))
print(upperToLower("R"))
print(even(8))
print(odd(5))
evenTill(10)
oddTill(10)
print(numDivBy2(10))
print(numDivBy3(9))
print(numDivBy5(20))
print(isPrime(13))
print(isPrime(12))
print(divisibilityTest(10,2))
print(ar(2,3))
print(print10)
print10()
print(length([3,2,4,5,6,7,4]))














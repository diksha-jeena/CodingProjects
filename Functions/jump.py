def fun():
    print("I am inside the function")
    fun2()
def fun2():
    print("inside fun2")




#main
fun()
print("now outside the function")
fun()
print("outside")
fun()
print("outside")
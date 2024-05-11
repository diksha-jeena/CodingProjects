def str1():
    return("Hey")
def str2():
    return("This is ")
def str3():
    return("Diksha")
tpl = (str1 , str2 , str3)
n = len(tpl)
def runAll(tpl):
    for i in range(n):
        print(tpl[i]())
runAll(tpl)
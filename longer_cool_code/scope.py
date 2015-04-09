value = 3

def printValue():
    print (value)

def incrementValue():
    global value
    value = value+1

value = 20
printValue()
incrementValue()
printValue()

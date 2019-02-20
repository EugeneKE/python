#a=12222.123456789
#dig = 5
def myFinding(a, dig):
    aStr = list(str(a))
    st = aStr.index('.')
    aStr.pop(st)
    myFloatLen = len(aStr)-st
    myInt =len(aStr)-myFloatLen
    myCicleLen = myFloatLen - dig
    aInt = list(map(int, aStr[::-1]))
    i=0
    while i < (len(aInt)-myInt-dig):
        if aInt[i] >= 5:
            aInt[i+1] += 1
        elif aInt[i] == 9:
            aInt[i] = 9

        i += 1
    myRes = list(map(str,(aInt[::-1])))
    myRes.insert(st,'.')
    myFindNum = ''
    for t in (myRes[:myInt+dig+1]):
        myFindNum += t
    return myFindNum
print(myFinding(1.787868687, 5))
# Functions corresponding to array/list manipulations

# Return the first element of the array
def getFirstElement(array):
    return array[0]

# Return the last element of the array
def getLastElement(array):
    return array[-1]

# Return first 3 elements
def getFirstThreeElements(array):
    return array[0:3]

'''
Return last 3 elements:
array = [1, 'Test', True, 5, '3', False]
expected result = [5, '3', False]
slice(start, end, step)
'''
def getLastThreeElements(array):
    
    return array[-3::1]

'''
Return all integers in the array
array = [1, 'Test', True, 5, '3', False]
expected result = [1, 5]
'''
def getIntegers(array):
    newArr = []
    for element in array:
        # if type(element) is int:
        if isinstance(element, int) and not isinstance(element, bool):
            newArr.append(element)
    print(newArr)
    return newArr
    

# Return all string in the array
def getStrings(array):
    arrstr = []
    for element in array:
        if isinstance(element,str):
            arrstr.append(element)
    print (arrstr)
    return arrstr

# Return all booleans in the array
def getBooleans(array):
    arrbool = []
    for element in array:
        if isinstance(element,bool):
            arrbool.append(element)
    return arrbool

# Return the array reversed
def getReversed(array):
    arrReversed = list(reversed(array))
    return arrReversed
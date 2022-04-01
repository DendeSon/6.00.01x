#Problem 5

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    temp = {}
    result = []
    for value in aDict.values():
        if value in temp.keys():
            temp[value] += 1
        else:
            temp[value] = 1
    for key in aDict.keys():
        if temp[aDict[key]] == 1:
            result.append(key)
    return sorted(result)
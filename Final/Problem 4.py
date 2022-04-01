#Problem 4

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    dct = {}
    dctOdd = {}
    for i in L:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    for j in dct:
        if dct[j]%2 != 0:
            dctOdd[j] = dct[j]
    if len(dctOdd) >= 1:
        return max(dctOdd.keys())
    else:
        return None
#Problem 3

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    sum = 0
    numberCount = 0
    for char in s:
        try:
            item = int(char)
        except ValueError:
            pass
        else:
            sum += item
            numberCount += 1
            
    if numberCount == 0:
        raise ValueError
    else:
        return sum
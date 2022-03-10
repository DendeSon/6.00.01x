# Problem #4: Hand Length
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    count = 0
    for letter in hand.values():
        count += letter
    return count
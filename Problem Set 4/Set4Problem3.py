# Problem #3: Valid Words
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handCopy = hand.copy()    
    wordCheck = False
    if word in wordList:
        wordCheck = True
    
    letterCheck = set(list(word)) <= set(handCopy.keys())
    
    for letter in word:
        if letter in handCopy.keys():
            handCopy[letter] -= 1
            
    valueCheck = all(i >= 0 for i in handCopy.values())
    
    if wordCheck == True and letterCheck == True and valueCheck == True:
        return True
    else:
        return False
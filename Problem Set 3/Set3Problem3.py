# Problem 3 - Printing Out all Available Letters
# 
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLetters = string.ascii_lowercase
    availableLetters = ""
    
    for letter in allLetters:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters                
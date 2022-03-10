# Problem 1 - Is the Word Guessed
# 
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
        else:
            return False
    if count == len(secretWord):
        return True
    else:
        return False
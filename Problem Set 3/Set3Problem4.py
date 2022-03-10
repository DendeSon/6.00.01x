# Problem 4 - The Game
# 
def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guess_list = []
    guess_count = 8
    word_length = len(secret_word)

    print("Welcome to the game, Hangman!\n" + "I am thinking of a word that is " + str(word_length) + " letters long.\n"
          + "-------------")

    while guess_count > 0:
        print("You have", end=" ")
        print(guess_count, end=" ")
        print("guesses left.")
        print("Available letters:", end=" ")
        print(getAvailableLetters(guess_list))

        guess_input = input("Please guess a letter:")

        if guess_input not in guess_list:
            guess_list.append(guess_input)
        else:
            print("Oops! You've already guessed that letter:", end=" ")
            print(getGuessedWord(secret_word, guess_list))
            print("-------------")

            continue

        if guess_input in secret_word:

            print("Good guess:", end=" ")
            print(getGuessedWord(secret_word, guess_list))
            print("-------------")

            if isWordGuessed(secret_word, guess_list):
                print("Congratulations, you won!")
                break
            else:
                continue

        else:
            guess_count -= 1

            print("Oops! That letter is not in my word:", end=" ")
            print(getGuessedWord(secret_word, guess_list))
            print("-------------")

            continue

    else:
        print("Sorry, you ran out of guesses. The word was", end=" ")
        print(secretWord, end=".")
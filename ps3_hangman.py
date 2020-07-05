import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    return not (set(secretWord) - set(lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    return ''.join(['_', s][s in lettersGuessed] for s in secretWord)


def getAvailableLetters(lettersGuessed):
    import string
    lst = [
        s for s in string.ascii_lowercase if s not in lettersGuessed
    ]
    return ''.join(lst)

    

def hangman(secretWord):
    
    print('Welcome to the game, Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')
    mistakesMade = 0
    lettersGuessed = []

    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print('------------')
            print('Congratulations, you won!')
            break
        else:
        	print('------------')
        	print(f'You have {8 - mistakesMade} guesses left.')
        	print(f'Available letters: {getAvailableLetters(lettersGuessed)}')
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print(f'Good guess: {getGuessedWord(secretWord, lettersGuessed)}')
        	elif guess in lettersGuessed:
        		print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
        	elif guess not in secretWord:
        		print(f"Oops! That letter is not in my word: {getGuessedWord(secretWord, lettersGuessed)}")
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('------------')
        	print(f'Sorry, you ran out of guesses. The word was {secretWord}')
        	break
        else:
        	continue



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

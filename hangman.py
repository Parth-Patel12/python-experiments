# Hangman game

### 
#created by: Parth Patel
#@spiritualProgrammr
###
import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    
    w = getGuessedWord(secretWord, lettersGuessed)
    if w == secretWord :
        return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    word2 =''
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            word2 +=secretWord[i]
        else:
            word2 += '_'
        
    return word2




def getAvailableLetters(lettersGuessed):
    word =''
    for l in string.ascii_lowercase:
        	if l not in lettersGuessed:
        		word+=l
    return word

def hangman(secretWord):
    
    guess = 8
    lettersGuessed = []
    flag = 0
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    while guess > 0:
        print('-------------')
        print('You have '+ str(guess) +' guesses left.')
        
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        l = input('Please guess a letter: ')									         	#Use raw_input() for python 2.7
        if(l in secretWord)==False and l in getAvailableLetters(lettersGuessed):
            guess -= 1
            print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
        elif l not in getAvailableLetters(lettersGuessed) :
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        if (l in lettersGuessed) == False :
            lettersGuessed.append(l)
            if(l in secretWord)==True :
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            flag = 1
            print('-------------')
            print('Congratulations, you won!')
            break 
    if flag == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

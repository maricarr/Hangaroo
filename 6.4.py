def isWordGuessed (secretWord, lettersGuessed):
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    else:
        return True

def getGuessedWord(secretWord,lettersGuessed):
    word=""
    for x in secretWord:
        if x in lettersGuessed:
            word+=x
        else:
            word+="_ "
    return word

import string
def getAvailableLetters(lettersGuessed):
    out='' 
    alphabet=string.ascii_lowercase
    for x in alphabet:
        if x in lettersGuessed:
            continue
        else:
            out+=x
    return out

def hangaroo(secretWord):
    print("Hi! Welcome to Hangaroo!")
    print("You are challenged to guess for the secret word!")
    lettersGuessed=[]
    mistakesMade=0
    while (secretWord!=lettersGuessed):
        if secretWord!= getGuessedWord(secretWord,lettersGuessed):
            print("These are the available letters: ", getAvailableLetters(lettersGuessed))
            print(getGuessedWord (secretWord, lettersGuessed))
            print("Mistakes Made= ",mistakesMade)
            guess=input("Please guess a letter: ")
            guessInLowerCase = guess.lower()
            
            if guessInLowerCase not in secretWord and guessInLowerCase not in lettersGuessed:
                mistakesMade+=1
                print("Wrong guess-- Try again! ")
            
            elif guessInLowerCase not in secretWord and guessInLowerCase in lettersGuessed:
                print("You have already guessed that letter!-- Please try again!")
            
            elif guessInLowerCase in secretWord and guessInLowerCase in lettersGuessed:
                print("You have already guessed that letter!-- Please try again!")
        
            else:
                lettersGuessed.append(guessInLowerCase)
                print("Correct guess!")
            lettersGuessed.append(guessInLowerCase)
        else:
            print ("Congratulations, you guessed the word!")
            print("Secret word: ",getGuessedWord (secretWord, lettersGuessed))
            print("Mistakes Made= ",mistakesMade) 
            break
        
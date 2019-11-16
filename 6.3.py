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
        

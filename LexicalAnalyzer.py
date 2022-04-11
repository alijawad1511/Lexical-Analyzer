import re

# Lexical Units
tokens = {
    "Keyword": ["int","float","string","char","print","get"],
    "Operator": ['+','-','='],
    "Punctuation": [';','{','}']
}

# Set of Final States
finalStates = [2,4,5,6,7,8,9]

# Token/Lexeme (Sequence of Characters)
lexeme = ""

def getInput():
    # Take input from comment.txt file
    file = open('input.txt','r')
    inputString = file.read()
    file.close()

    return inputString

def isLetter(character):
    '''This function checks a given character is an alphabet or not.'''

    L = '[a-zA-Z]'    # Match Alphabets

    if re.match(L,character):
        return True
    else:
        return False    

def isNonZeroDigit(digit):
    '''This function checks a given character is an alphabet or not.'''
    
    NZ = '[1-9]'      # Match Digits 1-9

    if re.match(NZ,digit):
        return True
    else:
        return False

def isZeroDigit(digit):
    '''This function checks a given digit is zero or not'''
    
    Z = '0'

    if re.match(Z,digit):
        return True
    else:
        return False

def isDelimeter(character):
    '''This function checks a given character is a whitespace character or not e.g. \n \t space etc.'''
    
    DEL = '\s'        # Match Single Delimeter e.g. ' ', '\t', '\n' etc.

    if re.match(Z,character):
        return True
    else:
        return False


# Get Code input from Text File
inputStr = getInput()

# Set Initial State
currentState = 0

# Iterator
i = 0

L = '[a-zA-Z]'    # Match Alphabets
NZ = '[1-9]'      # Match Digits 1-9
DEL = '\s'        # Match Single Delimeter e.g. ' ', '\t', '\n' etc.
Z = '0'

# Open file to write output
file = open('output.txt','w')

def checkTokenType(lexeme):
    # To show either lexeme is keyword
    flag = True

    for type,value in tokens.items():
        for i in value:
            if i==lexeme:
                file.write(f"<{type}:{i}>\n")
                # if lexeme match with symbols in table
                flag = False
    if(flag):
        file.write(f"<Identifier:{lexeme}>\n")


while i<len(inputStr):

    match currentState:
        case 0:
            if isLetter(inputStr[i]):
                currentState = 1
                lexeme+=inputStr[i]
            elif isNonZeroDigit(inputStr[i]):
                lexeme+=inputStr[i]
                currentState = 3
            elif isZeroDigit(inputStr[i]):
                currentState = -1
            elif inputStr[i]=='+':
                lexeme+=inputStr[i]
                currentState = 7
            elif inputStr[i]=='=':
                lexeme+=inputStr[i]
                currentState = 6
            elif inputStr[i]==';':
                lexeme+=inputStr[i]
                currentState = 5
            elif inputStr[i]=='{':
                lexeme+=inputStr[i]
                currentState = 8
            elif inputStr[i]=='}':
                lexeme+=inputStr[i]
                currentState = 9
            elif isDelimeter(inputStr[i]):
                currentState = 0
        case 1:
            if isLetter(inputStr[i]):
                currentState = 1
                lexeme+=inputStr[i]
            elif isZeroDigit(inputStr[i]):
                currentState = 1
                lexeme+=inputStr[i]
            elif isNonZeroDigit(inputStr[i]):
                currentState = 1
                lexeme+=inputStr[i]
            else:
                # Token ends here
                checkTokenType(lexeme)
                lexeme = ""

                currentState = 2
                i-=1
        case 2:
            currentState = 0
            i-=1
        case 3:
            if isLetter(inputStr[i]):
                currentState = -1
            elif isZeroDigit(inputStr[i]):
                lexeme+=inputStr[i]
                currentState = 3
            elif isNonZeroDigit(inputStr[i]):
                lexeme+=inputStr[i]
                currentState = 3
            else:
                # Token ends here
                currentState = 4
                i-=1
        case 4:
            # Int-literal found
            file.write(f"<Int-Literal:{lexeme}>\n")
            lexeme=""
            currentState = 0
            i-=1
        case 5:
            # --ptr and set currentState to Initial State
            checkTokenType(lexeme)
            lexeme=""
            currentState = 0
            i-=1
        case 6:
            checkTokenType(lexeme)
            lexeme=""
            currentState = 0
            i-=1
        case 7:
            checkTokenType(lexeme)
            lexeme=""
            currentState = 0
            i-=1
        case 8:
            checkTokenType(lexeme)
            lexeme=""
            currentState = 0
            i-=1
        case 9:
            checkTokenType(lexeme)
            lexeme=""
            currentState = 0
            i-=1

    i+=1

# Check if lexeme is null
if not lexeme=="":
    checkTokenType(lexeme)
    lexeme=""


# Close file after writing tokens
file.close()


# Check Current State final or not
if currentState in finalStates:
    print('Accepted...')
    print(currentState)
else:
    print('Rejected...')
    print(currentState)
        
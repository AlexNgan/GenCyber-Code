#Determines if a passcode is valid. 

isLength 
isCapital 

def passCheck(userInput):
    global isLength 
    global isCapital 
    if len(userInput) < 12:
        print ("Your password is less than 12 letters; too short.")
    elif len(userInput) >= 12:
        isLength = True
    else:
        for char in userInput:
            if char.isupper() == False:
                print("Your password needs at least one capital letter.")
            else:
                isCapital = True

def init():
    global isLength 
    global isCapital 
    passCheck(input("Enter your password: ")) 
    if isLength == True and isCapital == True:
        print("Valid password.")
    else:
        print("Invalid password.")
        
init()

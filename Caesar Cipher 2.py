#Note: This program was originally written in Python 2.3, some functionality may be lost.

# This is a program designed to recieve input then encrypt it with two
# Caesar Ciphers, one for the odd chracters and one for even.

#NOTE: ord() turns a letter into ASCII and chr() converts it back.
#      32 is the ASCII code for a blank space.
#      The ASCII range for capital letters is 65 to 90.

print("---------This is a Caesar Cipher program---------")

#Global variables for the key values.
evenKey = 0
oddKey = 0
maxKey = 94
message = ""

#Function to reset variables, allowing the program to be looped.
def resetKey():
    global evenKey
    global oddKey
    global message
    evenKey = 0
    oddKey = 0
    message = ""

#Prompts user for the key to shift with.
def getKey():
    print("")
    print("The max key (amount by which a character is shifted) size is 94. ")
    global evenKey
    global oddKey
    while evenKey == 0 and oddKey == 0:
        evenKey = int(input("Enter the shift key for even chracters. This must be a nonzero integer. "))
        #Evaluates input
        if evenKey <1 and evenKey> maxKey:
        #If the user enters an int greater than the max or other chracters, an error message is generated and setKey() is called again
            print("Error. I didn't quite get that. ")

        oddKey = int(input("Enter the shift key for odd chracters. This must be a nonzero integer. ")) #Ensures that input is an int
        if oddKey < 1 and oddKey > maxKey:
            print("Error. I didn't quite get that.")
            getKey()
       
#Method to take input.
def getMessage():
    global message
    message = input("Enter the message. ").upper()
    return message
    
#This is the function for encrypting or decrypting.
def caesarCipher(message, oddKey, evenKey):
    translated = ""     #Empty string to store new message.
    
    #Loops until the program evaluates all the chracters of the message.
    #This function is applied to the even characters.
    for char in message:
        extra = 0
        num = ord(char)
        useKey = 0
        if num != 32:     #Skips spaces.
            if message.find(char)%2 == 0:     #Determines if char is even or odd.
                useKey = evenKey
            else:
                useKey = oddKey
            num += useKey
            
            #Wrap-around; keeps num within the ASCII range of letters.
            if num > 90: 
                extra = num - 90
                num = 65 + extra
            elif num < 65: 
                extra = 65 - num
                num = 90 - extra
        translated += chr(num)
    print("The message is now:", translated  + ".")

#Sets mode of program to encrypt or decrypt.
def setMode():
    global evenKey
    global oddKey
    mode = input("Do you want to encrypt or decrypt this? Enter 'e' or 'd': ")
    
    if mode == "e":
        #Nothing needs to be done to the keys for encyrption.
        caesarCipher(message, oddKey, evenKey)
            
    elif mode == "d":
        #For decryption, the negative of the key is used to reverse the encryption.
        oddKey = -oddKey 
        evenKey = -evenKey
        caesarCipher(message, oddKey, evenKey)
        
    #Error message. In the event that the user mistypes, the program asks again.
    else:
        print("I'm sorry, I didn't quite get that.")
        setMode()

#Keeps program running by calling other methods until user terminates.      
def startProgram():
    while True:
        print("")
        init = input("Hit 'y' to start the program and 'n' if you want to exit: ")
        #Allows program to be run again from the shell.
        if init == "y":
            resetKey()
            getKey()
            getMessage()
            setMode()
        elif init == "n":
            break

startProgram()

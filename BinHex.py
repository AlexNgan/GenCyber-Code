#BinHex.py
#Converts ASCII to hex.
def ASCIIToHex(letter):
    letterA = ord("A")
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hexConversion = "0123456789ABCDEF"
    letterIndex = alpha.find(letter)
    value = letterA + letterIndex
    leftNum = value//16
    rightNum = value%16
    return hexConversion[leftNum] + hexConversion[rightNum]
    
#Converts bits to hexadecimal.
def BinToHex(bitString):
    result = 0
    power = len(bitString)
    hexConvers = "0123456789ABCDEF"
    for s in bitString:
        lilBit = int(s)
        power -= 1
        result += (lilBit * (2**power))
    finalHex = hexConvers[result]
    return finalHex

#Converts binary to decimals.
def BinToDec(bitString):
    result = 0
    power = len(bitString)
    for s in bitString:
        lilBit = int(s)
        power -= 1
        result += (lilBit * (2**power))
    return result

def init():
    print("This is a tool that converts binary into either hex or decimal. Or ASCII into hex.")
    while True:
        convert = input("Enter the binary or ASCII to convert: ")
        command = input("Enter 'h' for hex, 'd' for decimal, or 'a' for ASCII to hex. Enter 'q' to quit. ")
        if command == "h":
            print(BinToHex(convert))
        elif command == "d":
            print(BinToDec(convert))
        elif command == "a":
            print(ASCIIToHex(convert))
        elif command == "q":
            break
        
init()

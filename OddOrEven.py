#Identifies an integer number as odd or even.

def OddOrEven(num):
    rem = num % 2
    if rem == 0:
        print(num,"is even.")
    else:
        print(num, "is odd.")

def BigOrSmall(num):
    if num > 100:
        print(num, "is big.")
    else:
        print(num, "is small.")
def init():
    try:
        number = int(input("Enter a numerical number: "))
        OddOrEven(number)
        BigOrSmall(number)
    except ValueError:
        print("That doesn't look like an integer, friend.")
        
init()

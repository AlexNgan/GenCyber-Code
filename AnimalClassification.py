#Author: Gloria

def guessAnimal():
    #print("Press 'q' at any time to quit.")
    print("Pick an animal (cat, dog, pidgeon, ostrich, turtle, or salmon) and I'll try to guess it. ")
    print("Enter 'y' or 'n' to answer.")
    
    #Ostrich and pidgeon.
    hasWings = input("Does it have wings? ")
    if hasWings == 'y':
        isNewYorker = input("Is it naturally found in NYC? ")
        if isNewYorker == 'y':
            print("It's a pidgeon! That's gross.")
            return ""
        else:
            print("You've picked an ostrich.")
            return ""
    
    #Salmon and turtle.
    coldBlood = input("Is it coldblooded? ")
    if coldBlood == 'y':
        hasShell= input("Does it have a shell?")
        if hasShell == 'y':
            print("You've picked a turtle!")
            return ""
        else:
            print("Salmon. I knew this was fishy.")
            return ""
    
    #Cat and dog.
    canBark = input("Does the animal bark? ")
    if canBark == 'y':
        print("Nice. A dog.")
        return ""
    else:
        print("You picked a cat!")
        return ""
        
guessAnimal()
            
    
        
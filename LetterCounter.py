def letterCount():
    word = input("Enter a word: ")
    letter = input("Enter a letter which you would like me to count the occurrences of: ")
    count = 0
    
    for char in word:
        if char == letter:
            count += 1
    
    print("The letter", letter, "occurs", count, "times in", word, ".")

letterCount()

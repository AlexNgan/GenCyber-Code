#Author: Gloria 

#Function to solve ed % totient = 1, for d (decryption jey). 
def keyFinder(e, tot):
    d = 1
    while True:
        ans = (e*d) % tot
        if(ans ==1):
            return d
        else:
            d += 1
            
print(keyFinder(13,8))
#Author: Gloria 
from datetime import datetime

def studentType():
    name = input("Enter your name: ")   
    gradYear = int(input("Enter your graduation year: "))
    currYear = int(datetime.year)
    types = ["not in high school yet","a freshman","a sophomore","a junior","a senior","a graduate"]
    
    index = currYear - gradYear
    if index < 0:
        index = 0
    
    print(name,"is",types(index),".")

studentType()
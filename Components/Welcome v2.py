import random
from random import randint

# List fo random names
names = ["Rose", "Lily", "Eric", "Lyle", "Bella", "James", "Isabella", "katie", "Jack", "Lara"]
def welcome():
    '''
 Purpose: To generate a random name from the list and print out
 a welcome message
 Parameters: None
 Returns: None
    '''
    num = randint (0,9)
    name = (names[num])

    print("***** Welcome to Jules Jewellery *****")
    print("***** My name is", name, "*****")
    print("***** I will be here to help you order your wonderful Jules Jewellery *****") 

def main():
    '''
 Purpose: To run all functions 
 a welcome message
 Parameters: None
 Returns: None
    '''
    welcome()


main()
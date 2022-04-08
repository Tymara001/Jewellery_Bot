# Jewellery bot program
import random
from random import randint

# List fo random names
names = ["Rose", "Lily", "Eric", "Lyle", "Bella", "James", "Isabella", "katie", "Jack", "Lara"]

# Welcome message with random name 
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

# Menu for pick up or delivery





# Pick up information - name and phone number 






# Delivery information - name adress and phone 





# Choose total number of accessories - max 10







# Jewellery menu






#Jewellery order - from menu - print each jewellery out with cost





#Prin order out - including if order is del or pick up and names and price of each jewellery - total cost including any delivery charge




#Ability to cancel or proceed with order






#Option for new order or to exit






#Main function
def main():
    '''
 Purpose: To run all functions 
 a welcome message
 Parameters: None
 Returns: None
    '''
    welcome()


main()
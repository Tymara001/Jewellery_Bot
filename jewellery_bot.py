# Jewellery bot program
import random
from random import randint

# List fo random names
names = ["Rose", "Lily", "Eric", "Lyle", "Bella", "James", "Isabella", "katie", "Jack", "Lara"]
#Customer details dictionary
customer_details = {}

# vaildates inputs to check if they are blank
def not_blank(question):
    vaild = False
    while not vaild:
       response = input(question)
       if response != "":
           return response.title()
       else:
           print("This cannot be blank")


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

def order_type():
    print ("Is your order for pickup or delivery?")
    print (" For pickup please enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:   
                if delivery == 1:
                    print ("Pickup")
                    pickup
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is not a vaild number")
            print("Please enter 1 or 2")


# Pick up information - name and phone number 
def pickup():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])
    print(customer_details)





# Delivery information - name adress and phone 





# Choose total number of accessories - max 10







# Jewellery menu






#Jewellery order - from menu - print each jewellery out with cost





#Print order out - including if order is del or pick up and names and price of each jewellery - total cost including any delivery charge




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
    order_type()
    pickup()


main()
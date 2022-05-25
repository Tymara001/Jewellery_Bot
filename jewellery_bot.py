# Jewellery bot program
#24/05/22
#Bugs - Phone number allows numbers
#     - Name input allows numbers

import random
from random import randint

# List fo random names
names = ["Rose", "Lily", "Eric", "Lyle", "Bella", "James", "Isabella", "katie", "Jack", "Lara"]
# lists of jewellery names
jewellery_names = ['moon ring','cycstle ring','promise ring', 'friendship ring','ruby ring','rose quartz ring',
                 'crystal bracelet','charm breacelet','rose quartz necklace','jade cryctle bracelet','gemstone necklace',
                 'tiger eye bracelet']
# lists of jewellery pices
jewellery_prices = [9.50, 9.50, 9.50, 9.50, 9.50, 9.50, 12.50, 12.50, 12.50, 12.50, 12.50, 12.50]

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
                    pickup_info()
                    break

                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else:
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is not a vaild number")
            print("Please enter 1 or 2")


# Pick up information - name and phone number 
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    #print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    #print (customer_details['phone'])


# Delivery information - name adress and phone 
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])


# Jewellery menu
def menu():
    number_jewellery = 12

    for count in range (number_jewellery):
     print("{} {} ${:.2f}"    .format(count+1,jewellery_names[count],jewellery_prices[count]))






# Choose total number of jewellery - max 6






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
    menu()


main()
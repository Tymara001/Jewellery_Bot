#Customer details dictionary
customer_details = {}


def not_blank(question):
    vaild = False
    while not vaild:
       response = input(question)
       if response != "":
           return response
       else:
           print("This cannot be blank")
     


#Basic instructions
question = ("Please enter your name ")
customer_details['name'] = not_blank(question)
print (customer_details['name'])

question = ("Please enter your phone number ")
customer_details['phone'] = not_blank(question)
print (customer_details['phone'])
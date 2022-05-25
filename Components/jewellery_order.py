# lists of jewellery names
jewellery_names = ['moon ring','cycstle ring','promise ring', 'friendship ring','ruby ring','rose quartz ring',
                 'crystal bracelet','charm breacelet','rose quartz necklace','jade cryctle bracelet','gemstone necklace',
                 'tiger eye bracelet']
# lists of jewellery pices
jewellery_prices = [9.50, 9.50, 9.50, 9.50, 9.50, 9.50, 12.50, 12.50, 12.50, 12.50, 12.50, 12.50]

#list to store ordered jewellerys
order_list =[]
#list to store jewellerys prices
order_cost = []

#list to store order cost
def menu():
    number_jewellery = 12

    for count in range (number_jewellery):
     print("{} {} ${:.2f}"    .format(count+1,jewellery_names[count],jewellery_prices[count]))

menu()

# ask for total number of jewellery for order
num_jewellerys = 0

num_jewellerys = int(input("How many jewellerys do you want to order? "))

print(num_jewellerys)

#Choose jewellery from menu
print ("Please choose your jewellerys by entering the number from the menu")
for item in range(num_jewellerys):
    while num_jewellerys > 0:
        jewellery_ordered = int(input())
        order_list.append(jewellery_names[jewellery_ordered])
        order_cost.append(jewellery_prices[jewellery_ordered])
        num_jewellerys = num_jewellerys-1

print(order_list)
print(order_cost)



#Countdown until all jewellery are ordered





#Print order
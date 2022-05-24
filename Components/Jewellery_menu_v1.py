jewellery_names = ['moon ring','cycstle ring','promise ring', 'friendship ring','ruby ring','rose quartz ring',
                 'crystal bracelet','charm breacelet','rose quartz necklace','jade cryctle bracelet','gemstone necklace',
                 'tiger eye bracelet']

jewellery_prices = [9.50, 9.50, 9.50, 9.50, 9.50, 9.50, 12.50, 12.50, 12.50, 12.50, 12.50, 12.50]

def menu():
    number_jewellery = 12

    for count in range (number_jewellery):
     print("{} {} ${:.2f}"    .format(count+1,jewellery_names[count],jewellery_prices[count]))

menu()
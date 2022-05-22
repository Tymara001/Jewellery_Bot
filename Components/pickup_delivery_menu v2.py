# Bugs
# will only work vaild input "d" and "p"
#vaild input triggers else statement but program does not input again.

# menu so that user can choose either pickup or delivery

print ("Do you want you order delivered or are you picking it up?")

print (" For delivery enter d")
print ("For pickup enter p")

delivery = input ()

if delivery == "d":
    print ("Delivery")

elif delivery == "p":
    print ("Pickup")

else:
    print ("That was not a vaild input")
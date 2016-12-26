# -*- coding: utf-8 -*-

menu_list = []

print "This is the Restaurant menu database"

while True:
    dish = raw_input("Enter the name of the dish here: ")
    price = float(raw_input("Enter the price of the dish: "))
    print "The daily dish is %s and its price is %.2f Euros" %(dish, price) #wie kann man die anzahl der nachkommastellen reduzieren?
    menu = dish + " - Euro " + str(price)
    menu_list.append(menu)
    status = raw_input("Do you want to enter another dish? (yes/no)")

    if status == "no":
        break

print "\nYou added %d new dishes to your database. The following will be saved in a text-file: " % (len(menu_list))
for item in menu_list:
    print item

with open("menu.txt", "w+") as menu_file:
    menu_file.write("list of menus:\n")
    for item in menu_list:
        menu_file.write(item + "\n")


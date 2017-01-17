from Tkinter import *
import tkMessageBox

menu_list = []

window = Tk()
window.geometry('530x320')

greeting = Label(window, text="This is the Restaurant menu database")
greeting.pack()

inputmenu = Label(window, text="Enter the name of the dish:")
inputmenu.pack()

dish = Entry(window)
dish.pack()

inputprice = Label(window, text="Enter the price:")
inputprice.pack()

price = Entry(window)
price.pack()


def OnButtonPress():
    result_text = "Your dish has been successfully added to your database, you can add another dish"

    tkMessageBox.showinfo("Saved!", result_text)


button = Button(window, text="Save", command=OnButtonPress)
button.pack()

saving = Label(window, text="If you close this window this will create a text-file with the dishes called menu.txt")
saving.pack()

window.mainloop()

#menu = dish " - Euro "  str(price)
#menu_list.append(menu)

with open("menu.txt", "w+") as menu_file:
    menu_file.write("list of menus:\n")
    for item in menu_list:
        menu_file.write(item + "\n")
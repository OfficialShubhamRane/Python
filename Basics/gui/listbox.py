def submit():
    print(listBox.get(listBox.curselection()))

def add():
    listBox.insert(listBox.size(), entryBox.get())

from tkinter import *

window = Tk()

listBox = Listbox(window,
                    bg="#f7ffde",
                    font=("Constantia",35),
                    width=12)

listBox.pack()

listBox.insert(1,"pizza")
listBox.insert(2,"burger")
listBox.insert(1,"garlic bread")
listBox.insert(2,"fried calamari")

listBox.config(height=listBox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,text="add", command=add)
addButton.pack()

submitButton = Button(window,text="submit", command=submit)
submitButton.pack()



window.mainloop()
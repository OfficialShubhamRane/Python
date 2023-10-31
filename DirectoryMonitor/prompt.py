import os
import tkinter as tk



# Create a function to be called when the "OK" button is clicked
def ok_button_clicked():
    print("OK button clicked")
    window.destroy()





# Create the main application window
window = tk.Tk()
window.title("Directory Monitor")
window.geometry("300x50+850+400")

# Create a label widget
label = tk.Label(window, text="Directory monitor has started")
label.pack()

# Create an "OK" button and associate the function with it
ok_button = tk.Button(window, text="OK", command=ok_button_clicked)
ok_button.pack()



# Start the main event loop

window.mainloop()


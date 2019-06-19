from tkinter import *
from main import interpret
 
window = Tk()
 
window.title("Window Title")
window.geometry('600x200')

nameLabel = Label(window, text="Name: ")
nameLabel.grid(column=0, row=0)

descriptionLabel = Label(window, text = "Description: ")
descriptionLabel.grid(column=0, row = 1)

dateLabel = Label(window, text = "Date: ")
dateLabel.grid(column=0, row = 2)

deadlineLabel = Label(window, text = "Has deadline: ")
deadlineLabel.grid(column=0, row = 3)

colorLabel = Label(window, text = "Color: ")
colorLabel.grid(column=0, row = 4)
 
sv = StringVar()

txt = Entry(window,width=70, textvariable=sv)
txt.grid(column=0, row=5)

def update(a, b, c):
    text = sv.get()
    result = interpret(text)

    nameLabel.configure(text="Name: " + result["name"])
    descriptionLabel.configure(text="Description: " + result["description"])
    dateLabel.configure(text="Date: " + str(result["date"]))
    deadlineLabel.configure(text="Has deadline: " + str(result["has_deadline"]))
    colorLabel.configure(text="Color: " + result["color"])
 
sv.trace_add("write", update)

window.mainloop()
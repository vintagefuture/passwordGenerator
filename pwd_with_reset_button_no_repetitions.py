from tkinter import *

def createPassword():

    import secrets
    import string
    piece1 = ''
    piece2 = ''
    piece3 = ''

    t = 'ioqxnmzvdbIOQXNMZVDB' # letters to exclude becuase difficult to pronounce and understand

    for x in range(0, 3):
        piece1 += secrets.choice(string.ascii_lowercase.translate({ord(i): None for i in t+piece1}))

    for x in range(0, 3):
        piece2 += secrets.choice(string.digits.translate({ord(i): None for i in piece2}))
    for x in range(0, 3):
        piece3 += secrets.choice(string.ascii_uppercase.translate({ord(i): None for i in t+piece3+piece1.upper()}))

    password = (piece1 + piece2 + piece3)
    #s = " ".join(repr(e) for e in password)
    e.delete(0, END)
    e.insert(0, password)
	
def cleanScreen():
	e.delete(0, END)
    
root = Tk()
#root.geometry("200x200")
root.title('Password Generator')

#label = Label(root, text="Password Generator")
e = Entry(root, width=12, justify = CENTER, font = "Helvetica 44 bold")

button1 = Button(root, text="Generate password", command=createPassword, font = "Helvetica 20 bold")
button2 = Button(root, text="Reset", command=cleanScreen, font = "Helvetica 20 bold")

#label.grid(row=0, sticky= N)
e.grid(row=1, sticky=N, columnspan = 2)
button1.grid(row = 2, column=0, sticky=N)
button2.grid(row = 2, column=1, sticky=N)

root.mainloop()
 

# from tkinter import *
#
# root = Tk()
# root.geometry('200x150')
# root.maxsize(640, 740)
# root.minsize(200, 250)
# root.title('tasbix')
# root.config(bg='orange')
# buttoncount = 0
# color = ['white', 'blue', 'yellow', 'red', 'green', 'black', 'pink', 'orange']
#
#
# def btn():
#     global color
#     global buttoncount
#     button1.config(bg=color[buttoncount])
#     buttoncount += 1
#     if buttoncount == 8:
#         buttoncount = 0
#
#
# button1 = Button(root, text=0, bg='orange', width=8, height=2, command=btn)
# button1.pack()
# root.mainloop()
from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, bg="yellow", fg="red", font="Algerian", textvariable=var, relief=RAISED )
var.set("Assalom-u alaykum! ")
label.pack()
root.mainloop()

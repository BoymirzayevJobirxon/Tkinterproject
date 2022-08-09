from tkinter import *

root = Tk()
root.geometry('200x150')
def onclickbutton1():
    print('birinchi button bosildi')
def onclickbutton2():
    print('ikkinchi button bosildi')
def onclickbutton3():
    print('uchinchi button bosildi')

button1 = Button (root, text='click me 1', bg='red',width=8,height=2,command=onclickbutton1)
button2 = Button (root, text='click me 2 ', bg='red',width=8,height=2,command=onclickbutton2)
button3 = Button (root, text='click me 3 ', bg='red',width=8,height=2,command=onclickbutton3)
button1.pack()
button2.pack()
button3.pack()



root.mainloop()

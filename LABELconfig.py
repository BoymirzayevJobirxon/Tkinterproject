# from tkinter import Label,Tk
#
# root = Tk()
# label1 = Label(root,text='option',width=20,height=10,bg='orange')
# label2 = Label(root,text='option',width=20,height=10,bg='red')
# label1.pack()
# label2.pack()
# root.mainloop()
# from  tkinter import Tk,Button,Label
# root = Tk()
# count = 0
# def f():
#     global  count
#     count+=1
#     label.config(text =count)
# def a():
#     global count
#     count -= 1
#
#     label.config(text=count)
#
# label = Label(root,text='zero',bg='orange')
# label.pack()
# btn = Button(root,text='add',bg='green',command=f)
# btn.pack()
# btn1 = Button(root,text='remove',bg='green',command=f)
# btn1.pack()
# root.mainloop()
# from tkinter import Label,Tk
#
# root = Tk()
# lebel1 = Label(root,text='option1',bg='teal',fg='black')
# lebel2 = Label(root,text='option2',bg='teal',fg='black')
# lebel3 = Label(root,text='option3',bg='teal',fg='black')
# lebel4 = Label(root,text='option3',bg='teal',fg='black')
#
# lebel5 = Label(root,text='option4',bg='teal',fg='black',width=10)
#
# lebel1.grid(row= 0 , column=0)
# lebel2.grid(row= 0 , column=1)
# lebel3.grid(row= 0 , column=2)
# lebel4.grid(row= 1, column=0)
# lebel5.grid(row= 0 , column=2)
# root.mainloop()


#
#
#
# lebel1.pack()
# lebel2.pack()
# lebel3.pack()
# lebel4.pack()
# root.mainloop()
from  tkinter import *
root = Tk()
root.geometry('400x500')
def f():
    print(entry.get())
    entry.delete(0,END)
entry = Entry(root,width=20,font=('consolas',24))
btn = Button(root,text='get',font=('consolas',24),command=f)
entry.pack()
btn.pack()
root.mainloop()



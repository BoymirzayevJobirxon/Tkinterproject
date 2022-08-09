# count = 0
# def msg ():
#    global count
#    count+=1
#
# msg()
# msg()
# print(count)


from tkinter import *

root = Tk()
root.geometry('200x150')
count = 0
def msg():
    global count
    count+=1
    print(count)



button1 = Button (root, text='click me 1', bg='red',width=8,height=2,command=msg)

button1.pack()



root.mainloop()

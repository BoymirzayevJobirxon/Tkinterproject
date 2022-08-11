# count = 0
# def msg ():
#    global count
#    count+=1
#
# msg()
# msg()
# print(count)


# from tkinter import *
#
# root = Tk()
# root.geometry('200x150')
# count = 0
# def msg():
#     global count
#     count+=1
#     print(count)
#
#
#
# button1 = Button (root, text='click me 1', bg='red',width=8,height=2,command=msg)
#
# button1.pack()
#
#
#
# root.mainloop()

from tkinter import *

root = Tk()
root.geometry('200x150')
root.maxsize(640,740)
root.minsize(200,250)
count = 0
count2 = 0


def check():
    global count
    count += 1

    print('subhanalloh', count)
    if count == 33:
        print('mashalloh')

    global count2
    if count<=33:
        count2+=1
        print('alhamdulilah',count)


button1 = Button(root, text='📿', bg='orange', width=8, height=2, command=check)

button1.pack()

root.mainloop()

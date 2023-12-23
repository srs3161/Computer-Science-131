from tkinter import *
root = Tk()
root.geometry("355x350")

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)
#frame = Frame(root, borderwidth=8, bg="red" )
#frame.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)



#def hello():
    #print("Hello this is my world")

#def expression():
    #print("the world is dangeros for human being")
##frame = Frame(root, borderwidth=7, bg="grey", relief=SUNKEN)
#frame.pack(side=LEFT, anchor="ne")

##b1 = Button(frame, fg="yellow", text="Navraj Singh", command=hello)
#b1.pack(side=LEFT, padx = 14)

#b2 = Button(frame, fg="yellow", text = "He is the best guy", command=expression)
#b2.pack(side=LEFT, padx = 14)



root.mainloop()
#from turtle import *
#color("red")
#begin_fill()
#pensize()
#left(50)
#forward(133)
#circle(40, 200)
#right(140)
#circle(50,200)
#forward(133)
#end_fill()
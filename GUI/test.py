from Tkinter import *
import turtle

root = Tk()

def Func():
	global app
	app = turtle.shape("turtle")

button1 = Button(root, text = "commit", command = Func)
button1.pack()


root.mainloop()
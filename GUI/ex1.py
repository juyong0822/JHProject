from tkinter import *

repo = "C:\\Users\\juyon\\Desktop\\PythonProject"

class Application(Frame):
	def say_hi(self):
		print("hi there, everyone!")

	def createWidgets(self):
		global photo
		photo = PhotoImage(file = repo + "\\Overwatch.png")

		self.QUIT = Button(self)
		self.QUIT["image"] = photo
		self.QUIT["fg"]   = "red"
		self.QUIT["command"] =  self.quit
		self.QUIT.pack({"side": "left"})

		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack({"side": "left"})

		self.label = Label(self)
		self.label["image"] = photo
		self.label.pack({"side": "left"})

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
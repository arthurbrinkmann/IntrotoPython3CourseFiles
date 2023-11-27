from tkinter import *
from time import *

class MyFrame(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.myCanvas = Canvas(width=300, height=200, bg="darkgreen")
		self.myCanvas.grid()

		my_rect_id = self.myCanvas.create_rectangle(10, 10, 50, 50)
		self.myCanvas.update()

		for count in range(20):
			increment = 20*count
			self.myCanvas.coords(my_rect_id,
				20 + increment, 20 + increment,
				50 + increment, 50 + increment)
			self.myCanvas.update()
			sleep(1)

frame02 = MyFrame()
frame02.mainloop()

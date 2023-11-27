from tkinter import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)

     self.myCanvas = Canvas(width=300, height=200, bg="blue")
     self.myCanvas.grid()

frame02 = MyFrame()
frame02.mainloop()

from tkinter import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)

     self.myCanvas = Canvas(width=300, height=200, bg="blue")
     self.myCanvas.grid()
     self.myCanvas.create_line(1, 1, 200, 200, arrow="first")
     
frame02 = MyFrame()
frame02.mainloop()

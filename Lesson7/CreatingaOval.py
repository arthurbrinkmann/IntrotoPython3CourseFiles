from tkinter import *

class MyFrame(Frame):
  def __init__(self):
     Frame.__init__(self)

     self.myCanvas = Canvas(width=300, height=200, bg="blue")
     self.myCanvas.grid()
     self.myCanvas.create_oval(10, 10, 200, 100, fill="white")
     
frame02 = MyFrame()
frame02.mainloop()

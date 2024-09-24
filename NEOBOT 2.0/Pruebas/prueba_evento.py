from tkinter import *

def H(event):
    print("Has presionado" + event.keysym)
    
window= Tk()


window.bind("<Key>",H)


window.mainloop()
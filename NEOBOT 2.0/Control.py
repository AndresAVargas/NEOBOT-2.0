import serial
import time
import tkinter as tk

window = tk.Tk()
window.configure(background="gray")
window.geometry("320x400")
window.title("Test Motor")

megaboard = serial.Serial('COM4', 9600)

def Control():
    def Fw(event):       
        megaboard.write(b'w')
    
    def Bk(event):
        megaboard.write(b's')

    def RtF(event):
        megaboard.write(b'd')

    def LtF(event):
        megaboard.write(b'a')
    
    def Stop(event):
        print("End of control")
        megaboard.write(b'q')
        megaboard.close()
        window.destroy()
    
    B1 = tk.Button(window,  text="Adelante", command=Fw)
    B2 = tk.Button(window,  text="Atras", command=Bk)
    B3 = tk.Button(window,  text="Adelante D", command=RtF)
    B4 = tk.Button(window,  text="Adelante I", command=LtF)
    B5 = tk.Button(window,  text="Parar", command=Stop)

    B1.grid(row=1, column=10, padx=20, pady=50)
    B2.grid(row=3, column=10, padx=20, pady=50)
    B3.grid(row=2, column=5, padx=20, pady=50)
    B4.grid(row=2, column=15, padx=20, pady=50)
    B5.grid(row=2, column=10, padx=20, pady=50)

    window.bind("<w>", Fw)
    window.bind("<d>", RtF)
    window.bind("<a>", LtF)
    window.bind("<s>", Bk)
    window.bind("<Return>", Stop)

    window.mainloop()

time.sleep(2)
Control()
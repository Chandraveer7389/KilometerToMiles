import tkinter
from tkinter import END

def clicked():
    s = float(input1.get())
    s = s*1.6
    label3.config(text=s)

window = tkinter.Tk()
window.minsize(width=250 , height=100)
window.title("Kilometers to miles converter")
window.config(padx=20,pady=20)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)
label1.config(padx=10,pady=10)

label2=tkinter.Label(text="is equals to")
label2.grid(column=0 , row = 1)
label2.config(padx=10)

label3=tkinter.Label(text="0")
label3.grid(column=1 , row = 1)
label3.config(padx=10)

label4=tkinter.Label(text="Km")
label4.grid(column=2 , row = 1)
label4.config(padx=10)

button = tkinter.Button(text="Calculate", command=clicked)
button.grid(column=1,row=2)

input1 = tkinter.Entry(width=10)
input1.grid(column=1 , row=0)
input1.insert(END,string="0")

window.mainloop()
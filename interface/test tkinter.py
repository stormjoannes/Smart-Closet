from tkinter import *
from tkinter.messagebox import showinfo

def clicked():
    bericht = 'Dit een bericht voor de gebruiker!'
    showinfo(title='popup', message=bericht)

root = Tk()
button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

root.mainloop()
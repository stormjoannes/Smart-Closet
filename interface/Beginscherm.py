from tkinter import *
from PIL import ImageTk, Image
from Main import *

def toonLoginFrame():
    signinframe.pack_forget()
    loginframe.pack()


def toonSignIn():
    loginframe.pack_forget()
    signinframe.pack()

def toonSignUp():
    loginframe.pack_forget()
    signupframe.pack()




root = Tk()

loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)
loginfield = Entry(master=loginframe)
loginfield.pack(padx=20, pady=20)
loginbutton = Button(master=loginframe, text='SIGN IN')
loginbutton.pack(padx=20, pady=20)

signinframe = Frame(master=root)
signinframe.pack(fill="both", expand=True)
signinfield = Entry(master=signinframe)
signinfield.pack(padx=20, pady=20)

signupframe = Frame(master=root)
signupframe.pack(fill="both", expand=True)
signupfield = Entry(master=signupframe)
signupfield.pack(padx=20, pady=20)

toonLoginFrame()
root.mainloop()
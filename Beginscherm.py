from tkinter import *
from tkinter.messagebox import showinfo

from Main import *

def toonLoginFrame():
    signinframe.pack_forget()
    signupframe.pack_forget()
    hoofdframe.pack_forget()
    loginframe.pack()

def toonSignInFrame():
    loginframe.pack_forget()
    hoofdframe.pack_forget()
    signinframe.pack()

def toonSignUpFrame():
    loginframe.pack_forget()
    hoofdframe.pack_forget()
    signupframe.pack()

def toonHoofdFrame():
    signinframe.pack_forget()
    signupframe.pack_forget()
    hoofdframe.pack()

def checkexistendSignIn():
    if checkIfExist(signinfield.get()) == False:
        bericht = 'Deze username is niet in gebruik!!'
        showinfo(title='Username not found', message=bericht)
    else:
        toonHoofdFrame()

def checkexistendSignUp():
    if checkIfExist(signupfieldName.get()) == True:
        bericht = 'Deze username is al in gebruik!'
        showinfo(title='Username already existend', message=bericht)
    else:
        toonHoofdFrame()

root = Tk()

loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)
signinbutton = Button(master=loginframe, text='SIGN IN', command=toonSignInFrame)
signinbutton.pack(padx=20, pady=20)
signupbutton = Button(master=loginframe, text='SIGN UP', command=toonSignUpFrame)
signupbutton.pack(padx=20, pady=20)

signinframe = Frame(master=root)
signinframe.pack(fill="both", expand=True)
signinfield = Entry(master=signinframe)
signinfield.pack(padx=20, pady=20)
signinbuttonframe = Button(master=signinframe, text="SIGN IN", command=checkexistendSignIn)
signinbuttonframe.pack(padx=20, pady=20)


signupframe = Frame(master=root)
signupframe.pack(fill="both", expand=True)

signupnameLabel = Label(master=signupframe,text='Vul hier je naam in',height=2)
signupnameLabel.pack()
signupfieldName = Entry(master=signupframe)
signupfieldName.pack(padx=20, pady=20)

signupstadLabel = Label(master=signupframe,text='Vul hier je stad in:',height=2)
signupstadLabel.pack()
signupfieldStad = Entry(master=signupframe)
signupfieldStad.pack(padx=20, pady=20)

signupstadLabel = Label(master=signupframe,text='Vul hier de afkorting van je land in:',height=2)
signupstadLabel.pack()
signupfieldLand = Entry(master=signupframe)
signupfieldLand.pack(padx=20, pady=20)
signupbuttonframe = Button(master=signupframe, text="SIGN UP", command=checkexistendSignUp)
signupbuttonframe.pack(padx=20, pady=20)

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
hoofdframeToevoegenButton = Button(master=hoofdframe, text="Kleding toevoegen")
hoofdframeToevoegenButton.pack(padx=20, pady=20)
hoofdframeVerwijderenButton = Button(master=hoofdframe, text="Kleding verwijderen")
hoofdframeVerwijderenButton.pack(padx=20, pady=20)
hoofdframeAutomatischButton = Button(master=hoofdframe, text="Setje automatisch genereren")
hoofdframeAutomatischButton.pack(padx=20, pady=20)
hoofdframeGegWijzigenButton = Button(master=hoofdframe, text="Gegevens wijzigen")
hoofdframeGegWijzigenButton.pack(padx=20, pady=20)


toonLoginFrame()
root.mainloop()
import time
from tkinter import *
from tkinter.messagebox import showinfo

from Main import *

def toonLoginFrame():
    global root1
    root1 = Tk()

    signinframe.pack_forget()
    signupframe.pack_forget()
    hoofdframe.pack_forget()
    loginframe.pack()

    signinbutton = Button(master=loginframe, text='SIGN IN', command=toonSignInFrame)
    signinbutton.pack(padx=20, pady=20)
    signupbutton = Button(master=loginframe, text='SIGN UP', command=toonSignUpFrame)
    signupbutton.pack(padx=20, pady=20)

    root.mainloop()

def toonSignInFrame():
    global root2
    root1.destroy()
    root2 = Tk()

    loginframe.pack_forget()
    hoofdframe.pack_forget()
    signinframe.pack()

    Label(master = signinframe, text="Username").pack()
    signinfield = Entry(master=signinframe, textvariable="username")
    signinfield.pack(padx=20, pady=20)

    signinbuttonframe = Button(master=signinframe, text="SIGN IN", command=checkexistendSignIn(signinfield))
    signinbuttonframe.pack(padx=20, pady=20)


def toonSignUpFrame():
    global root3
    root1.destroy()
    root3 = Tk()

    loginframe.pack_forget()
    hoofdframe.pack_forget()
    signupframe.pack()

    signupnameLabel = Label(master=signupframe, text='Vul hier je naam in', height=2)
    signupnameLabel.pack()
    signupfieldName = Entry(master=signupframe)
    signupfieldName.pack(padx=20, pady=20)

    signupstadLabel = Label(master=signupframe, text='Vul hier je stad in:', height=2)
    signupstadLabel.pack()
    signupfieldStad = Entry(master=signupframe)
    signupfieldStad.pack(padx=20, pady=20)

    signupstadLabel = Label(master=signupframe, text='Vul hier de afkorting van je land in:', height=2)
    signupstadLabel.pack()
    signupfieldLand = Entry(master=signupframe)
    signupfieldLand.pack(padx=20, pady=20)
    signupbuttonframe = Button(master=signupframe, text="SIGN UP", command=checkexistendSignUp(signupfieldName))
    signupbuttonframe.pack(padx=20, pady=20)

    root.mainloop()

def toonHoofdFrame(userName):
    global root4
    root2.destory()
    root3.destroy()
    root4 = Tk()

    signinframe.pack_forget()
    signupframe.pack_forget()
    loginframe.pack_forget()
    hoofdframe.pack()

    hoofdframeToevoegenButton = Button(master=hoofdframe, text="Kleding toevoegen", command=addDelete("add", userName))
    hoofdframeToevoegenButton.pack(padx=20, pady=20)
    hoofdframeVerwijderenButton = Button(master=hoofdframe, text="Kleding verwijderen", command=addDelete("delete", userName))
    hoofdframeVerwijderenButton.pack(padx=20, pady=20)
    hoofdframeAutomatischButton = Button(master=hoofdframe, text="Setje automatisch genereren")
    hoofdframeAutomatischButton.pack(padx=20, pady=20)
    hoofdframeGegevensButton = Button(master=hoofdframe, text="Gegevens wijzigen")
    hoofdframeGegevensButton.pack(padx=20, pady=20)

    root.mainloop()

def checkexistendSignIn(userName):
    if checkIfExist(userName) == False:
        bericht = 'Deze username is niet in gebruik!!'
        showinfo(title='Username not found', message=bericht)
    else:
        toonHoofdFrame(userName)

def checkexistendSignUp(userName):
    if checkIfExist(userName) == True:
        bericht = 'Deze username is al in gebruik!'
        showinfo(title='Username already existend', message=bericht)
    else:
        toonHoofdFrame(userName)

def addDelete(conf):
    print(userName)
    # if conf == "add":
    #     addClothes(userName)
    # else:
    #     deleteClothes(userName)

root = Tk()

loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)

signinframe = Frame(master=root)
signinframe.pack(fill="both", expand=True)

signupframe = Frame(master=root)
signupframe.pack(fill="both", expand=True)

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)

toonLoginFrame()
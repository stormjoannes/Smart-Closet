from tkinter import *
import json
from tkinter.messagebox import showinfo
from Main import *


def Signup():  # This is the signup definition,
    rootA.destroy()
    global nameE
    global roots

    roots = Tk()  # This creates the window, just a blank one.
    roots.title('Signup')  # This renames the title of said window to 'signup'
    intruction = Label(roots,
                       text='Sign in please\n')  # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0,
                    sticky=E)  # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    nameL = Label(roots, text='New Username: ')  # This just does the same as above, instead with the text new username.
    nameL.grid(row=1, column=0,
               sticky=W)  # Same thing as the instruction var just on different rows. :) Tkinter is like that.

    nameE = Entry(roots)  # This now puts a text box waiting for input.
    nameE.grid(row=1, column=1)  # You know what this does now :D

    signUpStadField = Label(roots, text='City name: ')  # This just does the same as above, instead with the text new username.
    signUpStadField.grid(row=2, column=0,
               sticky=W)  # Same thing as the instruction var just on different rows. :) Tkinter is like that.

    signUpStadEntry = Entry(roots)  # This now puts a text box waiting for input.
    signUpStadEntry.grid(row=2, column=1)  # You know what this does now :D

    signUpLandField = Label(roots, text='The abbreviation of your country: ')  # This just does the same as above, instead with the text new username.
    signUpLandField.grid(row=3, column=0,
               sticky=W)  # Same thing as the instruction var just on different rows. :) Tkinter is like that.

    signUpLandEntry = Entry(roots)  # This now puts a text box waiting for input.
    signUpLandEntry.grid(row=3, column=1)  # You know what this does now :D

    signupButton = Button(roots, text='Signup',
                          command=FSSignup)  # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)

    backLogin = Button(roots, text='Login', fg='Blue',
                    command=FSSignup)  # This makes the deluser button. blah go to the deluser def.
    backLogin.grid(columnspan=2, sticky=W)
    roots.mainloop()  # This just makes the window keep open, we will destroy it soon


def FSSignup():
    roots.destroy()  # This will destroy the signup window. :)
    Login()  # This will move us onto the login definition :D


def Login():
    global nameEL
    global rootA

    rootA = Tk()  # This now makes a new window.
    rootA.title('Login')  # This makes the window title 'login'

    intruction = Label(rootA, text='Please Login\n')  # More labels to tell us what they do
    intruction.grid(sticky=E)  # Blahdy Blah

    nameL = Label(rootA, text='Username: ')  # More labels
    nameL.grid(row=1, sticky=W)

    nameEL = Entry(rootA)  # The entry input
    nameEL.grid(row=1, column=1)

    loginB = Button(rootA, text='Login',
                    command=toHomeScreen)  # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text='Sign in', fg='Blue',
                    command=Signup)  # This makes the deluser button. blah go to the deluser def.
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()


def toHomeScreen():
    if checkIfExist(str(nameEL)) == True:
        print("homescreen")
    else:
        bericht = f'Username not existend, try it it again!'
        showinfo(title='UserName error', message=bericht)

def toLogin():
    if checkIfExist(str(nameE)) == False:
        roots.destroy()
        toLogin()
    else:
        bericht = 'Username already existend, try it it again!'
        showinfo(title='UserName error', message=bericht)

Login()
from tkinter import *
from tkinter.messagebox import showinfo
from Main import *
import json
from AddOrDelete import *
from KledingkastBekijken import *


def Signup():  # This is the signup definition,
    rootA.destroy()
    global nameE
    global roots
    global signUpStadEntry
    global signUpLandEntry

    roots = Tk()
    roots.title('Signup')
    intruction = Label(roots,
                       text='Sign aub\n')
    intruction.grid(row=0, column=0,
                    sticky=E)

    nameL = Label(roots, text='Nieuwe naam: ')
    nameL.grid(row=1, column=0,
               sticky=W)

    nameE = Entry(roots)
    nameE.grid(row=1, column=1)

    signUpStadField = Label(roots, text='Stad naam: ')
    signUpStadField.grid(row=2, column=0,
               sticky=W)

    signUpStadEntry = Entry(roots)
    signUpStadEntry.grid(row=2, column=1)

    signUpLandField = Label(roots, text='De afkorting van je land: ')
    signUpLandField.grid(row=3, column=0,
               sticky=W)

    signUpLandEntry = Entry(roots)
    signUpLandEntry.grid(row=3, column=1)

    signupButton = Button(roots, text='Signup',
                          command=toLogin)
    signupButton.grid(columnspan=2, sticky=W)

    backLogin = Button(roots, text='Login', fg='Blue',
                    command=FSSignup)
    backLogin.grid(columnspan=2, sticky=W)
    roots.mainloop()


def FSSignup():
    roots.destroy()
    Login()


def Login():
    global nameEL
    global rootA

    rootA = Tk()
    rootA.title('Login')

    intruction = Label(rootA, text='Log aub in\n')
    intruction.grid(sticky=E)

    nameL = Label(rootA, text='Username: ')
    nameL.grid(row=1, sticky=W)

    nameEL = Entry(rootA)
    nameEL.grid(row=1, column=1)

    loginB = Button(rootA, text='Login',
                    command=toHomeScreen)
    loginB.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text='Sign in', fg='Blue',
                    command=Signup)
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()

# def toHomescreen():
#     rootA.destroy()
#     Homescreen()

def Homescreen():
    global rootHm

    rootHm = Tk()
    rootHm.title('Home')

    homescreenLabelTitle = Label(rootHm, text='Wat wil je doen: ')
    homescreenLabelTitle.grid(row=1, sticky=W)

    homescreenAddButton= Button(rootHm, text='voeg kleding toe ', command=AddScreen)
    homescreenAddButton.grid(row=2)

    homescreenDeleteButton = Button(rootHm, text='Verwijder kleding ', command=DeleteScreen)
    homescreenDeleteButton.grid(row=3)

    homescreenSettingsButton = Button(rootHm, text='Verander persoons gegevens')
    homescreenSettingsButton.grid(row=4)

    homescreenAutomaticGenButton = Button(rootHm, fg='blue', text='Automatisch genereren van je kleding setje ')
    homescreenAutomaticGenButton.grid(row=5)

    rootHm.mainloop()


def AddScreen():
    rootHm.destroy()
    global rootAdd
    global addscreenNameEntry
    global addscreenLongShortEntry
    global addscreenOpportunityEntry
    global addscreenColorEntry
    global addscreenBrandEntry
    global addscreenCategoryEntry

    rootAdd = Tk()
    rootAdd.title('ADD')

    addscreenTitle = Label(rootAdd, text='Vul de parameters van je kledingstuk in: ')
    addscreenTitle.grid(row=0, sticky=W)

    addscreenNameLabel = Label(rootAdd, text='Naam: ')
    addscreenNameLabel.grid(row=1, column=0,  sticky=W)

    addscreenNameEntry = Entry(rootAdd)
    addscreenNameEntry.grid(row=1, column=1)

    addscreenLongShortLabel = Label(rootAdd, text='lange/korte broekspijpen/mouwen: ')
    addscreenLongShortLabel.grid(row=2, column=0,  sticky=W)

    addscreenLongShortEntry = Entry(rootAdd)
    addscreenLongShortEntry.grid(row=2, column=1)

    addscreenOpportunityLabel = Label(rootAdd, text='Gelegenheid(ddagelijks leven, sport of feestje): ')
    addscreenOpportunityLabel.grid(row=3, column=0,  sticky=W)

    addscreenOpportunityEntry = Entry(rootAdd)
    addscreenOpportunityEntry.grid(row=3, column=1)

    addscreenColorLabel = Label(rootAdd, text='Kleur: ')
    addscreenColorLabel.grid(row=4, column=0,  sticky=W)

    addscreenColorEntry = Entry(rootAdd)
    addscreenColorEntry.grid(row=4, column=1)

    addscreenBrandLabel = Label(rootAdd, text='Merk: ')
    addscreenBrandLabel.grid(row=5, column=0,  sticky=W)

    addscreenBrandEntry = Entry(rootAdd)
    addscreenBrandEntry.grid(row=5, column=1)

    addscreenCategoryLabel = Label(rootAdd, text='Categorie: ')
    addscreenCategoryLabel.grid(row=6, column=0,  sticky=W)

    addscreenCategoryEntry = Entry(rootAdd)
    addscreenCategoryEntry.grid(row=6, column=1)

    addscreenADDButton = Button(rootAdd, text='Voeg kledingstuk toe!', command=toAddClothing)
    addscreenADDButton.grid(row=7)

def DeleteScreen():
    rootHm.destroy()
    global rootDelete
    global deletescreenNameEntry
    global deletescreenLongShortEntry
    global deletescreenOpportunityEntry
    global deletescreenColorEntry
    global deletescreenBrandEntry
    global deletescreenCategoryEntry

    rootDelete = Tk()
    rootDelete.title('DELETE')

    deletescreenTitle = Label(rootDelete, text='Vul de parameters van je kledingstuk in: ')
    deletescreenTitle.grid(row=0, sticky=W)

    deletescreenNameLabel = Label(rootDelete, text='Naam: ')
    deletescreenNameLabel.grid(row=1, column=0,  sticky=W)

    deletescreenNameEntry = Entry(rootDelete)
    deletescreenNameEntry.grid(row=1, column=1)

    deletescreenLongShortLabel = Label(rootDelete, text='lange/korte broekspijpen/mouwen: ')
    deletescreenLongShortLabel.grid(row=2, column=0,  sticky=W)

    deletescreenLongShortEntry = Entry(rootDelete)
    deletescreenLongShortEntry.grid(row=2, column=1)

    deletescreenOpportunityLabel = Label(rootDelete, text='Gelegenheid(ddagelijks leven, sport of feestje): ')
    deletescreenOpportunityLabel.grid(row=3, column=0,  sticky=W)

    deletescreenOpportunityEntry = Entry(rootDelete)
    deletescreenOpportunityEntry.grid(row=3, column=1)

    deletescreenColorLabel = Label(rootDelete, text='Kleur: ')
    deletescreenColorLabel.grid(row=4, column=0,  sticky=W)

    deletescreenColorEntry = Entry(rootDelete)
    deletescreenColorEntry.grid(row=4, column=1)

    deletescreenBrandLabel = Label(rootDelete, text='Merk: ')
    deletescreenBrandLabel.grid(row=5, column=0,  sticky=W)

    deletescreenBrandEntry = Entry(rootDelete)
    deletescreenBrandEntry.grid(row=5, column=1)

    deletescreenCategoryLabel = Label(rootDelete, text='Categorie: ')
    deletescreenCategoryLabel.grid(row=6, column=0,  sticky=W)

    deletescreenCategoryEntry = Entry(rootDelete)
    deletescreenCategoryEntry.grid(row=6, column=1)

    deletescreenDELETEButton = Button(rootDelete, text='Verwijder kledingstuk!', command=toDeleteClothing)
    deletescreenDELETEButton.grid(row=7)

def changePersonalData():
    global rootCPD

    rootcpd = Tk()
    rootcpd.title('personal data')

    personaldataTitleLabel = Label(rootCPD, text='Waarop wil je filteren: ')
    personaldataTitleLabel.grid(row=0)

    personaldataFilterLabel = Label(rootCPD, text=f'{getAllPossibleFilters()}: ')
    personaldataFilterLabel.grid(row=1, column=0)

    personaldataFilterEntry = Entry(rootCPD)
    personaldataFilterEntry.grid(row=1, column=1)

def UitkiezenScreen():
    rootChoose = Tk()
    rootChoose.title('Choose')

def toHomeScreen():
    if checkIfExist(str(nameEL.get())) == True:
        global userName
        userName = str(nameEL.get())
        rootA.destroy()
        Homescreen()
    else:
        bericht = 'Username not existend, try it it again!'
        showinfo(title='UserName error', message=bericht)

def toLogin():
    if checkIfExist(str(nameE.get())) == False:
        configSignUp(str(nameE.get()), str(signUpStadEntry.get()), str(signUpLandEntry.get()))
        FSSignup()
    else:
        bericht = f'Username already existend, {nameE.get(), signUpStadEntry.get(), signUpLandEntry.get()} try it it again!'
        showinfo(title='UserName error', message=bericht)

def toAddClothing():
    addClothes(userName, str(addscreenNameEntry.get()), str(addscreenLongShortEntry.get()),
               str(addscreenOpportunityEntry.get()), str(addscreenColorEntry.get()), str(addscreenBrandEntry.get()),
               str(addscreenCategoryEntry.get()))
    rootAdd.destroy()
    Homescreen()

def toDeleteClothing():
    statusDelete = deleteClothes(userName, str(deletescreenNameEntry.get()), str(deletescreenLongShortEntry.get()),
               str(deletescreenOpportunityEntry.get()), str(deletescreenColorEntry.get()), str(deletescreenBrandEntry.get()),
               str(deletescreenCategoryEntry.get()))

    if statusDelete == False:
        bericht = f'kledingstuk {str(deletescreenNameEntry.get())} bestaat niet en kan dus ook niet verwijderd worden!'
        showinfo(title='Delete Error', message=bericht)

    rootDelete.destroy()
    Homescreen()

def toBekijken():
    bekijken(userName, )
# def toHomeScreenAdd():
#     rootAdd.destroy()
#     Homescreen()


Login()
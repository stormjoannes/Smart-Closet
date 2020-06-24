import json
#boven 22 is warm, onder 13 is koud
# try:
with open('../jsonFiles/Kledingkast.json', 'r') as BackupData:
    backupDataDrawBack = json.load(BackupData)
# except:
#     with open('../jsonFiles/BackupKledingkast.json', 'r') as BackupData:
#         backupDataDrawBack = json.load(BackupData)
#     with open("../jsonFiles/Kledingkast.json", 'w+') as f:
#         f.write(f"{backupDataDrawBack}")

from Code.Functions import *
from tkinter import ttk
import pathlib

def Signup():  # This is the signup definition,
    "'In deze functie maak ik het signup frame aan, hier kun je jezelf aanmelden'"
    rootA.destroy()
    global rootSignUp
    global Globroot

    rootSignUp = Tk()
    rootSignUp.title('Signup')
    Globroot = rootSignUp

    showMenuLoginSignup(rootSignUp)

    intruction = Label(rootSignUp, text='Sign aub\n', background="gray")
    intruction.grid(row=0, column=0)

    nameL = Label(rootSignUp, text='Nieuwe naam: ', background="gray")
    nameL.grid(row=1, column=0,
               sticky=W)

    nameE = Entry(rootSignUp)
    nameE.grid(row=1, column=1)

    signUpStadField = Label(rootSignUp, text='Stad naam: ', background="gray")
    signUpStadField.grid(row=2, column=0,
               sticky=W)

    signUpStadEntry = Entry(rootSignUp)
    signUpStadEntry.grid(row=2, column=1)

    signUpLandField = Label(rootSignUp, text='De afkorting van je land: ', background="gray")
    signUpLandField.grid(row=3, column=0,
               sticky=W)

    signUpLandEntry = Entry(rootSignUp)
    signUpLandEntry.grid(row=3, column=1)

    signupButton = Button(rootSignUp, text='Signup',
                          command=lambda:toLogin(nameE.get(), signUpStadEntry.get(), signUpLandEntry.get()))
    signupButton.grid(columnspan=2, sticky=W)

    backLogin = Button(rootSignUp, text='Login', fg='Blue',
                       command=toLogIn)
    backLogin.grid(columnspan=2, sticky=W)

    # intruction.pack(ipadx=10000)
    #
    # nameL = Label(rootSignUp, text='Nieuwe naam: ', background="gray")
    # nameL.pack(row=1, column=0,
    #            sticky=W)
    #
    # nameE = Entry(rootSignUp)
    # nameE.pack(row=1, column=1)
    #
    # signUpStadField = Label(rootSignUp, text='Stad naam: ', background="gray")
    # signUpStadField.pack(row=2, column=0,
    #            sticky=W)
    #
    # signUpStadEntry = Entry(rootSignUp)
    # signUpStadEntry.pack(row=2, column=1)
    #
    # signUpLandField = Label(rootSignUp, text='De afkorting van je land: ', background="gray")
    # signUpLandField.pack(row=3, column=0,
    #            sticky=W)
    #
    # signUpLandEntry = Entry(rootSignUp)
    # signUpLandEntry.pack(row=3, column=1)
    #
    # signupButton = Button(rootSignUp, text='Signup',
    #                       command=lambda:toLogin(nameE.get(), signUpStadEntry.get(), signUpLandEntry.get()))
    # signupButton.pack(columnspan=2, sticky=W)
    #
    # backLogin = Button(rootSignUp, text='Login', fg='Blue',
    #                    command=toLogIn)
    # backLogin.pack(columnspan=2, sticky=W)

    rootSignUp.mainloop()


def toLogIn():
    "'deze functie word vaker gebruikt om vanuit dat frame naar het login frame te gaan'"
    Globroot.destroy()
    Login()


def showMenuLoginSignup(root):
    "'Dit is een aparte functie om het dropdown menu voor de signup en de login te maken'"
    # root.geometry('1920x1080')
    root.configure(background='gray')

    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label='file', menu=subMenu)
    subMenu.add_command(label='exit', command=exit)


def Login():
    "'In deze functie kun je inloggen met je username'"
    global rootA
    global Globroot

    rootA = Tk()
    rootA.title('Login')

    Globroot = rootA

    showMenuLoginSignup(rootA)

    intruction = Label(rootA, text='Log in\n', background="gray", font=("Helvetica", 20))
    intruction.grid(column=1)

    nameL = Label(rootA, text='Username: ', background="gray")
    nameL.grid(row=1, sticky=W)

    nameEL = Entry(rootA)
    nameEL.grid(row=1, column=1)

    loginB = Button(rootA, text='Login',
                    command=lambda:toHomeScreen(nameEL.get()))
    loginB.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text='Sign in', fg='Blue',
                    command=Signup)
    rmuser.grid(columnspan=2, sticky=W)

    # intruction = Label(rootA, text='Log in\n', background="gray", font=("Helvetica", 50))
    # intruction.pack()
    #
    # nameL = Label(rootA, text='Username: ', background="gray", font=("Helvetica", 20))
    # nameL.pack()
    #
    # nameEL = Entry(rootA)
    # nameEL.pack()
    #
    # loginB = Button(rootA, text='Login',
    #                 command=lambda:toHomeScreen(nameEL.get()))
    # loginB.pack(side=BOTTOM)
    #
    # rmuser = Button(rootA, text='Sign in', fg='Blue',
    #                 command=Signup)
    # rmuser.pack()
    rootA.mainloop()

try:
    def Homescreen():
        "'deze functie geeft het hoofdmenu weer. hier kun je alle opties uitkiezen die er zijn.'"
        global rootHm
        global Globroot

        rootHm = Tk()
        rootHm.title('Home')
        Globroot = rootHm

        backupDump()
        showMenu(rootHm)
        refreshGedragen(userName)

        homescreenLabelTitle = Label(rootHm, text='Wat wil je doen: ', background="gray")
        homescreenLabelTitle.grid(row=1, sticky=W)

        homescreenAddButton= Button(rootHm, text='voeg kleding toe ', command=AddScreen)
        homescreenAddButton.grid(row=2)

        homescreenDeleteButton = Button(rootHm, text='Verwijder kleding ', command=DeleteScreen)
        homescreenDeleteButton.grid(row=3)

        homescreenSettingsButton = Button(rootHm, text='Kleding uitkiezen', command=UitkiezenScreen)
        homescreenSettingsButton.grid(row=4)

        homescreenAutomaticGenButton = Button(rootHm, fg='blue', text='Automatisch genereren van je kleding setje ', command=toGenScreen)
        homescreenAutomaticGenButton.grid(row=5)

        rootHm.mainloop()
except:
    bericht = "Er is iets mis gegaan, probeer het opnieuw!"
    showinfo(title='System error', message=bericht)
    Login()


def AddScreen():
    "'In deze functie word het frame aangemaakt om kleding toe te voegen aan je digitale kledingkast'"
    rootHm.destroy()
    global rootAdd
    global Globroot

    rootAdd = Tk()
    rootAdd.title('ADD')
    Globroot = rootAdd

    showMenu(rootAdd)
    inputParametersClothing(rootAdd)

    addscreenADDButton = Button(rootAdd, text='Voeg kledingstuk toe!', command=lambda:DeleteOrAdd(userName, str(screenNameEntry.get()), str(screenLongShortEntry.get()), str(screenOpportunityEntry.get()), str(screenColorEntry.get()), str(screenBrandEntry.get()), str(screenCategoryEntry.get()), "add"))
    addscreenADDButton.grid(row=7)

    rootAdd.mainloop()


def inputParametersClothing(root):
    "'Deze functie zorgt voor de input van de paramaters van de kleding. deze worden gebruikt om kleren te verwijderen en toe te voegen'"
    global screenNameEntry
    global screenLongShortEntry
    global screenOpportunityEntry
    global screenColorEntry
    global screenBrandEntry
    global screenCategoryEntry

    screenTitle = Label(root, text='Vul de parameters van je kledingstuk in: ', background="gray")
    screenTitle.grid(row=0, sticky=W)

    screenNameLabel = Label(root, text='Naam: ', background="gray")
    screenNameLabel.grid(row=1, column=0,  sticky=W)

    screenNameEntry = Entry(root)
    screenNameEntry.grid(row=1, column=1)

    screenLongShortLabel = Label(root, text='lange/korte broekspijpen/mouwen: ', background="gray")
    screenLongShortLabel.grid(row=2, column=0,  sticky=W)

    screenLongShortEntry = Entry(root)
    screenLongShortEntry.grid(row=2, column=1)

    screenOpportunityLabel = Label(root, text='Gelegenheid(ddagelijks leven, sport of feestje): ', background="gray")
    screenOpportunityLabel.grid(row=3, column=0,  sticky=W)

    screenOpportunityEntry = Entry(root)
    screenOpportunityEntry.grid(row=3, column=1)

    screenColorLabel = Label(root, text='Kleur: ', background="gray")
    screenColorLabel.grid(row=4, column=0,  sticky=W)

    screenColorEntry = Entry(root)
    screenColorEntry.grid(row=4, column=1)

    screenBrandLabel = Label(root, text='Merk: ', background="gray")
    screenBrandLabel.grid(row=5, column=0,  sticky=W)

    screenBrandEntry = Entry(root)
    screenBrandEntry.grid(row=5, column=1)

    screenCategoryLabel = Label(root, text='Categorie: ', background="gray")
    screenCategoryLabel.grid(row=6, column=0,  sticky=W)

    screenCategoryEntry = Entry(root)
    screenCategoryEntry.grid(row=6, column=1)

    addscreenBackButton = Button(root, text='Back', command=toHub)
    addscreenBackButton.grid(row=7, sticky=W)


def DeleteScreen():
    "'In deze functie word het frame aangemaakt om kleding te verwijderen van je digitale kledingkast'"
    with open('../jsonFiles/Kledingkast.json', 'r') as Clothes:
        CheckforClothes = json.load(Clothes)

    if len(CheckforClothes[userName]) > 2:
        rootHm.destroy()
        global rootDelete
        global Globroot

        rootDelete = Tk()
        rootDelete.title('DELETE')
        Globroot = rootDelete

        showMenu(rootDelete)

        inputParametersClothing(rootDelete)

        deletescreenDELETEButton = Button(rootDelete, text='Verwijder kledingstuk!', command=lambda:DeleteOrAdd(userName, str(screenNameEntry.get()), str(screenLongShortEntry.get()), str(screenOpportunityEntry.get()), str(screenColorEntry.get()), str(screenBrandEntry.get()), str(screenCategoryEntry.get()), "delete"))
        deletescreenDELETEButton.grid(row=7)

        rootDelete.mainloop()
    else:
        bericht = "Helaas hebben we geen kledingstukken aangetroffen om te verwijderen."
        showinfo(title='Clothing error', message=bericht)


def DeleteOrAdd(userName, name, LongShort, opportunity, color, brand, category, switch):
    if switch == "add":
        addClothes(userName, name, LongShort, opportunity, color, brand, category)
    else:
        deleteClothes(userName, name, LongShort, opportunity, color, brand, category)
    toHub()


def changePersonalData():
    "'Deze functie word gebruikt in het dropdown menu. Hier kun je persoonlijke gegevens aanpassen.'"
    global rootCPD

    rootCPD = Tk()
    rootCPD.title('personal data')

    showMenu(rootCPD)

    with open('../jsonFiles/Kledingkast.json', 'r+') as docPersonalData:
        personalData = json.load(docPersonalData)

    personaldataUserNameLabel = Label(rootCPD, text='Username: ', background="gray")
    personaldataUserNameLabel.grid(row=0, column=0,  sticky=W)

    personaldataUserNameEntry = Entry(rootCPD)
    personaldataUserNameEntry.insert(0, userName)
    personaldataUserNameEntry.grid(row=0, column=1)

    personaldataBetweenWearLabel = Label(rootCPD, text='Tijd tussen het dragen van kleding: ', background="gray")
    personaldataBetweenWearLabel.grid(row=1, column=0,  sticky=W)

    personaldataBetweenWearEntry = Entry(rootCPD)
    personaldataBetweenWearEntry.insert(0, personalData[userName][0]["gegevens"][1]["overigeGeg"]["betweenWear"])
    personaldataBetweenWearEntry.grid(row=1, column=1)


    personaldataCityLabel = Label(rootCPD, text='Stad: ', background="gray")
    personaldataCityLabel.grid(row=2, column=0,  sticky=W)

    personaldataCityEntry = Entry(rootCPD)
    personaldataCityEntry.insert(0, personalData[userName][0]["gegevens"][0]["locatie"]["stad"])
    personaldataCityEntry.grid(row=2, column=1)


    personaldataLandLabel = Label(rootCPD, text='Afkorting van Land: ', background="gray")
    personaldataLandLabel.grid(row=3, column=0,  sticky=W)

    personaldataLandEntry = Entry(rootCPD)
    personaldataLandEntry.insert(0, personalData[userName][0]["gegevens"][0]["locatie"]["land"])
    personaldataLandEntry.grid(row=3, column=1)

    personaldataSubmitChanges = Button(rootCPD, text='Toepassen', command=lambda:commitPersonalData(personaldataBetweenWearEntry.get(), personaldataCityEntry.get(), personaldataLandEntry.get(), personaldataUserNameEntry.get()))
    personaldataSubmitChanges.grid(sticky=E)

    rootCPD.mainloop()


def deleteAccountCheck():
    "'Deze functie zorgt er voor dat je je account kan verwijderen'"
    global rootDeleteAccount
    rootDeleteAccount = Tk()
    rootDeleteAccount.title('Account delete')

    delAccountTitle = Label(rootDeleteAccount, text='Weet je zeker dat je je account wilt verwijderen: ', background="gray")
    delAccountTitle.grid(row=1, column=0,  sticky=W)

    delAccountYesButton = Button(rootDeleteAccount, text='Ja', command=lambda:deleteAccount(Login, userName, Globroot, rootDeleteAccount))
    delAccountYesButton.grid(row=3, sticky=W)

    delAccountNeeButton = Button(rootDeleteAccount, text='Nee', command=toHub)
    delAccountNeeButton.grid(row=3, sticky=E)

    rootDeleteAccount.mainloop()


def toDeleteAccount(Login, userName, Globroot, rootDeleteAccount):
    deleteAccount(userName)
    Globroot.destroy()
    rootDeleteAccount.destroy()
    Login()


def UitkiezenScreen():
    "'Deze functie opent je kledingkast zodat je gewoon in je kledingkast kan kijken, filters kunnen ook toegepast worden.'"
    with open('../jsonFiles/Kledingkast.json', 'r') as Clothes:
        CheckforClothes = json.load(Clothes)

    if len(CheckforClothes[userName]) > 2:
        rootHm.destroy()
        global Globroot
        global rootChoose

        # global chooseFilterCombobox

        rootChoose = Tk()
        rootChoose.title('Choose')
        Globroot = rootChoose

        showMenu(rootChoose)

        chooseTitleLabel = Label(rootChoose, text='Al je kleren: ', background="gray")
        chooseTitleLabel.grid(row=2)

        chooseEmptySpaceLabel = Label(rootChoose, text='', background="gray")
        chooseEmptySpaceLabel.grid(row=3)

        allClothes(rootChoose, userName)

        possibleFilters = getAllPossibleFilters(userName)

        chooseFilterLabel = Label(rootChoose, text='Filter: ', background="gray")
        chooseFilterLabel.grid(row=0, sticky=W)

        chooseFilterCombobox = ttk.Combobox(rootChoose, value=possibleFilters)
        chooseFilterCombobox.insert(0, 'None')
        chooseFilterCombobox.grid(row=0, column=0)

        chooseFilterButton = Button(rootChoose, text='SUBMIT', command=lambda:forDetailFilter(chooseFilterCombobox.get(), rootChoose))
        chooseFilterButton.grid(row=0, column=1)

        chooseDeleteFilterButton = Button(rootChoose, text='Delete Filter', command=lambda:toDeleteFilter(rootChoose))
        chooseDeleteFilterButton.grid(row=100, sticky=E)

        chooseBackButton = Button(rootChoose, text='Back', command=toHub)
        chooseBackButton.grid(row=100, sticky=W)
    else:
        bericht = "Helaas hebben we geen kledingstukken aangetroffen om uit te kiezen."
        showinfo(title='Clothing error', message=bericht)


def toGenScreen():
    rootHm.destroy()
    setGenScreen()


def setGenScreen():
    "'In deze functie word het frame aangemaakt voor het automatisch uitkiezen van een kledingsetje voor jou.'"
    global rootGen
    global Globroot

    rootGen = Tk()
    rootGen.title('Generator')
    Globroot = rootGen

    showMenu(rootGen)

    GenTitleLabel = Label(rootGen, text='Voor welke gelegenheid wil je een kledingstuk uitkiezen: ', background="gray")
    GenTitleLabel.grid(row=0)

    GenSpaceLabel = Label(rootGen, text='', background="gray")
    GenSpaceLabel.grid(row=1)

    genDagelijksButton = Button(rootGen, text='Dagelijks leven', command=lambda:WeatherForPickClothes('dagelijks', rootGen, userName, Homescreen, showMenu, setGenScreen))
    genDagelijksButton.grid(row=2, sticky=W)

    genSportutton = Button(rootGen, text='Sport', command=lambda:WeatherForPickClothes('sport', rootGen, userName, Homescreen, showMenu, setGenScreen))
    genSportutton.grid(row=2, column=0)

    genFeestButton = Button(rootGen, text='Feest', command=lambda:WeatherForPickClothes('feest', rootGen, userName, Homescreen, showMenu, setGenScreen))
    genFeestButton.grid(row=2, column=1)

    GenSpaceLabel = Label(rootGen, text='', background="gray")
    GenSpaceLabel.grid(row=3)

    genBackButton = Button(rootGen, text='Back', command=toHub)
    genBackButton.grid(row=5, sticky=W)

    rootGen.mainloop()


def showMenu(root):
    "'Deze functie word in bijna alle frames aangeroepen om zo het drop down menu overal het zelfde weer te geven.'"
    global toDestroyRoot

    # root.geometry('1920x1080')
    root.configure(background='gray')

    toDestroyRoot = root
    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label='settings', menu=subMenu)
    subMenu.add_command(label='personal data', command=changePersonalData)
    subMenu.add_command(label='delete account', command=deleteAccountCheck)
    subMenu.add_separator()
    subMenu.add_command(label='homescreen', command=toHub)
    subMenu.add_command(label='Log out', command=toLogIn)
    subMenu.add_command(label='exit', command=exit)


def toHub():
    "'deze functie zorgt voor het destroyen van het vorige frame en stuurt je door naar het homescreen'"
    toDestroyRoot.destroy()
    Homescreen()


def exit():
    "'deze functie zorgt ervoor dat je het programma  afsluit door het enige frame dat openstaat te destroyen.'"
    Globroot.destroy()


def commitPersonalData(BetweenWear, City, Land, ChangeName):
    "'Deze functie zorgt ervoor dat de ingevulde data die je wilt veranderen van jouw profiel opgeslagen word.'"
    global userName
    global Globroot
    changedUserName = str(gegWijzigen(userName, BetweenWear, City, Land, ChangeName))
    userName = changedUserName
    rootCPD.destroy()
    Globroot=rootHm


def toHomeScreen(name):
    "'Deze functie word gebruikt bij de login om te checken of je door kan worden gestuurde naar het hoofdscherm'"
    if checkIfExist(name) == True:
        global userName
        userName = name
        rootA.destroy()
        Homescreen()
    else:
        bericht = 'Username not existend, try it it again!'
        showinfo(title='UserName error', message=bericht)


def toLogin(signUpName, signUpStad, signUpLand):
    "''hier check je of de ingevulde waardes om je aan te melden kloppen en correct kunnen worden verwerkt."
    if len(signUpStad) == 0 or len(signUpLand) == 0 or len(signUpName) == 0:
        emptyInput = ''
        if len(signUpName) == 0:
            emptyInput += "naam"
        if len(signUpStad) == 0:
            if len(emptyInput) > 0:
                emptyInput += ', stad'
            else:
                emptyInput += 'stad'
        if len(signUpLand) == 0:
            if len(emptyInput) > 0:
                emptyInput += ', land'
            else:
                emptyInput += 'land'
        bericht = f'Vul je {emptyInput} in!'
        showinfo(title='Field error', message=bericht)
    else:
        try:
            setValuesWeer(signUpStad, signUpLand)
            if checkIfExist(signUpName) == False:
                configSignUp(signUpName, signUpStad, signUpLand)
                rootSignUp.destroy()
                Login()
            else:
                bericht = f'Username {signUpName} already existend, try another name!'
                showinfo(title='UserName error', message=bericht)
        except:
            bericht = f'De ingevulde stad of het ingevulde land is niet herkenbaar!'
            showinfo(title='Field error', message=bericht)

file = pathlib.Path("../jsonFiles/Kledingkast.json")
if file.exists():
    Login()
else:
    with open("../jsonFiles/Kledingkast.json", 'w+') as f:
        f.write('{}')
    with open("../jsonFiles/BackupKledingkast.json", 'w+') as f:
        f.write('{}')
    Login()

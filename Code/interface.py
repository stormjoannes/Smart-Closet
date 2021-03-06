from Code.Functions import *
from Code.KledingkastBekijken import *
from tkinter import ttk
import pathlib

def Signup():
    """
    In deze functie maak ik het signup frame aan, hier kun je jezelf aanmelden.
    """

    rootLogin.destroy()
    global rootSignUp
    global Globroot

    rootSignUp = Tk()
    rootSignUp.title('Signup')
    Globroot = rootSignUp
    rootSignUp.geometry("300x175")

    showMenuLoginSignup(rootSignUp)

    intruction = Label(rootSignUp, text='Sign aub\n', background="#c6def1", font=("Helvetica", 15))
    intruction.place(x=100, y=0)

    signUpEntryNameLabel = Label(rootSignUp, text='Nieuwe naam: ', background="#c6def1", font=("Helvetica", 10))
    signUpEntryNameLabel.place(x=5, y=30)

    signUpNameEntry = Entry(rootSignUp)
    signUpNameEntry.place(x=155, y=30)

    signUpStadField = Label(rootSignUp, text='Stad naam: ', background="#c6def1", font=("Helvetica", 10))
    signUpStadField.place(x=5, y=60)

    signUpStadEntry = Entry(rootSignUp)
    signUpStadEntry.place(x=155, y=60)

    signUpLandField = Label(rootSignUp, text='De afkorting van je land: ', background="#c6def1", font=("Helvetica", 10))
    signUpLandField.place(x=5, y=90)

    signUpLandEntry = Entry(rootSignUp)
    signUpLandEntry.place(x=155, y=90)

    signupButton = Button(rootSignUp, text='Signup', fg='Blue', command=lambda:toLogin(signUpNameEntry.get(),
                                               signUpStadEntry.get(), signUpLandEntry.get()), width="12", height="1")
    signupButton.place(x=172, y=120)

    backLogin = Button(rootSignUp, text='Login',width="12", height="1", command=toLogIn)
    backLogin.place(x=5, y=120)

    rootSignUp.mainloop()


def toLogIn():
    """
    deze functie word vaker gebruikt om vanuit dat frame naar het login frame te gaan.
    """

    Globroot.destroy()
    Login()


def showMenuLoginSignup(root):
    """Dit is een aparte functie om het dropdown menu voor de signup en de login te maken
    """

    root.configure(background="#c6def1")
    root.iconbitmap('../overige_bestanden/kledingkastIco.ico')

    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    subMenu.config(fg="#555b6e")
    menu.add_cascade(label='Settings', menu=subMenu)
    subMenu.add_command(label='Exit', command=exitProg)


def Login():
    """
    In deze functie kun je inloggen met je username
    """

    global rootLogin
    global Globroot

    rootLogin = Tk()
    rootLogin.title('Login')
    rootLogin.geometry("225x175")


    Globroot = rootLogin

    showMenuLoginSignup(rootLogin)

    LoginTitleLabel = Label(rootLogin, text='Log in\n', background="#c6def1", font=("Helvetica", 20))
    LoginTitleLabel.place(x=75, y=0)

    LoginEntryNameLabel = Label(rootLogin, text='Username: ', background="#c6def1")
    LoginEntryNameLabel.place(x=2, y=58)

    LoginUserNameEntry = Entry(rootLogin)
    LoginUserNameEntry.place(x=70, y=60)

    loginB = Button(rootLogin, text='Login', fg='Blue', command=lambda:toHomeScreen(LoginUserNameEntry.get()),
                    width="7", height="2")
    loginB.place(x=70, y=100)

    rmuser = Button(rootLogin, text='Sign in', command=Signup, width="7", height="2")
    rmuser.place(x=140, y=100)

    rootLogin.mainloop()

try:
    def Homescreen():
        """
        deze functie geeft het hoofdmenu weer. hier kun je alle opties uitkiezen die er zijn.
        """

        global rootHm
        global Globroot

        rootHm = Tk()
        rootHm.title('Home')
        Globroot = rootHm
        rootHm.geometry("400x250")

        backupDump()
        showMenu(rootHm)
        testDatabase()
        refreshGedragen(userName)

        homescreenLabelTitle = Label(rootHm, text='Wat wil je doen: ', background="#c6def1", font=("Helvetica", 12))
        homescreenLabelTitle.place(x=0, y=0)

        homescreenAddButton= Button(rootHm, text='voeg kleding toe ', command=AddScreen, width=20, height="2")
        homescreenAddButton.place(x=125, y=25)

        homescreenDeleteButton = Button(rootHm, text='Verwijder kleding ', command=DeleteScreen, width=20, height="2")
        homescreenDeleteButton.place(x=125, y=70)

        homescreenSettingsButton = Button(rootHm, text='Kleding uitkiezen', command=UitkiezenScreen,
                                          width=30, height="2")
        homescreenSettingsButton.place(x=90, y=115)

        homescreenAutomaticGenButton = Button(rootHm, fg='blue', text='Automatisch genereren van je kleding setje ',
                                              command=toGenScreen, width=40, height="2")
        homescreenAutomaticGenButton.place(x=50, y=160)

        rootHm.mainloop()
except:
    bericht = "Er is iets mis gegaan, probeer het opnieuw!"
    showinfo(title='System error', message=bericht)
    Login()


def AddScreen():
    """
    In deze functie word het frame aangemaakt om kleding toe te voegen aan je digitale kledingkast
    """

    rootHm.destroy()
    global rootAdd
    global Globroot

    rootAdd = Tk()
    rootAdd.title('ADD')
    Globroot = rootAdd
    rootAdd.geometry('400x225')

    showMenu(rootAdd)
    inputParametersClothing(rootAdd)

    addscreenADDButton = Button(rootAdd, text='Voeg kledingstuk toe!', command=lambda:DeleteOrAdd(userName, str(screenNameEntry.get()),
                                        str(screenLongShortEntry.get()), str(screenOpportunityEntry.get()), str(screenColorEntry.get()),
                                        str(screenBrandEntry.get()), str(screenCategoryEntry.get()), "add"))
    addscreenADDButton.grid(row=7)

    rootAdd.mainloop()


def inputParametersClothing(root):
    """
    Deze functie zorgt voor de input van de paramaters van de kleding.
    deze worden gebruikt om kleren te verwijderen en toe te voegen
    """

    global screenNameEntry
    global screenLongShortEntry
    global screenOpportunityEntry
    global screenColorEntry
    global screenBrandEntry
    global screenCategoryEntry

    screenTitle = Label(root, text='Vul de parameters van je kledingstuk in: ', background="#c6def1")
    screenTitle.grid(row=0, sticky=W)

    screenNameLabel = Label(root, text='Naam: ', background="#c6def1")
    screenNameLabel.grid(row=1, column=0,  sticky=W)

    screenNameEntry = Entry(root)
    screenNameEntry.grid(row=1, column=1)

    screenLongShortLabel = Label(root, text='lange/korte broekspijpen/mouwen: ', background="#c6def1")
    screenLongShortLabel.grid(row=2, column=0,  sticky=W)

    screenLongShortEntry = Entry(root)
    screenLongShortEntry.grid(row=2, column=1)

    screenOpportunityLabel = Label(root, text='Gelegenheid(dagelijks leven, sport of feestje): ', background="#c6def1")
    screenOpportunityLabel.grid(row=3, column=0,  sticky=W)

    screenOpportunityEntry = Entry(root)
    screenOpportunityEntry.grid(row=3, column=1)

    screenColorLabel = Label(root, text='Kleur: ', background="#c6def1")
    screenColorLabel.grid(row=4, column=0,  sticky=W)

    screenColorEntry = Entry(root)
    screenColorEntry.grid(row=4, column=1)

    screenBrandLabel = Label(root, text='Merk: ', background="#c6def1")
    screenBrandLabel.grid(row=5, column=0,  sticky=W)

    screenBrandEntry = Entry(root)
    screenBrandEntry.grid(row=5, column=1)

    screenCategoryLabel = Label(root, text='Categorie: ', background="#c6def1")
    screenCategoryLabel.grid(row=6, column=0,  sticky=W)

    screenCategoryEntry = Entry(root)
    screenCategoryEntry.grid(row=6, column=1)

    addscreenBackButton = Button(root, text='Back', command=toHub)
    addscreenBackButton.grid(row=7, sticky=W)


def DeleteScreen():
    """
    In deze functie word het frame aangemaakt om kleding te verwijderen van je digitale kledingkast
    """

    with open('../jsonFiles/Kledingkast.json', 'r') as Clothes:
        CheckforClothes = json.load(Clothes)

    if len(CheckforClothes[userName]) > 2:
        rootHm.destroy()
        global rootDelete
        global Globroot

        rootDelete = Tk()
        rootDelete.title('DELETE')
        Globroot = rootDelete
        rootDelete.geometry('400x225')

        showMenu(rootDelete)

        inputParametersClothing(rootDelete)

        deletescreenDELETEButton = Button(rootDelete, text='Verwijder kledingstuk!', command=lambda:DeleteOrAdd(userName,
                                                    str(screenNameEntry.get()), str(screenLongShortEntry.get()), str(screenOpportunityEntry.get()),
                                                    str(screenColorEntry.get()), str(screenBrandEntry.get()), str(screenCategoryEntry.get()), "delete"))
        deletescreenDELETEButton.grid(row=7)

        rootDelete.mainloop()
    else:
        bericht = "Helaas hebben we geen kledingstukken aangetroffen om te verwijderen."
        showinfo(title='Clothing error', message=bericht)


def DeleteOrAdd(userName, name, LongShort, opportunity, color, brand, category, switch):
    """
    Hier word er gekeken of ik een kledingstuk wil toevoegen of verwijderen.
    Zo word de juiste functie aangeroepen.
    """

    if switch == "add":
        addClothes(userName, name, LongShort, opportunity, color, brand, category)
    else:
        deleteClothes(userName, name, LongShort, opportunity, color, brand, category)
    toHub()


def changePersonalData():
    """
    Deze functie word gebruikt in het dropdown menu. Hier kun je persoonlijke gegevens aanpassen.
    """

    global rootCPD

    rootCPD = Tk()
    rootCPD.title('personal data')

    showMenu(rootCPD)

    with open('../jsonFiles/Kledingkast.json', 'r+') as docPersonalData:
        personalData = json.load(docPersonalData)

    personaldataUserNameLabel = Label(rootCPD, text='Username: ', background="#c6def1")
    personaldataUserNameLabel.grid(row=0, column=0,  sticky=W)

    personaldataUserNameEntry = Entry(rootCPD)
    personaldataUserNameEntry.insert(0, userName)
    personaldataUserNameEntry.grid(row=0, column=1)

    personaldataBetweenWearLabel = Label(rootCPD, text='Tijd tussen het dragen van kleding: ', background="#c6def1")
    personaldataBetweenWearLabel.grid(row=1, column=0,  sticky=W)

    personaldataBetweenWearEntry = Entry(rootCPD)
    personaldataBetweenWearEntry.insert(0, personalData[userName][0]["gegevens"][1]["overigeGeg"]["betweenWear"])
    personaldataBetweenWearEntry.grid(row=1, column=1)


    personaldataCityLabel = Label(rootCPD, text='Stad: ', background="#c6def1")
    personaldataCityLabel.grid(row=2, column=0,  sticky=W)

    personaldataCityEntry = Entry(rootCPD)
    personaldataCityEntry.insert(0, personalData[userName][0]["gegevens"][0]["locatie"]["stad"])
    personaldataCityEntry.grid(row=2, column=1)


    personaldataLandLabel = Label(rootCPD, text='Afkorting van Land: ', background="#c6def1")
    personaldataLandLabel.grid(row=3, column=0,  sticky=W)

    personaldataLandEntry = Entry(rootCPD)
    personaldataLandEntry.insert(0, personalData[userName][0]["gegevens"][0]["locatie"]["land"])
    personaldataLandEntry.grid(row=3, column=1)

    personaldataSubmitChanges = Button(rootCPD, text='Toepassen', command=lambda:commitPersonalData(personaldataBetweenWearEntry.get(),
                                            personaldataCityEntry.get(), personaldataLandEntry.get(), personaldataUserNameEntry.get()))
    personaldataSubmitChanges.grid(sticky=E)

    rootCPD.mainloop()


def deleteAccountCheck():
    """
    Deze functie zorgt er voor dat je je account kan verwijderen
    """

    global rootDeleteAccount
    rootDeleteAccount = Tk()
    rootDeleteAccount.title('Account delete')

    delAccountTitle = Label(rootDeleteAccount, text='Weet je zeker dat je je account wilt verwijderen: ', background="#c6def1")
    delAccountTitle.grid(row=1, column=0,  sticky=W)

    delAccountYesButton = Button(rootDeleteAccount, text='Ja', fg='RED', command=lambda:deleteAccount(Login, userName, Globroot, rootDeleteAccount))
    delAccountYesButton.grid(row=3, sticky=W, ipadx=51)

    delAccountNeeButton = Button(rootDeleteAccount, text='Nee', fg='BLUE', command=DeleteRoot)
    delAccountNeeButton.grid(row=3, sticky=E, ipadx=51)

    rootDeleteAccount.mainloop()

def DeleteRoot():
    """
    Deze functie gebruik ik om een huidige root alleen te destroyen
    """

    rootDeleteAccount.destroy()


def toDeleteAccount(Login, userName, Globroot, rootDeleteAccount):
    """
    Via deze functie ga ik naar mijn functie om mijn account te deleten en zorg ik dat overige roots gedestroyed worden.
    """

    deleteAccount(userName)
    Globroot.destroy()
    rootDeleteAccount.destroy()
    Login()


def UitkiezenScreen():
    """
    Deze functie opent je kledingkast zodat je gewoon in je kledingkast kan kijken, filters kunnen ook toegepast worden.
    """

    with open('../jsonFiles/Kledingkast.json', 'r') as Clothes:
        CheckforClothes = json.load(Clothes)

    if len(CheckforClothes[userName]) > 2:
        rootHm.destroy()
        global Globroot
        global rootChoose

        rootChoose = Tk()
        rootChoose.title('Choose')
        Globroot = rootChoose

        showMenu(rootChoose)

        chooseEmptySpaceLabel = Label(rootChoose, text='', background="#c6def1")
        chooseEmptySpaceLabel.grid(row=3)

        allClothes(rootChoose, userName)

        possibleFilters = getAllPossibleFilters(userName)

        chooseFilterLabel = Label(rootChoose, text='Filter: ', background="#c6def1")
        chooseFilterLabel.grid(row=0, sticky=W)

        chooseFilterCombobox = ttk.Combobox(rootChoose, value=possibleFilters)
        chooseFilterCombobox.insert(0, 'None')
        chooseFilterCombobox.grid(row=0, column=0)

        chooseFilterButton = Button(rootChoose, text='SUBMIT', command=lambda:forDetailFilter(chooseFilterCombobox.get(), rootChoose))
        chooseFilterButton.grid(row=0, column=1)



        chooseBackButton = Button(rootChoose, text='Back', command=toHub)
        chooseBackButton.grid(row=100, sticky=W)
    else:
        bericht = "Helaas hebben we geen kledingstukken aangetroffen om uit te kiezen."
        showinfo(title='Clothing error', message=bericht)


def toGenScreen():
    """
    Via deze functie ga je vanaf het homescreen naar het automatisch setjes genereren scherm.
    """

    rootHm.destroy()
    setGenScreen()


def setGenScreen():
    """
    In deze functie word het frame aangemaakt voor het automatisch uitkiezen van een kledingsetje voor jou.
    """

    global rootGen
    global Globroot

    rootGen = Tk()
    rootGen.title('Generator')
    Globroot = rootGen
    rootGen.geometry("450x175")

    showMenu(rootGen)

    GenTitleLabel = Label(rootGen, text='Voor welke gelegenheid wil je een kledingstuk uitkiezen: ', background="#c6def1", font=("Helvetica", 10))
    GenTitleLabel.place(x=0, y=0)

    genDagelijksButton = Button(rootGen, text='Dagelijks leven', command=lambda:frame('dagelijks leven', userName, setGenScreen, showMenu, rootGen), width=13, height="2")
    genDagelijksButton.place(x=5, y=30)

    genSportutton = Button(rootGen, text='Sport', command=lambda:frame('sport', userName, setGenScreen, showMenu, rootGen), width=13, height="2")
    genSportutton.place(x=150, y=30)

    genFeestButton = Button(rootGen, text='Feest', command=lambda:frame('feestje', userName, setGenScreen, showMenu, rootGen), width=13, height="2")
    genFeestButton.place(x=300, y=30)

    genBackButton = Button(rootGen, text='Back', command=toHub, width=7, height="2")
    genBackButton.place(x=5, y=110)

    rootGen.mainloop()


def showMenu(root):
    """
    Deze functie word in bijna alle frames aangeroepen om zo het drop down menu overal het zelfde weer te geven.
    """

    global toDestroyRoot

    root.configure(background='#c6def1')
    root.iconbitmap('../overige_bestanden/kledingkastIco.ico')


    toDestroyRoot = root
    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    subMenu.config(fg="#555b6e")
    menu.add_cascade(label='Settings', menu=subMenu)
    subMenu.add_command(label='Personal data', command=changePersonalData)
    subMenu.add_command(label='Delete account', command=deleteAccountCheck)
    subMenu.add_separator()
    subMenu.add_command(label='Log out', command=toLogIn)
    subMenu.add_command(label='Exit', command=exitProg)


def toHub():
    """
    Deze functie zorgt voor het destroyen van het vorige frame en stuurt je door naar het homescreen.
    """

    toDestroyRoot.destroy()
    Homescreen()


def exitProg():
    """
    Deze functie zorgt ervoor dat je het programma  afsluit door het enige frame dat openstaat te destroyen.
    """

    exit(0)


def commitPersonalData(BetweenWear, City, Land, ChangeName):
    """
    Deze functie zorgt ervoor dat de ingevulde data die je wilt veranderen van jouw profiel opgeslagen word.
    """

    global userName
    global Globroot
    changedUserName = str(gegWijzigen(userName, BetweenWear, City, Land, ChangeName))
    userName = changedUserName
    rootCPD.destroy()
    Globroot=rootHm


def toHomeScreen(name):
    """
    Deze functie word gebruikt bij de login om te checken of je door kan worden gestuurde naar het hoofdscherm.
    """

    if checkIfExist(name) is True:
        global userName
        userName = name
        rootLogin.destroy()
        Homescreen()
    else:
        bericht = 'Username not existend, try it it again!'
        showinfo(title='UserName error', message=bericht)


def toLogin(signUpName, signUpStad, signUpLand):
    """
    Hier check je of de ingevulde waardes om je aan te melden kloppen en correct kunnen worden verwerkt.
    """

    if len(signUpStad) == 0 or len(signUpLand) == 0 or len(signUpName) == 0:
        #string met alle entry's die verkeerd ingevuld zijn.
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

def testDatabase():
    """
    Deze functie is zeer belangrijk. Mocht een window niet correct gesloten worden op het verkeerde moment kan het
    voorkomen dat de database leeg raakt. Dit vermijd ik door hem dan opnieuw te schrijven vanuit de backupDatabase.
    """

    try:
        with open('../jsonFiles/Kledingkast.json', 'r') as doc:
            json.load(doc)
    except:
        with open("../jsonFiles/Kledingkast.json", 'w') as f:

            with open("../jsonFiles/BackupKledingkast.json", 'r') as backUpInfSetback:
                Information = json.load(backUpInfSetback)
            json.dump(Information, f)


file = pathlib.Path("../jsonFiles/Kledingkast.json")
if file.exists():
    testDatabase()
    Login()
else:
    with open("../jsonFiles/Kledingkast.json", 'w+') as f:
        f.write('{}')
    with open("../jsonFiles/BackupKledingkast.json", 'w+') as f:
        f.write('{}')
    Login()

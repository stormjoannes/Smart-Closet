from tkinter import *
from tkinter.font import BOLD
from tkinter.messagebox import showinfo
from Functions import *
import json
from tkinter import ttk


def Signup():  # This is the signup definition,
    rootA.destroy()
    global rootSignUp
    global Globroot

    rootSignUp = Tk()
    rootSignUp.title('Signup')
    Globroot = rootSignUp

    showMenuLoginSignup(rootSignUp)

    intruction = Label(rootSignUp, text='Sign aub\n', background="gray")
    intruction.grid(row=0, column=0,
                    sticky=E)

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

    # intruction = Label(roots, text='Sign aub\n', background="gray", font=("Helvetica", 100))
    # intruction.pack()
    #
    # nameL = Label(roots, text='Nieuwe naam: ', background="gray", font=("Helvetica", 50))
    # nameL.pack()
    #
    # nameE = Entry(roots, font=("Helvetica", 50))
    # nameE.pack()
    #
    # signUpStadField = Label(roots, text='Stad naam: ', background="gray", font=("Helvetica", 50))
    # signUpStadField.pack()
    #
    # signUpStadEntry = Entry(roots, font=("Helvetica", 50))
    # signUpStadEntry.pack()
    #
    # signUpLandField = Label(roots, text='De afkorting van je land: ', background="gray", font=("Helvetica", 50))
    # signUpLandField.pack()
    #
    # signUpLandEntry = Entry(roots, font=("Helvetica", 50))
    # signUpLandEntry.pack()
    #
    # signupButton = Button(roots, text='Signup',
    #                       command=toLogin)
    # signupButton.pack()
    #
    # backLogin = Button(roots, text='Login', fg='Blue',
    #                 command=FSSignup)
    # backLogin.pack()



    rootSignUp.mainloop()


def toLogIn():
    Globroot.destroy()
    Login()

def showMenuLoginSignup(root):

    root.geometry('1920x1080')
    root.configure(background='gray')

    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label='file', menu=subMenu)
    subMenu.add_command(label='exit', command=exit)


def Login():
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

    # intruction = Label(rootA, text='Log in\n', background="gray", font=("Helvetica", 100))
    # intruction.pack(side=TOP)
    #
    # nameL = Label(rootA, text='Username: ', background="gray", font=("Helvetica", 50))
    # nameL.pack(pady=10, )
    #
    # nameEL = Entry(rootA, font=("Helvetica", 20))
    # nameEL.pack(ipadx=100, ipady=10, pady=10)
    #
    # loginB = Button(rootA, text='Login', command=toHomeScreen, font=("Helvetica", 50))
    # loginB.pack(side=LEFT, ipadx=100, ipady=70, padx=20)
    #
    # rmuser = Button(rootA, text='Sign in', fg='Blue',
    #                 command=Signup, font=("Helvetica", 50))
    # rmuser.pack(side=LEFT, ipadx=100, ipady=70)

    rootA.mainloop()

try:
    def Homescreen():
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

        homescreenAutomaticGenButton = Button(rootHm, fg='blue', text='Automatisch genereren van je kleding setje ', command=setGenScreen)
        homescreenAutomaticGenButton.grid(row=5)

        rootHm.mainloop()
except:
    bericht = "Er is iets mis gegaan, probeer het opnieuw!"
    showinfo(title='System error', message=bericht)
    Login()


def AddScreen():
    rootHm.destroy()
    global rootAdd
    global Globroot

    rootAdd = Tk()
    rootAdd.title('ADD')
    Globroot = rootAdd

    showMenu(rootAdd)
    inputParametersClothing(rootAdd)

    addscreenADDButton = Button(rootAdd, text='Voeg kledingstuk toe!', command=lambda:toAddClothing(userName, str(screenNameEntry.get()), str(screenLongShortEntry.get()), str(screenOpportunityEntry.get()), str(screenColorEntry.get()), str(screenBrandEntry.get()), str(screenCategoryEntry.get()), toHub))
    addscreenADDButton.grid(row=7)

    rootAdd.mainloop()


def inputParametersClothing(root):
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
    with open('Kledingkast.json', 'r') as Clothes:
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

        deletescreenDELETEButton = Button(rootDelete, text='Verwijder kledingstuk!', command=lambda:toDeleteClothing(userName, str(screenNameEntry.get()), str(screenLongShortEntry.get()), str(screenOpportunityEntry.get()), str(screenColorEntry.get()), str(screenBrandEntry.get()), str(screenCategoryEntry.get()), toHub))
        deletescreenDELETEButton.grid(row=7)

        rootDelete.mainloop()
    else:
        bericht = "Helaas hebben we geen kledingstukken aangetroffen om te verwijderen."
        showinfo(title='Clothing error', message=bericht)


def changePersonalData():
    global rootCPD

    rootCPD = Tk()
    rootCPD.title('personal data')

    showMenu(rootCPD)

    with open('Kledingkast.json', 'r+') as docPersonalData:
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
    global rootDeleteAccount
    rootDeleteAccount = Tk()
    rootDeleteAccount.title('Account delete')

    delAccountTitle = Label(rootDeleteAccount, text='Weet je zeker dat je je account wilt verwijderen: ', background="gray")
    delAccountTitle.grid(row=1, column=0,  sticky=W)

    delAccountYesButton = Button(rootDeleteAccount, text='Ja', command=deleteAccount)
    delAccountYesButton.grid(row=3, sticky=W)

    delAccountNeeButton = Button(rootDeleteAccount, text='Nee', command=toHub)
    delAccountNeeButton.grid(row=3, sticky=E)

    rootDeleteAccount.mainloop()


def deleteAccount():
    with open('Kledingkast.json', 'r') as ALLaccounts:
        deleteAccountData = json.load(ALLaccounts)
        deleteAccountData.pop(userName)

    with open('Kledingkast.json', 'w') as deleteACC:
        json.dump(deleteAccountData, deleteACC)
    backupDump()
    Globroot.destroy()
    rootDeleteAccount.destroy()
    Login()


def UitkiezenScreen():
    with open('Kledingkast.json', 'r') as Clothes:
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


def setGenScreen():
    rootHm.destroy()
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

    genDagelijksButton = Button(rootGen, text='Dagelijks leven', command=lambda:WeatherForPickClothes('dagelijks'))
    genDagelijksButton.grid(row=2, sticky=W)

    genSportutton = Button(rootGen, text='Sport', command=lambda:WeatherForPickClothes('sport'))
    genSportutton.grid(row=2, column=0)

    genFeestButton = Button(rootGen, text='Feest', command=lambda:WeatherForPickClothes('feest'))
    genFeestButton.grid(row=2, column=1)

    GenSpaceLabel = Label(rootGen, text='', background="gray")
    GenSpaceLabel.grid(row=3)

    genBackButton = Button(rootGen, text='Back', command=toHub)
    genBackButton.grid(row=5, sticky=W)

    rootGen.mainloop()

def WeatherForPickClothes(func):
    global loopIndex
    if func == 'dagelijks':
        opportunity = 'dagelijks leven'
    elif func == 'sport':
        opportunity = 'sport'
    elif func == 'feest':
        opportunity = 'feestje'

    with open('Kledingkast.json', 'r+') as Data:
        placeInfo = json.load(Data)

    stad = placeInfo[userName][0]["gegevens"][0]["locatie"]["stad"]
    land = placeInfo[userName][0]["gegevens"][0]["locatie"]["land"]
    huidigeWeer = setValuesWeer(stad, land)
    gevoelsTemp = huidigeWeer[0]
    windSnelheid = huidigeWeer[2]
    if windSnelheid >= 5:
        gevoelsTemp = 13.12 + 0.6215 * gevoelsTemp - 11.37 * windSnelheid ** 0.16 + 0.3965 * gevoelsTemp * windSnelheid ** 0.16
    RandClothes = pickClothes(userName, gevoelsTemp, huidigeWeer[1], opportunity)
    loopIndex = 0
    recommendedClothes(RandClothes[0], RandClothes[1], loopIndex)


def showMenu(root):
    global toDestroyRoot

    root.geometry('1920x1080')
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
def autoGen(mogelijkeTops, mogelijkeBottoms, aantrekken, top, bottom, data, loopIndex):
    rootWear.destroy()
    if aantrekken == "ja":

        with open('Kledingkast.json', 'w') as ALL:
            today = datetime.today().strftime("%Y-%m-%d")
            formatVoorAppend = [top, bottom, str(today)]
            data[userName][1]["gedragen"].append(formatVoorAppend)
            json.dump(data, ALL)
            ALL.close()
            rootGen.update()
            rootGen.destroy()
            Homescreen()

    else:
        mogelijkeTops.remove(top)
        mogelijkeBottoms.remove(bottom)
        recommendedClothes(mogelijkeTops, mogelijkeBottoms, loopIndex)

def recommendedClothes(mogelijkeTop, mogelijkeBottom, loopIndex):
    mogelijkeTops = mogelijkeTop
    mogelijkeBottoms = mogelijkeBottom

    with open('Kledingkast.json', 'r+') as inf:
        data = json.load(inf)

    loopIndex += 1

    if len(mogelijkeTops) != 0:
        top = random.choice(mogelijkeTops)

        if top[2] != 'jurkje':
            if len(mogelijkeBottoms) != 0:
                bottom = random.choice(mogelijkeBottoms)
                if bottom[1] == top[1]:
                    bottom.random.choice(mogelijkeBottoms)
            else:
                bottom = None
    else:
        top = None

    if top == None or top == None and bottom == None or top[2] != 'jurkje' and bottom == None:
        bericht = "Helaas hebben we met deze beperkte kleding hoeveelheid geen setje kunnen vinden om aan te trekken."
        showinfo(title='Clothing error', message=bericht)
        rootGen.update()
        rootGen.destroy()
        Homescreen()
    else:
        global rootWear
        global Globroot
        rootWear = Tk()
        rootWear.title("Wear clothes")
        Globroot = rootWear

        showMenu(rootWear)

        GenTopLabel = Label(rootWear, text=f'Top: {top}', background="gray")
        GenTopLabel.grid(row=5)

        GenBottomLabel = Label(rootWear, text=f'Bottom: {bottom}', background="gray")
        GenBottomLabel.grid(row=6)

        genTitleLabel = Label(rootWear, text='Ga je dit setje dragen:', background="gray")
        genTitleLabel.grid(row=9)

        genYesButton = Button(rootWear, text='Ja', command=lambda:autoGen(mogelijkeTops, mogelijkeBottoms, 'ja', top, bottom, data, loopIndex))
        genYesButton.grid(row=11, sticky=W)

        genNoButton = Button(rootWear, text='Nee', command=lambda:autoGen(mogelijkeTops, mogelijkeBottoms, 'nee', top, bottom, data, loopIndex))
        genNoButton.grid(row=11, sticky=E)

        genBackButton = Button(rootWear, text='Back', command=exit)
        genBackButton.grid(row=12)

        rootWear.mainloop()


def toHub():
    toDestroyRoot.destroy()
    Homescreen()


def exit():
    Globroot.destroy()

def commitPersonalData(BetweenWear, City, Land, ChangeName):
    global userName
    global Globroot
    changedUserName = str(gegWijzigen(userName, BetweenWear, City, Land, ChangeName))
    userName = changedUserName
    rootCPD.destroy()
    Globroot=rootHm


def toHomeScreen(name):
    if checkIfExist(name) == True:
        global userName
        userName = name
        rootA.destroy()
        Homescreen()
    else:
        bericht = 'Username not existend, try it it again!'
        showinfo(title='UserName error', message=bericht)

def toLogin(signUpName, signUpStad, signUpLand):
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


# statusDB = "positive"
# try:
#     with open('BackupKledingkast.json', 'r') as BackupData:
#         backupDataDrawBack = json.load(BackupData)
#
#     with open('Kledingkast.json', 'w') as frRefresh:
#         json.dump(backupDataDrawBack, frRefresh)
#         frRefresh.close()
# except:
#     statusDB = "negative"
#
# if statusDB == "positive":
Login()
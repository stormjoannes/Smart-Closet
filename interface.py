from tkinter import *
from tkinter.font import BOLD
from tkinter.messagebox import showinfo
from Main import *
import json
from tkinter import ttk


def Signup():  # This is the signup definition,
    rootA.destroy()
    global nameE
    global roots
    global signUpStadEntry
    global signUpLandEntry

    roots = Tk()
    roots.title('Signup')

    showMenuLoginSignup(roots)

    intruction = Label(roots, text='Sign aub\n', background="gray")
    intruction.grid(row=0, column=0,
                    sticky=E)

    nameL = Label(roots, text='Nieuwe naam: ', background="gray")
    nameL.grid(row=1, column=0,
               sticky=W)

    nameE = Entry(roots)
    nameE.grid(row=1, column=1)

    signUpStadField = Label(roots, text='Stad naam: ', background="gray")
    signUpStadField.grid(row=2, column=0,
               sticky=W)

    signUpStadEntry = Entry(roots)
    signUpStadEntry.grid(row=2, column=1)

    signUpLandField = Label(roots, text='De afkorting van je land: ', background="gray")
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
    backLogin.pack()



    roots.mainloop()


def FSSignup():
    roots.destroy()
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
    global nameEL
    global rootA
    global Globroot

    rootA = Tk()
    rootA.title('Login')
    Globroot = rootA
    # frame = Frame(rootA, bg="black")
    # frame.grid(ipadx=1920 , ipady=1080)

    showMenuLoginSignup(rootA)

    intruction = Label(rootA, text='Log in\n', background="gray", font=("Helvetica", 20))
    intruction.grid(column=1)

    nameL = Label(rootA, text='Username: ', background="gray")
    nameL.grid(row=1, sticky=W)

    nameEL = Entry(rootA)
    nameEL.grid(row=1, column=1)

    loginB = Button(rootA, text='Login',
                    command=toHomeScreen)
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


def Homescreen():
    global rootHm
    global Globroot

    rootHm = Tk()
    rootHm.title('Home')
    Globroot = rootHm

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


def AddScreen():
    rootHm.destroy()
    global rootAdd
    # global addscreenNameEntry
    # global addscreenLongShortEntry
    # global addscreenOpportunityEntry
    # global addscreenColorEntry
    # global addscreenBrandEntry
    # global addscreenCategoryEntry
    global Globroot

    rootAdd = Tk()
    rootAdd.title('ADD')
    Globroot = rootAdd

    showMenu(rootAdd)

    # addscreenTitle = Label(rootAdd, text='Vul de parameters van je kledingstuk in: ', background="gray")
    # addscreenTitle.grid(row=0, sticky=W)
    #
    # addscreenNameLabel = Label(rootAdd, text='Naam: ', background="gray")
    # addscreenNameLabel.grid(row=1, column=0,  sticky=W)
    #
    # addscreenNameEntry = Entry(rootAdd)
    # addscreenNameEntry.grid(row=1, column=1)
    #
    # addscreenLongShortLabel = Label(rootAdd, text='lang/kort broekspijpen/mouwen: ', background="gray")
    # addscreenLongShortLabel.grid(row=2, column=0,  sticky=W)
    #
    # addscreenLongShortEntry = Entry(rootAdd)
    # addscreenLongShortEntry.grid(row=2, column=1)
    #
    # addscreenOpportunityLabel = Label(rootAdd, text='Gelegenheid(dagelijks leven, sport of feestje): ', background="gray")
    # addscreenOpportunityLabel.grid(row=3, column=0,  sticky=W)
    #
    # addscreenOpportunityEntry = Entry(rootAdd)
    # addscreenOpportunityEntry.grid(row=3, column=1)
    #
    # addscreenColorLabel = Label(rootAdd, text='Kleur: ', background="gray")
    # addscreenColorLabel.grid(row=4, column=0,  sticky=W)
    #
    # addscreenColorEntry = Entry(rootAdd)
    # addscreenColorEntry.grid(row=4, column=1)
    #
    # addscreenBrandLabel = Label(rootAdd, text='Merk: ', background="gray")
    # addscreenBrandLabel.grid(row=5, column=0,  sticky=W)
    #
    # addscreenBrandEntry = Entry(rootAdd)
    # addscreenBrandEntry.grid(row=5, column=1)
    #
    # addscreenCategoryLabel = Label(rootAdd, text='Categorie: ', background="gray")
    # addscreenCategoryLabel.grid(row=6, column=0,  sticky=W)
    #
    # addscreenCategoryEntry = Entry(rootAdd)
    # addscreenCategoryEntry.grid(row=6, column=1)

    inputParametersClothing(rootAdd)

    addscreenADDButton = Button(rootAdd, text='Voeg kledingstuk toe!', command=toAddClothing)
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

def DeleteScreen():
    rootHm.destroy()
    global rootDelete
    global Globroot

    rootDelete = Tk()
    rootDelete.title('DELETE')
    Globroot = rootDelete

    showMenu(rootDelete)

    inputParametersClothing(rootDelete)

    deletescreenDELETEButton = Button(rootDelete, text='Verwijder kledingstuk!', command=toDeleteClothing)
    deletescreenDELETEButton.grid(row=7)

    rootDelete.mainloop()

def changePersonalData():
    global rootCPD
    global Globroot
    global personaldataUserNameEntry
    global personaldataBetweenWearEntry
    global personaldataCityEntry
    global personaldataLandEntry

    rootCPD = Tk()
    rootCPD.title('personal data')
    Globroot = rootCPD

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

    personaldataSubmitChanges = Button(rootCPD, text='Toepassen', command=commitPersonalData)
    personaldataSubmitChanges.grid(sticky=E)

    rootCPD.mainloop()

def UitkiezenScreen():
    rootHm.destroy()
    global Globroot

    global rootChoose
    global chooseFilterCombobox

    rootChoose = Tk()
    rootChoose.title('Choose')
    Globroot = rootChoose

    showMenu(rootChoose)

    chooseTitleLabel = Label(rootChoose, text='Al je kleren: ', background="gray")
    chooseTitleLabel.grid(row=2)

    chooseEmptySpaceLabel = Label(rootChoose, text='', background="gray")
    chooseEmptySpaceLabel.grid(row=3)

    allClothes()

    possibleFilters = getAllPossibleFilters(userName)

    chooseFilterLabel = Label(rootChoose, text='Filter: ', background="gray")
    chooseFilterLabel.grid(row=0, sticky=W)

    chooseFilterCombobox = ttk.Combobox(rootChoose, value=possibleFilters)
    chooseFilterCombobox.insert(0, 'None')
    chooseFilterCombobox.grid(row=0, column=0)

    chooseFilterButton = Button(rootChoose, text='SUBMIT', command=forDetailFilter)
    chooseFilterButton.grid(row=0, column=1)

    chooseDeleteFilterButton = Button(rootChoose, text='Delete Filter', command=toDeleteFilter)
    chooseDeleteFilterButton.grid(row=100, sticky=E)

    chooseBackButton = Button(rootChoose, text='Back', command=toHub)
    chooseBackButton.grid(row=100, sticky=W)

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

    genDagelijksButton = Button(rootGen, text='Dagelijks leven', command=setChoiceGenDagelijks)
    genDagelijksButton.grid(row=10, sticky=W)

    genSportutton = Button(rootGen, text='Sport', command=setChoiceGenSport)
    genSportutton.grid(row=10, column=0)

    genFeestButton = Button(rootGen, text='Feest', command=setChoiceGenFeest)
    genFeestButton.grid(row=10, column=1)


    # WeatherForPickClothes()
    rootGen.mainloop()

def setChoiceGenDagelijks():
    WeatherForPickClothes('dagelijks')
def setChoiceGenSport():
    WeatherForPickClothes('sport')
def setChoiceGenFeest():
    WeatherForPickClothes('feest')

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
    # getRandGenClothes(RandClothes[0], RandClothes[1], loopIndex)
    recommendedClothes(RandClothes[0], RandClothes[1], loopIndex)
    # rootGen.mainloop()


def showMenu(root):
    global toDestroyRoot
    global Globroot

    # Globroot = root

    Globroot.geometry('1920x1080')
    Globroot.configure(background='gray')

    toDestroyRoot = root
    menu = Menu(root)
    root.config(menu=menu)
    Globroot = toDestroyRoot

    subMenu = Menu(menu)
    menu.add_cascade(label='file', menu=subMenu)
    subMenu.add_command(label='personal data', command=changePersonalData)
    subMenu.add_separator()
    subMenu.add_command(label='homescreen', command=toHub)
    subMenu.add_command(label='exit', command=exit)

def autoGen(mogelijkeTops, mogelijkeBottoms, aantrekken, top, bottom, data, loopIndex):
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
    global mogelijkeTops
    global mogelijkeBottoms
    global top
    global bottom
    global data

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

        genYesButton = Button(rootWear, text='Ja', command=WearYes)
        genYesButton.grid(row=11, sticky=W)

        genNoButton = Button(rootWear, text='Nee', command=WearNo)
        genNoButton.grid(row=11, sticky=E)

        rootWear.mainloop()


def WearYes():
    rootWear.destroy()
    autoGen(mogelijkeTops, mogelijkeBottoms, 'ja', top, bottom, data, loopIndex)


def WearNo():
    rootWear.destroy()
    autoGen(mogelijkeTops, mogelijkeBottoms, 'nee', top, bottom, data, loopIndex)


def toHub():
    toDestroyRoot.destroy()
    Homescreen()


def exit():
    Globroot.destroy()


def commitPersonalData():
    global userName
    changedUserName = str(gegWijzigen(userName, personaldataBetweenWearEntry.get(), personaldataCityEntry.get(), personaldataLandEntry.get(), personaldataUserNameEntry.get()))
    userName = changedUserName
    Globroot.destroy()


def toHomeScreen():
    if checkIfExist(str(nameEL.get())) == True:
        global userName
        userName = nameEL.get()
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
    addClothes(userName, str(screenNameEntry.get()), str(screenLongShortEntry.get()),
               str(screenOpportunityEntry.get()), str(screenColorEntry.get()), str(screenBrandEntry.get()),
               str(screenCategoryEntry.get()))
    rootAdd.destroy()
    Homescreen()

def toDeleteClothing():
    statusDelete = deleteClothes(userName, str(screenNameEntry.get()), str(screenLongShortEntry.get()),
               str(screenOpportunityEntry.get()), str(screenColorEntry.get()), str(screenBrandEntry.get()),
               str(screenCategoryEntry.get()))

    if statusDelete == False:
        bericht = f'kledingstuk {str(deletescreenNameEntry.get())} bestaat niet en kan dus ook niet verwijderd worden!'
        showinfo(title='Delete Error', message=bericht)

    rootDelete.destroy()
    Homescreen()

def allClothes():
    global AllClothes

    allClothingString = ''

    for indexAll in range(2, len(allInfVariables[userName])):
        allClothingString += str(allInfVariables[userName][indexAll]) + '\n'

    AllClothes = Label(rootChoose, text=f'{allClothingString}: ', background="gray")
    AllClothes.grid(row=indexAll + 2, column=0)

def toDeleteFilter():
    try:
        AllClothesDetailFiltered.destroy()
    except:
        bericht = 'No filter applied!'
        showinfo(title='Filter Error', message=bericht)
    allClothes()

def getDetailFilters():
    global AllClothesDetailFiltered

    watBekijken = chooseFilterCombobox.get()
    detailFilter = chooseDetailFilterEntry.get()

    AllClothes.destroy()

    allFilteredClothingString = ''
    for indexAllFiltered in range(2, len(allInfVariables[userName])):
        if detailFilter in allInfVariables[userName][indexAllFiltered][watBekijken]:
            allFilteredClothingString += str(allInfVariables[userName][indexAllFiltered]) + '\n'

    AllClothesDetailFiltered = Label(rootChoose, text=f'{allFilteredClothingString}: ', background="gray")
    AllClothesDetailFiltered.grid(row=indexAllFiltered, column=0)

def forDetailFilter():
    global chooseDetailFilterEntry

    chooseFilterLabel = Label(rootChoose, text=f'Op welke {chooseFilterCombobox.get()} wil je filteren: ', background="gray")
    chooseFilterLabel.grid(row=1, sticky=W)

    chooseDetailFilterEntry = Entry(rootChoose)
    chooseDetailFilterEntry.grid(row=1, column=0)

    chooseFilterButton = Button(rootChoose, text='SUBMIT', command=getDetailFilters)
    chooseFilterButton.grid(row=1, column=1)
try:
    Login()
except:
    bericht = "Helaas er is iets misgegaan, je word terug gestuurd naar het beginscherm."
    showinfo(title='Clothing error', message=bericht)
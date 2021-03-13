import pyodbc 



conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=  ;' # server i use SQL Server Managment Studio and i take my pc name here but you use yours one 
                      'Database=SE307proje;' # write your database name i use my project SE307proje
                      'Trusted_Connection=yes;')
#we have University , Enstitute , Author , Thesis , Type , Language , Supervisor , COSupervisor
#i create this tables on SQL and they have relation
#author has university and enstitute also they have id and name
#thesis have  type , language  , supervisor , co-supervisor , title , abstract , year ,  number of page , submission date
#this program working on terminal


cursor = conn.cursor()
queryCommand = """SELECT Thesis.ThesisID,Author.AuthorName, Author.AuthorSurname, University.UniversityName , Enstitute.EnstituteName , Type.Types , Language.Languages , Supervisor.SupervisorName , Supervisor.SupervisorSurname , Thesis.Title ,  Thesis.Abstract,Thesis.Year,Thesis.NumberOfPages,Thesis.SubmissionDate
FROM Thesis
INNER JOIN Author on Thesis.AuthorID = Author.AuthorID 
INNER JOIN University on Author.UniversityID = University.UniversityID
INNER JOIN Enstitute on Author.EnstituteID = Enstitute.EnstituteID
INNER JOIN Type on Thesis.TypeID = Type.TypeID
INNER JOIN Language on Thesis.LanguageID = Language.LanguageID
INNER JOIN Supervisor on Thesis.SupervisorID = Supervisor.SupervisorID"""

def printUniversity():
    cursor.execute('SELECT * FROM dbo.University')
    print("university table is")
    print()
    print("The table of contents is as follows: (UniversityID , UniversityName)")
    print()
    for row in cursor:
        print(row)
    print()

def printEnstitute():
    cursor.execute('SELECT * FROM dbo.Enstitute')
    print("Ensititute table is")
    print()
    print("The table of contents is as follows: (EnstituteID , EnstituteName)")
    print()
    for row in cursor:
        print(row)
    print()

def printAuthor():
    cursor.execute('SELECT * FROM dbo.Author')
    print("Author table is")
    print()
    print("The table of contents is as follows: (AuthorID , UniversityID , EnstituteID, AuthorName , AuthorSurname)")
    print()
    for row in cursor:
        print(row)
    print()

def printLanguage():
    cursor.execute('SELECT * FROM dbo.Language')
    print("Language table is")
    print()
    print("The table of contents is as follows:(LanguageID , Language)")
    print()
    for row in cursor:
        print(row)
    print()

def printType():
    cursor.execute('SELECT * FROM dbo.Type')
    print("Type table is")
    print()
    print("The table of contents is as follows: (TypeId , Type)")
    print()
    for row in cursor:
        print(row)
    print()

def printSupervisor():
    cursor.execute('SELECT * FROM dbo.Supervisor')
    print("Supervisor table is")
    print()
    print("The table of contents is as follows : (SupervisorID , SupervisorName , SupervisorSurname)")
    print()
    for row in cursor:
        print(row)
    print()

def printCOSupervisor():
    cursor.execute('SELECT * FROM dbo.COSupervisor')
    print("COSupervisor table is")
    print()
    print("The table of contents is as follows : (COSupervisorID , COSupervisorName , COSupervisorSurname)")
    print()
    for row in cursor:
        print(row)
    print()

def printThesis():
    cursor.execute('SELECT * FROM dbo.Thesis')
    print("Thesis table is")
    print()
    print("The table of contents is as follows : (ThesisID , AuthorID , TypeID , LanguageID , SupervisorID , COSupervisorID , Title , Abstract , Year , NumberOfPage , SubmissionDate)")
    print()
    for row in cursor:
        print(row)
    print()

def updateUniversity():
    printUniversity()
    UniversityID = input("Which id of university should we change ? : ")
    UniversityName = input("Enter your university name: ")
    result = cursor.execute('UPDATE University SET UniversityName = ? WHERE UniversityID = ?',('{}'.format(UniversityName),UniversityID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printUniversity()

def updateEnstitute():
    printEnstitute()
    EnstituteID = input("Which id of enstitute should we change ? : ")
    EnstituteName = input("Enter your enstitute name: ")
    result = cursor.execute('UPDATE Enstitute SET EnstituteName = ? WHERE EnstituteID = ?',('{}'.format(EnstituteName),EnstituteID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printEnstitute()

def updateLanguage():
    printLanguage()
    LanguageID =input("Which id of language should we change ? : ")
    Languages =input("Enter language : ")
    result = cursor.execute('UPDATE Language SET Languages = ? WHERE LanguageID = ?',('{}'.format(Languages),LanguageID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printLanguage()

def updateTypes():
    printType()
    TypeID = input("Which id of type should we change ? : ")
    Types = input("Enter a new type of thesis : ")
    result = cursor.execute('UPDATE Type SET Types = ? WHERE TypeID = ?',('{}'.format(Types),TypeID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printType()

def updateSupervisorName():
    printSupervisor()
    SupervisorID = input("Which id of Supervisor should we change ? : ")
    SupervisorName = input("What is Supervisor name ? : ")
    result = cursor.execute('UPDATE Supervisor SET SupervisorName = ? WHERE SupervisorID = ?',('{}'.format(SupervisorName),SupervisorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printSupervisor()

def updateSupervisorSurname():
    printSupervisor()
    SupervisorID = input("Which id of Supervisor should we change ? : ")
    SupervisorSurname = input("What is the Supervisor surname ? : ")
    result = cursor.execute('UPDATE Supervisor SET SupervisorSurname = ? WHERE SupervisorID = ?',('{}'.format(SupervisorSurname),SupervisorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printSupervisor()

def updateCOSupervisorName():
    printCOSupervisor()
    COSupervisorID = input("Which id of CO-Supervisor should we change ? : ")
    COSupervisorName = input("What is the CO-Supervisor name ? : ")
    result = cursor.execute('UPDATE COSupervisor SET COSupervisorName = ? WHERE COSupervisorID = ?',('{}'.format(COSupervisorName),COSupervisorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printCOSupervisor()

def updateCOSupervisorSurname():
    printCOSupervisor()
    COSupervisorID = input("Which id of CO-Supervisor should we change ? : ")
    COSupervisorSurname = input("What is the CO-Supervisor surname ? : ")
    result = cursor.execute('UPDATE COSupervisor SET COSupervisorSurname = ? WHERE COSupervisorID = ?',('{}'.format(COSupervisorSurname),COSupervisorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printCOSupervisor()

def updateAuthorUniversityID():
    printAuthor()
    AuthorID = input("Which id of Author should we change ? : ")
    UniversityID = input("what is the Author's new university id? : ")
    result = cursor.execute('UPDATE Author SET UniversityID = ? WHERE AuthorID = ?',('{}'.format(UniversityID),AuthorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printAuthor()

def updateAuthorEnstituteID():
    printAuthor()
    AuthorID = input("Which id of Author should we change ? : ")
    EnstituteID = input("what is the Author's new enstitute id? : ")
    result = cursor.execute('UPDATE Author SET EnstituteID = ? WHERE AuthorID = ?',('{}'.format(EnstituteID),AuthorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printAuthor()

def updateAuthorAuthorName():
    printAuthor()
    AuthorID = input("Which id of Author should we change ? : ")
    AuthorName = input("what is the Author's new name ? : ")
    result = cursor.execute('UPDATE Author SET AuthorName = ? WHERE AuthorID = ?',('{}'.format(AuthorName),AuthorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printAuthor()

def updateAuthorSurname():
    printAuthor()
    AuthorID = input("Which id of Author should we change ? : ")
    AuthorSurname = input("what is the Author's new surname ? : ")
    result = cursor.execute('UPDATE Author SET AuthorSurname = ? WHERE AuthorID = ?',('{}'.format(AuthorSurname),AuthorID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printAuthor()

def updateThesisAuthor():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    printAuthor()
    AuthorID = input("What is the new Author ID please enter right AuthorID ? : ")
    result = cursor.execute('UPDATE Thesis SET AuthorID = ?  WHERE ThesisID = ?',('{}'.format(AuthorID),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisType():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    printType()
    TypeID = input("What is the new Type ID please enter right TypeID ? : ")
    result = cursor.execute('UPDATE Thesis SET TypeID = ? WHERE ThesisID = ?',('{}'.format(TypeID),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisLanguage():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    printLanguage()
    LanguageID = input("What is the new Language ID please enter right LanguageID ? : ")
    result = cursor.execute('UPDATE Thesis SET LanguageID = ? WHERE ThesisID = ?',('{}'.format(LanguageID),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisSupervisor():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    printSupervisor()
    SupervisorID = input("What is the new Supervisor ID please enter right SupervisorID? : ")
    result = cursor.execute('UPDATE Thesis SET SupervisorID = ?  WHERE ThesisID = ?',('{}'.format(SupervisorID),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisCOSupervisor():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    printCOSupervisor()
    COSupervisorID =input("What is the new CO-Supervisor ID please enter right COSupervisorID ? : ")
    result = cursor.execute('UPDATE Thesis SET COSupervisorID = ?  WHERE ThesisID = ?',('{}'.format(COSupervisorID),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisTitle():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    Title = input("What is the new Title ? : ")
    result = cursor.execute('UPDATE Thesis SET Title = ? WHERE ThesisID = ?',('{}'.format(Title),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisAbstract():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    Abstract = input("What is the new Abstract")
    result = cursor.execute('UPDATE Thesis SET Abstract = ? WHERE ThesisID = ?',('{}'.format(Abstract),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisYear():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    Year = input("What is the write year: ")
    result = cursor.execute('UPDATE Thesis SET Year = ?  WHERE ThesisID = ?',('{}'.format(Year),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def updateThesisNumberOfPages():
    printThesis()
    ThesisID = input("Which id of Thesis should we change ? : ")
    NumberOfPages = input("What is the number of pages in thesis ? : ")
    result = cursor.execute('UPDATE Thesis SET NumberOfPages = ? WHERE ThesisID = ?',('{}'.format(NumberOfPages),ThesisID))
    cursor.commit()
    print(str(cursor) + " data was update")
    printThesis()

def insertUniversity():
    printUniversity()
    UniversityID = input("new id of University : ")
    University =  input("new id of University : ")
    insert = insert = 'INSERT INTO University VALUES(?,?)'
    data =(UniversityID,University)
    result = cursor.execute(insert,data)
    cursor.commit()
    printUniversity()

def insertEnstitute():
    printEnstitute()
    EnstituteID = input("new id of Enstitute : ")
    Enstitute =  input("new id of Enstitute : ")
    insert = insert = 'INSERT INTO Enstitute VALUES(?,?)'
    data =(EnstituteID,Enstitute)
    result = cursor.execute(insert,data)
    cursor.commit()
    printEnstitute()

def insertAuthor():
    printAuthor()
    printUniversity()
    printEnstitute()
    AuthorID = input("new id of Author : ")
    AuthorUniversityID = input("new Authors University id : ")
    AuthorEnstituteID = input("new Authors Enstitute id : ")
    AuthorName = input("new Author name : ")
    AuthorSurname = input("new Author Surname : ")
    insert = insert = 'INSERT INTO Author VALUES(?,?,?,?,?)'
    data =(AuthorID,AuthorUniversityID,AuthorEnstituteID,AuthorName,AuthorSurname)
    result = cursor.execute(insert,data)
    cursor.commit()
    printAuthor()

def insertLanguage():
    printLanguage()
    LanguageID =  input("new id of language :")
    Language=  input("name of new language :")
    insert = 'INSERT INTO Language VALUES(?,?)'
    data = (LanguageID,Language)
    result = cursor.execute(insert,data)
    cursor.commit()
    printLanguage()

def insertType():
    printType()
    TypeID =  input("new id of Type :")
    Type=  input("name of new Type :")
    insert = 'INSERT INTO Type VALUES(?,?)'
    data = (TypeID,Type)
    result = cursor.execute(insert,data)
    cursor.commit()
    printType()

def insertSupervisor():
    printSupervisor()
    SupervisorID = input("new id of Supervisor")
    SupervisorName = input("new supervisor name : ")
    SupervisorSurname = input("new supervisor Surname : ")
    insert = 'INSERT INTO Supervisor VALUES(?,?,?)'
    data = (SupervisorID,SupervisorName,SupervisorSurname)
    result = cursor.execute(insert,data)
    cursor.commit()
    printSupervisor()

def insertCOSupervisor():
    printCOSupervisor()
    COSupervisorID = input("new id of Supervisor : ")
    COSupervisorName = input("new supervisor name : ")
    COSupervisorSurname = input("new supervisor Surname : ")
    insert = 'INSERT INTO COSupervisor VALUES(?,?,?)'
    data = (COSupervisorID,COSupervisorName,COSupervisorSurname)
    result = cursor.execute(insert,data)
    cursor.commit()
    printCOSupervisor()

def insertThesisHasCOSupervisor():
    printAuthor()
    printType()
    printLanguage()
    printSupervisor()
    printCOSupervisor()
    printThesis()
    ThesisID = input("new id of thesis : ")
    AuthorID = input("new thesis Author id :")
    TypeID = input("new thesis type id : ") 
    LanguageID = input("new thesis language id : ")
    SupervisorID = input("new thesis supervisor id : ")
    COSupervisorID = input("if have cosupervisor enter a id if you havent got press enter button : ")
    Tite = input("new thesis title :")
    Abstract = input("new thesis abstract :")
    Year = input("new thesis year :") 
    NumberOfPage = input("how many pages has new thesis : ")
    SubmissionDate = input("new thesis submission date like =>day.mounth.year : ")
    insert = 'INSERT INTO Thesis VALUES(?,?,?,?,?,?,?,?,?,?,?)'
    data = (ThesisID,AuthorID,TypeID,LanguageID,SupervisorID,COSupervisorID,Tite,Abstract,Year,NumberOfPage,SubmissionDate)
    result = cursor.execute(insert,data)
    cursor.commit()
    printThesis()

def insertThesisHasntCOSupervisor():
    printAuthor()
    printType()
    printLanguage()
    printSupervisor()
    printCOSupervisor()
    printThesis()
    ThesisID = input("new id of thesis : ")
    AuthorID = input("new thesis Author id :")
    TypeID = input("new thesis type id : ") 
    LanguageID = input("new thesis language id : ")
    SupervisorID = input("new thesis supervisor id : ")
    COSupervisorID = None
    Tite = input("new thesis title :")
    Abstract = input("new thesis abstract :")
    Year = input("new thesis year :") 
    NumberOfPage = input("how many pages has new thesis : ")
    SubmissionDate = input("new thesis submission date like =>day.mounth.year : ")
    result = cursor.execute('INSERT INTO Thesis VALUES(?,?,?,?,?,?,?,?,?,?,?)',(ThesisID,AuthorID,TypeID,LanguageID,SupervisorID,COSupervisorID,Tite,Abstract,Year,NumberOfPage,SubmissionDate))
    cursor.commit()

def joinAuthorTable():
    print("The table of contents is as follows: (AuthorID , UniversityName , EnstituteName, AuthorName , AuthorSurname)")
    print()
    result = cursor.execute('SELECT Author.AuthorID , University.UniversityName ,Enstitute.EnstituteName, Author.AuthorName, Author.AuthorSurname  FROM Author INNER JOIN University  ON Author.UniversityID = University.UniversityID INNER JOIN Enstitute ON Author.EnstituteID = Enstitute.EnstituteID ;')
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def joinThesisHasCOSupervisor():
    print("The table of contents is as follows :")
    print("ThesisID , AuthorName , AuthorSurname ,UniversityName , EnstituteName , Types , Languages , SupervisorName , SupervisorSurname , COSupervisorName , COSupervisorSurname , Title , Abstract , Year , NumberOfPage , SubmissionDate)")
    print()
    result = cursor.execute('{}'.format(queryCommand))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def joinThesisHasntCOSupervisor():
    print("The table of contents is as follows :")
    print("ThesisID , AuthorName , AuthorSurname ,UniversityName , EnstituteName , Types , Languages , SupervisorName , SupervisorSurname , Title , Abstract , Year , NumberOfPage , SubmissionDate)")
    print()
    result = cursor.execute('''SELECT Thesis.ThesisID,Author.AuthorName, Author.AuthorSurname, University.UniversityName , Enstitute.EnstituteName , Type.Types , Language.Languages , Supervisor.SupervisorName , Supervisor.SupervisorSurname , Thesis.Title ,  Thesis.Abstract,Thesis.Year,Thesis.NumberOfPages,Thesis.SubmissionDate
FROM Thesis
INNER JOIN Author on Thesis.AuthorID = Author.AuthorID
INNER JOIN University on Author.UniversityID = University.UniversityID
INNER JOIN Enstitute on Author.EnstituteID = Enstitute.EnstituteID
INNER JOIN Type on Thesis.TypeID = Type.TypeID
INNER JOIN Language on Thesis.LanguageID = Language.LanguageID
INNER JOIN Supervisor on Thesis.SupervisorID = Supervisor.SupervisorID;''')
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereName():
    name = input("Which name shall we search? \n")
    print()
    result = cursor.execute("{} WHERE AuthorName ='{}';".format(queryCommand,name))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereSurname():
    surname = input("Which Surname shall we search? \n")
    print()
    result = cursor.execute("{} WHERE AuthorSurname ='{}';".format(queryCommand,surname))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereUniversity():
    university = input("Which University shall we search? \n")
    print()
    result = cursor.execute("{} WHERE UniversityName ='{}';".format(queryCommand,university))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereEnstitute():
    enstitute = input("Which Enstitute shall we search? \n")
    print()
    result = cursor.execute("{} WHERE EnstituteName ='{}';".format(queryCommand,enstitute ))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereType():
    type = input("Which type of thesis shall we search? \n")
    print()
    result = cursor.execute("{} WHERE Types ='{}';".format(queryCommand,type))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereLanguage():
    language = input("Which language of thesis shall we search? \n")
    print()
    result = cursor.execute("{} WHERE LanguageName ='{}';".format(queryCommand,language))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereSupervisorName():
    supervisorName = input("Which supervisorName shall we search? \n")
    print()
    result = cursor.execute("{} WHERE SupervisorName ='{}';".format(queryCommand,supervisorName))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereSupervisorSurname():
    supervisorSurname = input("Which SupervisorSurname shall we search? \n")
    print()
    result = cursor.execute("{} WHERE SupervisorSurname ='{}';".format(queryCommand,supervisorSurname))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereCOSupervisorName():
    cosupervisorName = input("Which COSupervisorName shall we search? \n")
    print()
    result = cursor.execute("{} WHERE COSupervisorName ='{}';".format(queryCommand ,cosupervisorName))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereCOSupervisorSurname():
    cosupervisorSurname = input("Which COSupervisorSurname shall we search? \n")
    print()
    result = cursor.execute("{} WHERE COSupervisorSurname ='{}';".format(queryCommand,cosupervisorSurname))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereTitle():
    title = input("Which title shall we search? \n")
    print()
    result = cursor.execute("{} WHERE Title ='{}';".format(queryCommand,title))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereAbstract():
    abstract = input("Which Abstract shall we search? \n")
    print()
    result = cursor.execute("{} WHERE Abstract LIKE '{}%' ;".format(queryCommand,abstract))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereYear():
    year = input("Which year shall we search? \n")
    print()
    result = cursor.execute("{} WHERE Year ='{}';".format(queryCommand,year))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereNumberOfPage():
    numberOfPage = input("Which NumberOfPage shall we search? \n")
    print()
    result = cursor.execute("{} WHERE NumberOfPages ='{}';".format(queryCommand,numberOfPage))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

def whereSubmissionDate():
    submissionDate = input("Which SubmissionDate shall we search? like -> year.month.day \n")
    print()
    result = cursor.execute("{} WHERE SubmissionDate ='{}';".format(queryCommand,submissionDate))
    myresult = cursor.fetchall()
    cursor.commit()
    for row in myresult:
        print(row)
    print(str(cursor) + " data was update")

while True:
    print("""
1. print the tables
2. update the tables
3. add new data to tables
4. search the tables 
5. EXİT
    """)
    try:
        answer = int(input('Enter your selection (1/2/3/4/5) : '))
        if answer == 1 or answer == 2 or answer == 3 or answer == 4:
            if answer == 1:
                print("which table do you want to print \n")
                print("""
                1. print Universitys
                2. print Enstitutes
                3. print Authors
                4. print Languages
                5. print Types
                6. print Superviors
                7. print COSupervisors
                8. print Thesis
                9. print Author with datas
                10. print datas without co-supervisor in thesis table
                11. print All datas in Thesis table 
                """)
                try:
                    printAnswer = int(input('Enter your selection (1/2/3/4/5/6/7/8/9/10/11) :'))
                    if printAnswer == 1 or printAnswer == 2 or printAnswer == 3 or printAnswer == 4 or printAnswer == 5 or printAnswer == 6 or printAnswer == 7 or printAnswer == 8 or printAnswer == 9 or printAnswer == 10 or printAnswer == 11:
                        if printAnswer == 1:
                            printUniversity()
                        elif printAnswer == 2:
                            printEnstitute()
                        elif printAnswer == 3:
                            printAuthor()
                        elif printAnswer == 4:
                            printLanguage()
                        elif printAnswer == 5:
                            printType()
                        elif printAnswer == 6:
                            printSupervisor()
                        elif printAnswer == 7:
                            printCOSupervisor()
                        elif printAnswer == 8:
                            printThesis()
                        elif printAnswer == 9:
                            joinAuthorTable()
                        elif printAnswer == 10:
                            joinThesisHasntCOSupervisor()
                        elif printAnswer ==11:
                            joinThesisHasCOSupervisor()
                    else:
                        print('Please select one of this => (1/2/3/4/5/6/7/8/9/10/11)')
                except:
                    print('Please select one of this => (1/2/3/4/5/6/7/8/9/10/11)')
            elif answer == 2:
                print("which table do you want to update \n")
                print("""
                1. update University
                2. update Enstitute
                3. update Language
                4. update Type
                5. update supervisor name
                6. update supervisor surname
                7. update co-supervisor name
                8. update co-supervisor surname
                9. update author university
                10. update author ensitute
                11. update author name
                12. update author surname
                13. update thesis author
                14. update thesis type
                15. update thesis language
                16. update thesis supervisor
                17. update thesis co-supervisor
                18. update thesis title
                19. update thesis abstract
                20. update thesis year
                21. update thesis number of pages
                """)
                try:
                    updateAnswer = int(input('Enter your selection (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21) :'))
                    if updateAnswer == 1 or updateAnswer == 2 or updateAnswer == 3 or updateAnswer == 4 or updateAnswer == 5 or updateAnswer == 6 or updateAnswer == 7 or updateAnswer == 8 or updateAnswer == 9 or updateAnswer == 10 or updateAnswer == 11 or updateAnswer == 12 or updateAnswer == 13 or updateAnswer == 14 or updateAnswer == 15 or updateAnswer == 16 or updateAnswer == 17 or updateAnswer == 18 or updateAnswer == 19 or updateAnswer == 20 or updateAnswer == 21:
                        if updateAnswer == 1:
                            updateUniversity()
                        elif updateAnswer == 2:
                            updateEnstitute()
                        elif updateAnswer == 3:
                            updateLanguage
                        elif updateAnswer == 4:
                            updateTypes()
                        elif updateAnswer == 5:
                            updateSupervisorName()
                        elif updateAnswer == 6:
                            updateSupervisorSurname()
                        elif updateAnswer == 7:
                            updateCOSupervisorName()
                        elif updateAnswer == 8:
                            updateCOSupervisorSurname()
                        elif updateAnswer == 9:
                            updateAuthorUniversityID()
                        elif updateAnswer == 10:
                            updateAuthorEnstituteID()
                        elif updateAnswer == 11:
                            updateAuthorAuthorName()
                        elif updateAnswer == 12:
                            updateAuthorSurname()
                        elif updateAnswer == 13:
                            updateThesisAuthor()
                        elif updateAnswer == 14:
                            updateThesisType()
                        elif updateAnswer == 15:
                            updateThesisLanguage()
                        elif updateAnswer == 16:
                            updateThesisSupervisor()
                        elif updateAnswer == 17:
                            updateThesisCOSupervisor()
                        elif updateAnswer == 18:
                            updateThesisTitle()
                        elif updateAnswer == 19:
                            updateThesisAbstract()
                        elif updateAnswer == 20:
                            updateThesisYear()
                        elif updateAnswer == 21:
                            updateThesisNumberOfPages()
                    else:
                        print('please choose one of them => (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21) ')
                except:
                    print('please choose one of them => (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21) ')
            elif answer == 3:
                print("have you got a co-supervisor or not ? ")
                print("""
                1. YES
                2. NO 
                """)
                try:
                    choiceAnswer = int(input('enter your selection '))
                    if choiceAnswer == 1 or choiceAnswer == 2:
                        if choiceAnswer == 1:
                            print('Which table should we add new data ? \n')
                            print("""
                            1. add new data University
                            2. add new data Enstitute
                            3. add new data Author
                            4. add new data Language
                            5. add new data Type
                            6. add new data Supervisor
                            7. add new data co-supervisor
                            8. add new data to thesis
                            """)
                            try:
                                newDataAnswer = int(input('Enter your selection (1/2/3/4/5/6/7/8)'))
                                if newDataAnswer == 1 or newDataAnswer == 2 or newDataAnswer == 3 or newDataAnswer == 4 or newDataAnswer == 5 or newDataAnswer == 6 or newDataAnswer == 7 or newDataAnswer == 8 :
                                    if newDataAnswer == 1:
                                        insertUniversity()
                                    elif newDataAnswer == 2:
                                        insertEnstitute()
                                    elif newDataAnswer == 3:
                                        insertAuthor()
                                    elif newDataAnswer == 4:
                                        insertLanguage()
                                    elif newDataAnswer == 5:
                                        insertType()
                                    elif newDataAnswer == 6:
                                        insertSupervisor()
                                    elif newDataAnswer == 7:
                                        insertCOSupervisor()
                                    elif newDataAnswer == 8:
                                        insertThesisHasCOSupervisor()
                                else:
                                    print('please choose one of them => (1/2/3/4/5/6/7/8)')
                            except:
                                print('please choose one of them => (1/2/3/4/5/6/7/8)')
                        elif choiceAnswer == 2:
                            print('Which table should we add new data ? \n')
                            print("""
                            1. add new data University
                            2. add new data Enstitute
                            3. add new data Author
                            4. add new data Language
                            5. add new data Type
                            6. add new data Supervisor
                            7. add new data to thesis
                            """)
                            try:
                                newDataAnswerNoCOSupervisor = int(input('Enter your selection (1/2/3/4/5/6/7)'))
                                if newDataAnswerNoCOSupervisor == 1 or newDataAnswerNoCOSupervisor == 2 or newDataAnswerNoCOSupervisor == 3 or newDataAnswerNoCOSupervisor == 4 or newDataAnswerNoCOSupervisor == 5 or newDataAnswerNoCOSupervisor == 6 or newDataAnswerNoCOSupervisor == 7 :
                                    if newDataAnswerNoCOSupervisor == 1:
                                        insertUniversity()
                                    elif newDataAnswerNoCOSupervisor == 2:
                                        insertEnstitute()
                                    elif newDataAnswerNoCOSupervisor == 3:
                                        insertAuthor()
                                    elif newDataAnswerNoCOSupervisor == 4:
                                        insertLanguage()
                                    elif newDataAnswerNoCOSupervisor == 5:
                                        insertType()
                                    elif newDataAnswerNoCOSupervisor == 6:
                                        insertSupervisor()
                                    elif newDataAnswerNoCOSupervisor == 7:
                                        insertThesisHasntCOSupervisor()
                                else:
                                    print('please choose one of them => (1/2/3/4/5/6/7)')
                            except:
                                print('please choose one of them => (1/2/3/4/5/6/7)')
                    else:
                        print('please choose one of them => (1/2)')
                except:
                    print('please choose one of them => (1/2)')
            elif answer == 4:
                print("what are we looking for")
                print("""
                1. search for name
                2. search for surname
                3. search for university
                4. search for enstitute
                5. search for type
                6. search for language
                7. search for supervisor name
                8. search for supervisor surname
                9. search for co-supervisor name
                10. search for co-supervisor surname
                11. search for title
                12. search for abstract
                13. search for year
                14. search for number of page
                15. search for submission date
                """)
                try:
                    search = int(input('Enter your selection (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15)'))
                    if search == 1 or search == 2 or search == 3 or search == 4 or search == 5 or search == 6 or search == 7 or search == 8 or search == 9 or search == 10 or search == 11 or search == 12 or search == 13 or search == 14 or search == 15 :
                        if search == 1:
                            whereName()
                        elif search == 2:
                            whereSurname()
                        elif search == 3:
                            whereUniversity()
                        elif search == 4:
                            whereEnstitute()
                        elif search == 5:
                            whereType()
                        elif search == 6:
                            whereLanguage()
                        elif search == 7:
                            whereSupervisorName()
                        elif search == 8:
                            whereSupervisorSurname()
                        elif search == 9:
                            whereCOSupervisorName()
                        elif search == 10:
                            whereCOSupervisorSurname()
                        elif search == 11:
                            whereTitle()
                        elif search == 12:
                            whereAbstract()
                        elif search == 13:
                            whereYear()
                        elif search == 14:
                            whereNumberOfPage()
                        elif search == 15:
                            whereSubmissionDate()
                except:
                    print('please choose one of them => (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15)')
            else:
                print('Please select 1 or 2 or 3 or 4')
        elif answer == 5:
            break
        else:
            print('Please select 1 or 2 or 3 or 4 or 5')
    except:
        print('Please select 1 or 2 or 3 or 4 or 5')
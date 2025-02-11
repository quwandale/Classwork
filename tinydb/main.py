from tinydb import TinyDB, Query

db = TinyDB("students.json")
User = Query()

def addRecord():
#adding record
    name = input("Enter your name: ")
    grade =input("Enter your grade: ")
    db.insert({"Name" : name, "Grade" : grade})

def searchRecord():
#searching for record
    studentSearch = input("enter name: ")
    student=db.search(User.Name == studentSearch)
    print(student)

def showAll():
    #show all records
    for item in db:
        print(item)

while True:
    menu == input(""" Choose an option
                  1. Add a record
                  2. Seach for a record
                  3. Show all records
                  """)
    if menu == "1":
        addRecord()
    elif menu == "2":
        searchRecord()
    elif menu == "3":
        showAll()
    elif menu == "END":
        print("Thank you for using the database.")
        break
    else:
        print("There is no such option")
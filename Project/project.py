# Medical Database Using Python and CSV

## Libraries Used
from tabulate import tabulate  ## displays database
from datetime import date  ## calculates age
from sys import exit  ## exits 
import csv  ## exports database into csv file

print("", end = "\n") ## prints an extra line for aesthetic purposes

## ensures that database doesn't return to default settings when programme is rerun
with open('database.csv') as d:
    reader = csv.reader(d)
    data = list(reader)

database = []
database.extend(data)

## prints a person's details on request (used in search function)
def printPerson(lst: list):
    print(f"Name: {lst[0]}")
    print(f"Date of Birth: {lst[1]}")
    print(f"Age: {lst[2]}")
    print(f"Telephone Number: {lst[3]}")

## works with printPerson()c to find the person's details so they can be printed
def printRow(person: str):
    for lst in database:
        if person in lst:
            printPerson(lst)

## adds new data to the database
def write(database: list):
    name = input("Enter Name: ")
    duplicate = False

    for lst in database:
        if name in lst:
            print("Duplicate entry detected. Patient already in database.")
            duplicate = True

    if duplicate == False:
        birthday = input("Enter Date of Birth: ")
        number = input("Enter Telephone Number: ")
        
        ## accepts several kinds of user input for date of birth (".", "/", "-", and no delimiter)
        ## note: programmed to UK date system (day-month-year)
        if "." in birthday:
            day, month, y = birthday.split(".")
            if len(y) == 2:
                if int(y) > int(str(date.today().year)[2:]):
                    year = "19" + y
                else:
                    year = "20" + y
            else:
                year = y
        elif "-" in birthday:
            day, month, y = birthday.split("-")
            if len(y) == 2:
                if int(y) > int(str(date.today().year)[2:]):
                    year = "19" + y
                else:
                    year = "20" + y
            else:
                year = y
        elif "/" in birthday:
            day, month, y = birthday.split("/")
            if len(y) == 2:
                if int(y) > int(str(date.today().year)[2:]):
                    year = "19" + y
                else:
                    year = "20" + y
            else:
                year = y
        elif len(birthday) == 6 or len(birthday) == 8:
            day = birthday[0:2]
            month = birthday[2:4]
            y = birthday [4:-1]

            if len(y) == 2:
                if int(y) > int(str(date.today().year)[2:]):
                    year = "19" + y
                else:
                    year = "20" + y
            else:
                year = y
        else:
            print("Unsupported date format.")

        birthdayNew = f"{day}-{month}-{year}"

        age = date.today().year - int(year)  ## calculate user age (roughly, only based on year of birth not day or month)
    
        lstNew = [name, birthdayNew, age, number]  ## creates the new database entry
        database.append(lstNew)  ## adds this new entry to the database
        print("Database has been updated.")

## edits data already in the database
def edit(database: list):
    name = input("Whose data would you like to edit? ")  ## accepts user input
    for lst in database:  ## finds data in database
        try:
            ## changes either name, date of birth or telephone number of specified input (not age which is automatically calculated)
            if name in lst:
                printRow(name)  ## displays original data (pre-change)
                secondChoice = input("Enter n to change patient's name, d for birthday, or t for telephone number: ")
                secondChoice = secondChoice.strip().lower()

                if secondChoice == "n":  ## changes name
                    newName = input("Enter the new name: ")
                    for lst in database:
                        if name in lst:
                            lst[0] = newName

                elif secondChoice == "d":  ## changes date of birth 
                    ## code borrowed from write() function ** possible improvement - make a function instead of copypasting **
                    birthday = input("Enter the new date of birth: ")
                    if "." in birthday:
                        day, month, y = birthday.split(".")
                        if len(y) == 2:
                            if int(y) > date.today().year:
                                year = "19" + y
                            else:
                                year = "20" + y
                        else:
                            year = y
                    elif "-" in birthday:
                        day, month, y = birthday.split("-")
                        if len(y) == 2:
                            if int(y) > date.today().year:
                                year = "19" + y
                            else:
                                year = "20" + y
                        else:
                            year = y
                    elif "/" in birthday:
                        day, month, y = birthday.split("/")
                        if len(y) == 2:
                            if int(y) > date.today().year:
                                year = "19" + y
                            else:
                                year = "20" + y
                        else:
                            year = y
                    elif len(birthday) == 6 or len(birthday) == 8:
                        day = birthday[0:2]
                        month = birthday[2:4]
                        y = birthday [4:-1]

                        if len(y) == 2:
                            if int(y) > date.today().year:
                                year = "19" + y
                            else:
                                year = "20" + y
                        else:
                            year = y
                    else:
                        print("Unsupported date format.")

                    birthdayNew = f"{day}-{month}-{year}"
                    age = date.today().year - int(year) 

                    for lst in database:
                        if name in lst:
                            lst[1] = birthdayNew
                            lst[2] = age
                            
                elif secondChoice == "t":  ## changes telephone number
                    newNumber = input("Enter the new telephone number: ")
                    for lst in database:
                        if name in lst:
                            lst[3] = newNumber
                print("Database has been updated.")
        except:
            print("User not found.")  ## if name not in database, print error message

## prints database using tabulate library
def view(database: list):
    print(tabulate(database, headers="firstrow", tablefmt="grid"))  ## uses tabulate to output database

## exports database to a csv file (database.csv)
def export(database: list):
    with open("database.csv", "w") as CSVFile:
        w = csv.writer(CSVFile)
        w.writerows(database)
    
    print("Database exported as database.csv")

## searches the database by name, birthday, or telephone number and displays all the data of user, if found
def search(database: list):
    fourthChoice = input("Enter n to search by name, d for birthday, or t for telephone number: ")  ## accepts user input
    fourthChoice = fourthChoice.strip().lower()
    if fourthChoice == "n":  ## searches by name
        name = input("Which name would you like to search: ")
        print("Searching...")
        print()
        for lst in database:
            try:
                if name in lst:
                    printRow(name)
            except:
                print("User not found") 
    elif fourthChoice == "d":  ## searches by date of birth
        birthday = input("Which birthday would you like to search (dd-mm-yyyy): ")
        birthday = birthday.strip()
        print("Searching...")
        print()
        for lst in database:
            try:
                if birthday in lst:
                    printRow(birthday)
            except:
                print("User not found")
    elif fourthChoice == "t":  ## searches by telephone number
        number = input("Which telephone number would you like to search: ")
        number = number.strip()
        print("Searching...")
        print()
        for lst in database:
            try:
                if number in lst:
                    printRow(name)
            except:
                print("User not found")  

## deletes user data, if administrator access is proven (password is 123456)
def delete(database: list):
    admin = input("WARNING: Deleting requires administrator access. Enter the password (6 digits): ")
    admin = int(admin.strip())
    if admin == 123456:  ## checks for admin access
        name = input("Whose data would you like to delete? ")
        for lst in database:
            if name in lst:
                database.remove(lst)
    else:
        print("Password incorrect.")  

## gives user choice of quitting program or performing more tasks
def thirdChoice(choice: str):
    if choice.strip().lower() == "c":
        main(database)
    elif choice.strip().lower() == "q":
        quit()
    else:
        thirdChoice(input("""To continue press c, to quit press q. Before quitting, ensure that you have 
pressed x to export, to make sure your database is saved. """))

## quits program
def quit():
    exit(1)

## master function, runs other functions and provides intro screen for user
def main(database):
    ## allows user to choose function: write, edit, view, export, search, or delete
    print("""Enter w to add to your database, e to edit details, v to view the full database, x to export it or s to search. 
If you have admin access, you can delete by pressing d.""")
    print()
    firstChoice = input("Enter: ")
    firstChoice = firstChoice.strip().lower()
    if firstChoice == "w":
        write(database)
        thirdChoice(input("""To continue press c, to quit press q. Before quitting, ensure that you have 
pressed x to export, to make sure your database is saved. """))

    elif firstChoice == "e":
        edit(database)
        thirdChoice(input("""To continue press c, to quit press q. Before quitting, ensure that you have 
pressed x to export, to make sure your database is saved. """))

    elif firstChoice == "v":
        view(database)
        thirdChoice(input("""To continue press c, to quit press q. Before quitting, ensure that you have 
pressed x to export, to make sure your database is saved. """))

    elif firstChoice == "x":
        export(database)
        thirdChoice(input("""To continue press c, to quit press q. Before quitting, ensure that you have 
pressed x to export, to make sure your database is saved. """))

    elif firstChoice == "s":
        search(database)
        thirdChoice(input("""To continue press c, to quit press q. Before quitting, ensure that you have 
pressed x to export, to make sure your database is saved. """))

    elif firstChoice == "d":
        delete(database)
        thirdChoice(input("""To continue press c, to quit press q. Before quitting, ensure that you have 
pressed x to export, to make sure your database is saved. """))

    else:
        print("Unrecognised. Please try again.")
        main(database)
        
if __name__ == "__main__":
    main(database)  ## runs main function

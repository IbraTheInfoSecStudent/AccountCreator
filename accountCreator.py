# Author: Ibrahim Girowal
# Description: Account creator program. Users can create accounts and save them to a file.
# Accounts from files can be retrieved. Save files can be deleted. Account details can be viewed.

# Required modules
import pickle, os, glob, openpyxl


# Creating a class Account. Each account the user creates is an object of this class
class Account:
    def __init__(self, fullname, username, password):
        self.fullname = fullname
        # Username is the unique value
        self.username = username
        self.password = password

    def getUserInfo(self):
        print(f"Full Name: {self.fullname.title()}\nUsername: {self.username}\nPassword: {self.password}")


class UserInfo:
    def __init__(self, favProg, carOwned, favFood):
        self.favProg = favProg
        self.carOwned = carOwned
        self.favFood = favFood

    def getUserInfo(self):
        print(f"Favourite Language: {self.favProg.title()}\nCar Owned: {self.carOwned}\nFavourite Food: {self.favFood}")

    def getFavProg(self):
        return self.favProg

    def getCar(self):
        return self.carOwned

    def getFavFood(self):
        return self.favFood

# This function creates accounts. Requires user to input their name, desired username, and desired password
def createAccount():
    name = input('Enter your full name: ')
    username = input('Enter a username of your choice: ')
    password = input('Enter a password of your choice: ')

    # Checks if the username the user chose is already chosen. If it is, it forces the user to choose another username
    if username in accountDictionary.keys():
        print('That username is taken. Chose another')
        createAccount()
        # If the username is unique, the information is added to a dictionary. The key is the username, and the value
    # that corresponds to that key is an object of the class Account
    else:
        accountDictionary[username] = Account(name, username, password)
        print('User successfully added!')


# This functions displays existing accounts
def displayAccounts():
    # If there is ever a case where the dictionary is empty, that means there are no existing accounts
    if len(accountDictionary) == 0:
        print('There are no existing accounts')
        # Displays usernames of all accounts
    else:
        print('Existing accounts:')
        for keys in accountDictionary.keys():
            print('\t' + keys)


# This function displays all data for a chosen account
def displayData():
    print('\nFor which account do you want to see the data?')
    # Displays each username so the user can pick which account they want to view information for
    for keys in accountDictionary.keys():
        print('\t' + keys)
    user = input('\nEnter account name: ')
    if user in accountDictionary.keys():
        # Loops through the entire dictionary, but only prints data once it finds the username the user chose
        for key, value in accountDictionary.items():
            if user == key:
                # Calls the method defined in the class Account
                value.getUserInfo()
            elif user != key:
                continue
    else:
        print('That user does not exist')


# This method will save the current accounts to a file
# It uses methods from the os and pickle modules
# Future additions to this function:
#   1. More input validation to prevent the user from writing to and overwriting a file that is not a save file
def writeToFile(dictionary):
    print('Current account save files: ')
    # Prints all files in the current directory that contain a .txt extension
    files = [f for f in os.listdir('.') if '.txt' in f]
    for f in files:
        print(f)

    filechoice = input('\nWhich file should the accounts be saved to?\nIt can be one of the above files, or a new one.'
                       '\nCAUTION: Existing files will be overwritten.\tChoose file: ')
    # It does not matter if the user includes the .txt in what they input
    if '.txt' in filechoice:
        filename = filechoice
    else:
        filename = (filechoice + '.txt')

    with open(filename, 'wb') as f:
        # Uses pickle's dump() function to put all accounts from the dictionary into the save file
        # If save file does not exist, it creates a new file automatically
        pickle.dump(dictionary, f)
    print('Saved to a file')


# This function will restore/retrieve from a save file to continue where you left off
def retrieveFromFile():
    print('List of account save files:')
    # Uses same code as above to print off save files
    files = [f for f in os.listdir('.') if '.txt' in f]
    for f in files:
        print(f)

    filechoice = input('\nWhich file do you want to retrieve accounts from? ')
    if '.txt' in filechoice:
        filename = filechoice
    else:
        filename = (filechoice + '.txt')

    # Try and except block in order to catch the FileNotFoundError
    try:
        with open(filename, 'rb') as f:
            # Uses pickle's load() function to retrieve data from the file
            dictionary = pickle.load(f)
        return dictionary
    except FileNotFoundError:
        print('That file does not exist\n')
        retrieveFromFile()


# This function allows the user to delete any save files
# Future additions:
#   1. Since there may be .txt files present that are not save files, the program should prevent the user from deleting those
def deleteSaveFile():
    print('List of account save files:')
    files = [f for f in os.listdir('.') if '.txt' in f]
    for f in files:
        print(f)
    filechoice = input('\nWhich save file do you want to delete? ')
    # Checks to see if the file is a .txt file (since only .txt files are present in the files list)
    if filechoice in files:
        os.remove(filechoice)
        print('Save file deleted!')
    else:
        print('That file does not exist')

# This function allows the user to view save files and their sizes, and gives a total size.
# File retrieval is done using glob() instead of the regular list comprehension done in previous functions
def saveFileTotalSize():
    print('List of account save file sizes:\n')
    totalSize = 0
    for f in glob.glob('*.txt'):
        print(f + ' | ' + str(os.path.getsize(f)) + ' bytes')
        totalSize += os.path.getsize(f)
    print('-------')
    print('Total size: ' + str(totalSize) + ' bytes')


def addUserInfo():
    print('\nFor which account do you want to add data?')
    # Displays each username so the user can pick which account they want to view information for
    for keys in accountDictionary.keys():
        print('\t' + keys)
    user = input('\nEnter account name: ')
    if user in accountDictionary.keys():
        favProg = input('Favourite programming language: ')
        car = input('Car owned: ')
        favFood = input('Favourite food: ')
        userInfoDictionary[user] = UserInfo(favProg, car, favFood)
        print('Data successfully added!')
    else:
        print('That user does not exist')


def viewUserData():
    print('\nFor which account do you want to add data?')
    # Displays each username so the user can pick which account they want to view information for
    for keys in accountDictionary.keys():
        print('\t' + keys)
    user = input('\nEnter account name: ')
    if user in userInfoDictionary:
        for key, value in userInfoDictionary.items():
            if user == key:
                value.getUserInfo()


def saveUserInfo(dictionary):
    print('Current account save files: ')
    # Prints all files in the current directory that contain a .txt extension
    files = [f for f in os.listdir('.') if '.txt' in f]
    for f in files:
        print(f)

    filechoice = input('\nWhich file should the accounts be saved to?\nIt can be one of the above files, or a new one.'
                       '\nCAUTION: Existing files will be overwritten.\tChoose file: ')
    # It does not matter if the user includes the .txt in what they input
    if '.txt' in filechoice:
        filename = filechoice
    else:
        filename = (filechoice + '.txt')

    with open(filename, 'wb') as f:
        # Uses pickle's dump() function to put all accounts from the dictionary into the save file
        # If save file does not exist, it creates a new file automatically
        pickle.dump(dictionary, f)
    print('Saved to a file')


def retrieveUserDataFromFile():
    print('List of data save files:')
    files = [f for f in os.listdir('.') if '.txt' in f]
    for f in files:
        print(f)

    filechoice = input('\nWhich file do you want to retrieve accounts from? ')
    if '.txt' in filechoice:
        filename = filechoice
    else:
        filename = (filechoice + '.txt')

    # Try and except block in order to catch the FileNotFoundError
    try:
        with open(filename, 'rb') as f:
            # Uses pickle's load() function to retrieve data from the file
            dictionary = pickle.load(f)
        return dictionary
    except FileNotFoundError:
        print('That file does not exist\n')
        retrieveFromFile()


def exportToExcel():
    name = input('Choose a file name: ')
    if '.xlsx' not in name:
        name = name+'.xlsx'
    excel = openpyxl.Workbook()
    sheet = excel['Sheet']
    sheet.title = 'User data'
    sheet = excel['User data']
    sheet['A1'] = 'Username'
    sheet['B1'] = 'Fav prog lang'
    sheet['C1'] = 'Car owned'
    sheet['D1'] = 'Fav food'
    c = 2
    for key, value in userInfoDictionary.items():
        sheet['A' + str(c)] = key
        sheet['B' + str(c)] = value.getFavProg()
        sheet['C' + str(c)] = value.getCar()
        sheet['D' + str(c)] = value.getFavFood()
        c += 1
    excel.save(name)
    print('Exporting to excel complete: ' + name)


# Dictionary where accounts are saved
accountDictionary = {}
userInfoDictionary = {}

# The start of the main program
print('Welcome to the Account & Data Management Portal!')
# A while loop to control the entire program flow and menu
while True:
    print('\n*** Account Management ***')
    print('\t1. Create a new account')
    print('\t2. View a list of existing accounts')
    print('\t3. View account information for a specific account')
    print('\t4. Save accounts to a file')
    print('\t5. Retrieve accounts from a specific file')
    print('\t6. Delete an account save file')
    print('\t7. View save file sizes')
    print('\t8. Quit\n')
    print('*** Data Management ***')
    print('\t9. Add user data')
    print('\t10. View user data')
    print('\t11. Save user data to a file')
    print('\t12. Retrieve user data from a file')
    print('\t13. Export data to excel file (.xlsx)')
    print('\t14. Export statistics as a text file')

    # Based on user input, call the appropriate function
    choice = input()
    if choice == '1':
        createAccount()
    elif choice == '2':
        displayAccounts()
    elif choice == '3':
        displayData()
    elif choice == '4':
        writeToFile(accountDictionary)
    elif choice == '5':
        # The logic behind the next few lines is as follows:
        # In a scenario where the user has created an account(s), and they desire to retrieve accounts from a save file,
        # the program would have erased all created accounts and replaced the existing dictionary with the dictionary returned
        # by the retrieveFromFile() dictictionary. In order to prevent this, I created a tempDictionary to place the dictionary
        # returned by the function, and then update the current dictionary with the dictionary from the save file. In other
        # words, I basically merged the 2 dictionaries
        tempDictionary = {}
        tempDictionary = retrieveFromFile()
        accountDictionary.update(tempDictionary)
        print('Accounts retrieved')
    elif choice == '6':
        deleteSaveFile()
    elif choice == '7':
        saveFileTotalSize()
    elif choice == '8':
        print('Goodbye!')
        break
    elif choice == '9':
        addUserInfo()
    elif choice == '10':
        viewUserData()
    elif choice == '11':
        saveUserInfo(userInfoDictionary)
    elif choice == '12':
        temp1Dictionary = {}
        temp1Dictionary = retrieveUserDataFromFile()
        userInfoDictionary.update(temp1Dictionary)
    elif choice == '13':
        exportToExcel()
    else:
        print('That option does not exist. Try again')

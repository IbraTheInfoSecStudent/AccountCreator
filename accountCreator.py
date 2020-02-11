# Author: Ibrahim Girowal
# Description: Account creator program. Users can create accounts and save them to a file.
# Accounts from files can be retrieved. Save files can be deleted. Account details can be viewed.

import pickle
import os


class Account:
    def __init__(self, fullname, username, password):
        self.fullname = fullname
        # username is the unique value
        self.username = username
        self.password = password

    def getUserInfo(self):
        print(f"full Name: {self.fullname.title()}\nUsername: {self.username}\nPassword: {self.password}")


active = True
accountDictionary = {}


def createAccount():
    name = input('Enter your full name: ')
    username = input('Enter a username of your choice: ')
    password = input('Enter a password of your choice: ')
    if username in accountDictionary.keys():
        print('That username is taken. Chose another')
        createAccount()
    else:
        accountDictionary[username] = Account(name, username, password)
        print('User successfully added!')


def displayAccounts():
    if len(accountDictionary) == 0:
        print('There are no existing accounts')
    else:
        print('Existing accounts:')
        for keys in accountDictionary.keys():
            print('\t' + keys)


def displayData():
    print('\nFor which account do you want to see the data?')
    for keys in accountDictionary.keys():
        print('\t' + keys)
    user = input('\nEnter account name: ')
    if user in accountDictionary.keys():
        for key, value in accountDictionary.items():
            if user == key:
                print(value.getUserInfo())
            elif user != key:
                continue
    else:
        print('That user does not exist')


def writeToFile(dictionary):
    print('Current account save files: ')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if '.txt' in f:
            print('\t' + f)
        else:
            continue

    filechoice = input('\nWhich file should the accounts be saved to?\nIt can be one of the above files, or a new one.'
                       '\nCAUTION: Existing files will be overwritten.\tChoose file: ')
    if '.txt' in filechoice:
        filename = filechoice
    else:
        filename = (filechoice + '.txt')
    with open(filename, 'wb') as f:
        pickle.dump(dictionary, f)
    print('Saved to a file')


def retrieveFromFile():
    print('List of account save files:')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if '.txt' in f:
            print('\t' + f)
        else:
            continue
    filechoice = input('\nWhich file do you want to retrieve accounts from? ')
    if '.txt' in filechoice:
        filename = filechoice
    else:
        filename = (filechoice + '.txt')
    try:
        with open(filename, 'rb') as f:
            dictionary = pickle.load(f)
        return dictionary
    except FileNotFoundError:
        print('That file does not exist\n')
        retrieveFromFile()


def deleteSaveFile():
    print('List of account save files:')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if '.txt' in f:
            print('\t' + f)
        else:
            continue
    filechoice = input('\nWhich save file do you want to delete? ')
    if filechoice in files:
        os.remove(filechoice)
        print('Save file deleted!')
    else:
        print('That file does not exist')


print('Welcome to the Account Creation Portal!')
while active:
    # while loop is for the menu
    # create functions for each option
    print('\nWhat would you like to do?')
    print('\t1. Create a new account')
    print('\t2. View a list of existing accounts')
    print('\t3. View all information for a specific account')
    print('\t4. Save accounts to a file')
    print('\t5. Retrieve accounts from a specific file')
    print('\t6. Delete an account save file')
    print('\t7. Quit')
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
        tempDictionary = {}
        tempDictionary = retrieveFromFile()
        accountDictionary.update(tempDictionary)
        print('Accounts retrieved')
    elif choice == '6':
        deleteSaveFile()
    elif choice == '7':
        print('Goodbye!')
        break
    else:
        print('That option does not exist. Try again')

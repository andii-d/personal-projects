"""
Task 5 : Password Reminder

Skills Required:
Using variables, operators, inputs, outputs and assignments
Using sequences, selection and iteration
Using count controlled loops (for) and condition controlled loops (while)
Using different types of data, i.e. integer, string, float and Boolean
Basic string manipulation
Basic file handling operations
Using lists
Using subroutines

People often struggle to remember their passwords for different accounts. One potential solution is to store the
passwords on your computer securely, using an encryption algorithm.

A relatively straightforward encryption algorithm is the Caesar Cipher. This cipher works by shifting each letter by
a number of characters. E.g. if the shift is 3 then a becomes d, b becomes e, etc.

The finished program should allow a user to enter an account, username and password. The password should be encrypted
using a Caesar Cipher that uses the length of the password as the key (i.e. if a password is 5 letters long,
the key will be 5). The account, username and encrypted password should then be saved to a file or files.

The program should also allow the user to recover their password by entering the account and username. The program
should then decrypt and display the password to the user.

Analyse the requirements for this system and design, develop, test and evaluate a program to help users store their
passwords securely.

Extension

At the moment it would be easy for someone else to gain access to the password by examining the text file and
entering the account and username to get the password. To make the program more secure, encrypt the account and
username as well.

Further Extension 

Implement a self-destruct sequence. If someone enters a password incorrectly 3 times in a row then the data file
should be deleted. Closing the program and re-running it should not reset the number of incorrect attempts.

"""

import string
import time

# Holds all the accounts within a class dictionary
allAccounts = {}

class Account:
    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

def encryption(password):
    encrypt_pw = password
    # Shifts the password by the length of itself
    shift = len(password)
    # Gets the string of ascii letters
    alphabet = string.ascii_letters
    # Shifts the ascii letters by the number given
    shifted = alphabet[shift:] + alphabet[:shift]
    # Makes a translation of the ascii alphabet to apply to the password
    table = str.maketrans(alphabet, shifted)
    # Applies the translated alphabet to the password
    encrypted = encrypt_pw.translate(table)

    return encrypted, shift

def save_account(account, username, encrypted_password):
    with open('database.txt', 'a') as f:
        f.write(f"{account}:{username}:{encrypted_password}\n")

def load_accounts():
    accounts = {}
    with open('database.txt') as file:
        for line in file:
            # Strips the line of any new lines
            line = line.rstrip()
            # Splits the line by a : and assigns it into the corresponding variables
            account, username, password = line.split(':')
            # Initializes the Account object
            newAccount = Account(account, username, password)
            # Add the account object to the dictionary
            accounts[account] = newAccount
    return accounts

def register():
    print('\nWelcome to the registration page.')

    # Setting the user's new account with their sign-in credentials
    while True:
        account = input('\nPlease create an account name: ')
        if account == '' or account in allAccounts:
            print('The account already exists or has an invalid name. Please re-enter a new name.\n')
            continue

        username = input('\nPlease create a username: ')
        if username == '' or username in allAccounts:
            print('The username is already taken or is invalid. Please choose another username.\n')
            continue

        password = input('\nPlease create a password: ')

        if password == '':
            print('Please re-enter a valid password.')
        else:
            encrypted_password, shift = encryption(password)

            with open('database.txt', 'a') as f:
                f.write(f"{account}:{username}:{encrypted_password}:{shift}\n")
                print('\nYour credentials have been encrypted and saved.\n')
                break

def login():
    print('\nWelcome to the login page.')

    while True:
        # Ask the user to enter their credentials
        account = input('\nPlease enter your account: ')
        if account in allAccounts:
            username = input('\nPlease enter your username: ')
            if username == allAccounts[account].username:
                encrypted_password = allAccounts[account].password
                shift = int(allAccounts[account].shift)  # Retrieve the shift from the account object
                # Decrypt the password using shift
                decrypted_password = decrypt(encrypted_password, shift)
                print(f'\nAccount accessed. Your password is: {decrypted_password}')
                break
            else:
                print('Please re-enter a correct username.')
                continue
        else:
            print('Please re-enter a correct account name.')
            continue

def decrypt(encrypted_password, shift):
    alphabet = string.ascii_letters
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(shifted, alphabet)
    decrypted = encrypted_password.translate(table)
    return decrypted

def menu():
    print('\nWelcome to your personal password reminder!\n'
          '\n1. Enter your account, username, and password'
          '\n2. Recover your account'
          '\n3. Quit\n')

    while True:
        try:
            mainmenu = int(input('Please enter an option: '))

        except ValueError:
            print('Please enter an integer.')
            continue

        else:
            if mainmenu == 1:
                register()

            elif mainmenu == 2:
                login()

            elif mainmenu == 3:
                print('Quitting.', end=''), time.sleep(0.5)
                print('.', end=''), time.sleep(0.5)
                print('.')
                quit()

# Load accounts from the database file
with open('database.txt') as file:
    for line in file:
        # Strips the line of any new lines
        line = line.rstrip()
        # Splits the line by a : and assigns it into the corresponding variables
        account, username, encrypted_password, shift = line.split(':')
        # Initializes the Account object
        newAccount = Account(account, username, encrypted_password, shift)
        # Add the account object to the dictionary
        allAccounts[account] = newAccount

menu()

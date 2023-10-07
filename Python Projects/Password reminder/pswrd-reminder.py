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
from cryptography.fernet import Fernet


# opening the key
with open('Python Projects\\Password reminder\\filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('Python Projects\Password reminder\databaseReminder.txt', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and 
# writing the encrypted data
with open('Python Projects\Password reminder\databaseReminder.txt', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)

# decryption below

# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('Python Projects\Password reminder\databaseReminder.txt', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('Python Projects\Password reminder\databaseReminder.txt', 'wb') as dec_file:
	dec_file.write(decrypted)



# Holds all the accounts within a class dictionary
allAccounts = {}

class Account:
    # Make an initialiser that stores all the details of the accounts
    def __init__(self, account, username, password, shift):
        self.account = account
        self.username = username
        self.password = password
        self.shift = shift  # Store the shift value in the Account object

def encryption(password):
    # Turn the password given in the resigter function into a placeholder variable
    encrypt_pw = password
    # Get the length of the password to shift it by the length of itself
    shift = len(password)
    # Gets the ascii letters into a string variable
    alphabet = string.ascii_letters
    # Slices alphabet starting from the shift, to the end (represents the forward shifted alphabet)
    # [:shift] takes a slice of alphabet from the beginning, to the end of shift position (represents the wrapping around)
    # 'shifted' combines these two slices to create a new alphabet where letters are shifted according to the value of shift.
    # i.e. if shift is 3, output is "defghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc"
    shifted = alphabet[shift:] + alphabet[:shift]
    # Makes an available translation of the ciphered alphabet
    table = str.maketrans(alphabet, shifted)
    # Translates the password along the ciphered one, by mapping each letter to another i.e. if shift is 3, a will become d, etc
    encrypted = encrypt_pw.translate(table)
    return encrypted, shift

def save_account(account, username, encrypted_password, shift):
    with open('Python Projects\Password reminder\databaseReminder.txt', 'a') as f:
        # Write the details of the account and its password to the file 
        f.write(f"{account}:{username}:{encrypted_password}:{shift}\n")

def load_accounts():
    accounts = {}
    with open('Python Projects\Password reminder\databaseReminder.txt') as file:
        for line in file:
            # Strips the line of any new lines
            line = line.rstrip()
            # Splits the line by a : and assigns it into the corresponding variables
            account, username, encrypted_password, shift = line.split(':')
            # Initializes the Account object
            newAccount = Account(account, username, encrypted_password, shift)
            # Add the account object to the dictionary
            accounts[account] = newAccount
    return accounts

def register():
    print('\nWelcome to the registration page.')

    accLife = 3
    usrLife = 3
    
    # Setting the user's new account with their sign-in credentials
    while True:
        account = input('\nPlease create an account name: ')
        if account == '' or account in allAccounts:
            print('\nThe account already exists or has an invalid name. Please re-enter a new name.\n'), time.sleep(0.7)
            accLife -= 1
            if accLife <= 0:
                print('You have attempted too many times to enter your account. Back to home menu...'), time.sleep(0.7)
                accLife = 3
                menu()
            else:
                continue
        
        if accLife <= 0:
            print('You have attempted too many times to enter your account. Back to home menu...'), time.sleep(0.7)
            accLife = 3
            menu()
        
        username = input('\nPlease create a username: ')
        if username == '' or username in allAccounts:
            print('\nThe username is already taken or is invalid. Please choose another username.\n'), time.sleep(0.7)
            usrLife -= 1
            if usrLife == 0:
                print('You have attempted too many times to enter your username. Back to home menu...'), time.sleep(0.7)
                usrLife = 3
                menu()
            else:
                continue
         
        if usrLife == 0:
            print('You have attempted too many times to enter your username. Back to home menu...'), time.sleep(0.7)
            usrLife = 3
            menu()

        password = input('\nPlease create a password: ')

        if password == '':
            print('Please re-enter a valid password.'), time.sleep(0.7)
        else:
            encrypted_password, shift = encryption(password)

            with open('Python Projects\Password reminder\databaseReminder.txt', 'a') as f:
                f.write(f"{account}:{username}:{encrypted_password}:{shift}\n")
                print('\nYour credentials have been encrypted and saved.\n')
                menu()

def login():
    print('\nWelcome to the login page.')

    while True:
        # Ask the user to enter their credentials
        account = input('\nPlease enter your account: ')
        if account in allAccounts:
            username = input('\nPlease enter your username: ')
            if username == allAccounts[account].username:
                # Check if the entered username matches the account
                encrypted_password = allAccounts[account].password
                # Retrieve the encrypted password associated with the specified account
                shift = int(allAccounts[account].shift)  # Retrieve the shift from the account object
                # Decrypt the password using shift, in the file
                decrypted_password = decrypt(encrypted_password, shift)
                print(f'\nAccount accessed. Your password is: {decrypted_password}'), time.sleep(1)
                menu()
            else:
                print('Please re-enter a correct username.'), time.sleep(0.7)
                continue
        else:
            print('Please re-enter a correct account name.'), time.sleep(0.7)
            continue

# Take the encrypted password and the shift as parameters
def decrypt(encrypted_password, shift):
    # Get the string of the ascii letters, a-zA-Z
    alphabet = string.ascii_letters
    # Get the shifted alphabet again by translating the old one by the shift
    shifted = alphabet[shift:] + alphabet[:shift]
    # Translate password back by reversing the cipher; 
    table = str.maketrans(shifted, alphabet)
    # Translate the encrypted password by mapping each letter to the original alphabet according to the shift, using the table
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
            print('Please enter an integer.'), time.sleep(0.7)
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
with open('Python Projects\Password reminder\databaseReminder.txt') as file:
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




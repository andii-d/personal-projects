
import time
import string



password = input('Please create a password: ')
    
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
print(encrypted)


    
encrypt_pw1 = encrypted
# Shifts the password by the length of itself
shift1 = len(encrypted) - len(encrypted) - len(encrypted)
# Gets the string of ascii letters
alphabet1 = string.ascii_letters
# Shifts the ascii letters by the number given
shifted1 = alphabet1[shift1:] + alphabet1[:shift1]
# Makes a translation of the ascii alphabet to apply to the password
table1 = str.maketrans(alphabet1, shifted1)
# Applies the translated alphabet to the password
encrypted1 = encrypt_pw1.translate(table1)

print('\nYour key to decrypt your password is: ', encrypted1)



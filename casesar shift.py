from cryptography.fernet import Fernet
import time
import string


def thing():  
    def write_key():
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

    def load_key():
        """
        Loads the key from the current directory named `key.key`
        """
        return open("key.key", "rb").read()

    write_key()
    key = load_key()
    message = "some secret message".encode()
    f = Fernet(key)
    encrypted = f.encrypt(message)
    print(encrypted), time.sleep(1)
    decrypted_encrypted = f.decrypt(encrypted)
    print(decrypted_encrypted)



password = input('Please create a password: ')
    
encrypt_pw = password
# Shifts the password by the length of itself
shift = len(password) - len(password)
# Gets the string of ascii letters
alphabet = string.ascii_letters
# Shifts the ascii letters by the number given
shifted = alphabet[shift:] + alphabet[:shift]
# Makes a translation of the ascii alphabet to apply to the password
table = str.maketrans(alphabet, shifted)
# Applies the translated alphabet to the password
encrypted = encrypt_pw.translate(table)
print(encrypted)



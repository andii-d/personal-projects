import string
text = 'Hello World'
shift = 3

alphabet = string.ascii_letters
shifted = alphabet[shift:] + alphabet[:shift] 
table = str.maketrans(alphabet, shifted)

encrypted = text.translate(table)

print(encrypted)

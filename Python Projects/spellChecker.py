import re

dictionary = set()
counter = 0

with open("words_alpha.txt") as f:
    for word in f:
        dictionary.add(word.strip())

sentence = input("Enter your sentence to spell check: ")
sentence = sentence.lower().split()

for word in sentence:
    if word not in dictionary:
        print(f"Misspelled word: {word}")
    else:
        counter += 1
        pass

if counter >= 1:
    print("The other words were spelt correctly")
else:
    print("No words were spelt correctly")

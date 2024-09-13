import string
import random

characters = string.digits + string.ascii_letters + "@" + "$" + "&" + "%" + " " 
characters = list(characters)  ## separates character individually
key = characters.copy()

random.shuffle(key)

# print(f"the character list: {characters}")

plainText = input("Please enter your message. ")
encryptedText = " "

## assign a key to each letter in the text inputted by the user.
for letter in plainText: 
    index = characters.index(letter)
    encryptedText += key[index]

print(f" original text: {plainText}")
print(f" encrypted text: {encryptedText}")



## To decrypt the encrypted text

encryptedText = input("Please enter the cipher code. ")
plainText= " "


for letter in encryptedText: 
    index = key.index(letter)
    plainText += characters[index]


print(f" encrypted text: {encryptedText}")
print(f" original text: {plainText}")




# -> omitted code line
## -> notes / explanation

# DECRYPTION
# taking path and key of the encrypted image
path = input(r'Enter path of image you want to decrypt: ')
key = int(input(r'Enter key for decryption: '))
print(r'keep note of the encryption key you assigned to the image during encryption.')

print('The path: ', path)
print('The key: ', key)

# the image file will be opened and data will be read from it
file = open(path, 'rb')
# store the image file data in the variable 'Theimage'
Theimage = file.read()
file.close()

# convert the file data into byte format
Theimage = bytearray(Theimage)

# perform XOR operation
for index, values in enumerate(Theimage):
     Theimage[index] = values ^ int(key)

# open the image file to write decrypted version of data
file = open(path, 'wb')
file.write(Theimage)
file.close()

print('the image has been decrypted!')
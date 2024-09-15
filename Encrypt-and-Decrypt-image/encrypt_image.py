# ENCRYPTION
# taking path and key for image to encrypt
path = input(r'Enter path of image you want to encrypt: ')
key = input(r'Enter an encryption key for the image: ')

print('The path: ', path)
print('The key: ', key)

# the image file will be opened and data will be read from it
file = open(path, 'rb')
# store the image file data in the variable Theimage
Theimage = file.read()
file.close()

# convert the file data into byte format
Theimage = bytearray(Theimage)

# perform XOR operation
for index, values in enumerate(Theimage):
     Theimage[index] = values ^ int(key)

# open the image file to write encrypted version of data

file = open(path, 'wb')
file.write(Theimage)
file.close()

print("The image has be encrypted!\nDon't forget the encryption key.")

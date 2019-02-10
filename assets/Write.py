import os
import shutil

path=input("Enter the location of file to write or create:")
if os.path.isfile(path):
    print('Rebuilding Existing file') #For existing file
else:
    print('Creating new file') #For new file
text=input("Enter the text to write:")
file=open(path,"w")
file.write(text)
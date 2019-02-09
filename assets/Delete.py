import os
import shutil

path=input("Enter the location of file to be write or create:")
if os.path.exists(path):      # checks if the file exists
    print('File Found')     #For existing file
    os.remove(path)          #os.remove(file path) is used to delete
    print('File has been deleted')
else:
    print('File Does\'nt exist')    #Is no file exist

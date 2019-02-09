import os
import shutil

path=input('Enter the location of Program:')
try:
    os.startfile(path)
except:
    print('File not found')
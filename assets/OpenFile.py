import os
import shutil

path=input('Enter Location of Program:')
try:
    os.startfile(path)
except:
    print('File not found')

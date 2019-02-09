import os
import shutil

path1=input('Enter the location of File to copy or rename:')
path2=input('Enter the location to copy:')
shutil.copy(path1,path2)
print('File copied')
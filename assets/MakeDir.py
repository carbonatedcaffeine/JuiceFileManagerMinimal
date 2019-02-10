import os
import shutil

path=input("Enter the directory name with location to make \neg. C:\\Hello\\Newdir \nWhere newdir is new directory:")
os.makedirs(path) 
print('Directory Created')

import os
import shutil

path=input("Enter Location Of Dir name with location to make \neg. C:\\Hello\\Newdir \nWhere newdir is new directory:")
os.makedirs(path) 
print('Directory Created')

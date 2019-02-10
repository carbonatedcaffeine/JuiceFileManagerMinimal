import os
import shutil

path=input("Enter the location of file to read:")
file=open(path,"r")
print(file.read()) 
input('Press Enter...')  
file.close()
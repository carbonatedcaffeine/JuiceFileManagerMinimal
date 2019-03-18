import os
import shutil

path=input("Enter Location Of File to read:")
file=open(path,"r")
print(file.read()) 
input('Press Enter...')  
file.close()

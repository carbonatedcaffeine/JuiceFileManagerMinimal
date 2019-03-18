import os
import shutil

path=input("Enter Location Of File:")
text=input("Enter the text to write:")
file=open(path,"a")
file.write('\n'+text)

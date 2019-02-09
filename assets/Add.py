import os
import shutil

path=input("Enter the file location:")
text=input("Enter the text to write:")
file=open(path,"a")
file.write('\n'+text)
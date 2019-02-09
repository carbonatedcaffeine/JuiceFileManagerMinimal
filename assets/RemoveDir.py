import os
import shutil

path=input('Enter the location of Directory:')
treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
if treedir==1:
    os.rmdir(path)
if treedir==2:
    shutil.rmtree(path)
    print('Directory Deleted')
if treedir==3:
    exit()
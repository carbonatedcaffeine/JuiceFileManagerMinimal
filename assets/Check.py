import os
import shutil

fp=int(input('Check the presence of \n1.File \n2.Directry \n'))
if fp==1:
    path=input("Enter Location Of File:")
    os.path.isfile(path)
    if os.path.isfile(path)==True:
        print('File Found')
    else:
        print('File not Found')
if fp==2:
    path=input("Enter the Directory location:")
    os.path.isdir(path)
    if os.path.isdir(path)==False:
        print('Directory Found')
    else:
        print('Directory Not Found')

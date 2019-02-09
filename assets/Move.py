import os
import shutil

path1=input('Enter the location of File to move or rename:')
mr=int(input('1.Rename \n2.Move \n'))
if mr==1:
    path2=input('Enter the resulting location with resulting file name:')
    shutil.move(path1,path2)
    print('File renamed')
if mr==2:
    path2=input('Enter the location to move:')
    shutil.move(path1,path2)
    print('File moved')
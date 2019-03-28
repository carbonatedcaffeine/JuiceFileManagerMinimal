import time
import os
import shutil
import webbrowser

# Imports the openweb asset to open websites
def OpenWeb():
	os.system("python3 ~/Downloads/JFM/Assets/OpenWeb.py")

# Imports the update asset to update all the other assets
def Update():
	os.system("python3 ~/Downloads/JFM/Assets/Update.py")

# Imports the read asset to read files
def Read():
	os.system("python3 ~/Downloads/JFM/Assets/Read.py")

# Imports the write asset to make a file .txt
def Write():
	os.system("python3 ~/Downloads/JFM/Assets/Write.py")

# Imports the add asset which adds text to files
def Add():
    os.system("python3 ~/Downloads/JFM/Assets/Add.py")

# Imports the delete asset to delete files
def Delete():
    os.system("python3 ~/Downloads/JFM/Assets/Delete.py")

# Imports the Dirlist asset to list files in a directory
def Dirlist():
    os.system("python3 ~/Downloads/JFM/Assets/DirList.py")

# Imports the check asset to check of a files existence
def Check():
    os.system("python3 ~/Downloads/JFM/Assets/Check.py")

# Imports the move asset to move a file
def Move():
    os.system("python3 ~/Downloads/JFM/Assets/Move.py")

# Imports the copy asset to copy a file
def Copy():
    os.system("python3 ~/Downloads/JFM/Assets/Copy.py")

# Imports the MakeDir asset to make a directory
def Makedir():
    os.system("python3 ~/Downloads/JFM/Assets/MakeDir.py")

# Imports the RemoveDir asset to remove a directory
def Removedir():
    os.system("python3 ~/Downloads/JFM/Assets/RemoveDir.py")

# Imports the OpenFile assets to open a file
def Openfile():
    os.system("python3 ~/Downloads/JFM/Assets/OpenFile.py")

# Imports the Information asset to show Information about this jfm build
def Information():
    os.system("python3 ~/Downloads/JFM/Assets/Information.py")

# Imports the extra asset to show some extras
def Extra():
    os.system("python3 ~/Downloads/JFM/Assets/Extra.py")

run=1
while(run==1):
    print('''
=======================================
Juice File Manager 4.0
=======================================''')
    dec=int(input(''' 1.Read a file
2.  Write in a File
3.  Append text in a File
4.  Delete a file
5.  List Files in a directory
6.  Check file existence
7.  Move a file
8.  Copy a file
9.  Create a Directory
10. Delete A Directory
11. Open a program
12. Exit

=======================================
Other
=======================================
13. Build Information
14. Extras
15. Update (USING TERMINAL)
16. Go To JuiceFileManager Homepage

#: '''))
    if dec==1:
        Read()
    if dec==2:
        Write()
    if dec==3:
        Add()
    if dec==4:
        Delete()
    if dec==5:
        Dirlist()
    if dec==6:
        Check()
    if dec==7:
        Move()
    if dec==8:
        Copy()
    if dec==9:
        Makedir()
    if dec==10:
        Removedir()
    if dec==11:
        Openfile()
    if dec==12:
        exit()
    if dec==13:
         Information()
    if dec==14:
        Extra()
    if dec==15:
        Update()
    if dec==16:
        OpenWeb()




    run=int(input("1.Run again \n2.Exit \n #: \n"))
    if run==2:
        exit()

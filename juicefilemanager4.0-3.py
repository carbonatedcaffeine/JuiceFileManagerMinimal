import time
import os
import shutil
import webbrowser

def OpenWeb():
	os.system("python3 /root/JFM/Assets/OpenWeb.py")
	
def Update():
	os.system("python3 /root/JFM/Assets/Update.py") 
		  
def Read():
	os.system("python3 /root/JFM/Assets/Read.py")
	
def Write():  
	os.system("python3 /root/JFM/Assets/Write.py")
    
def Add():
    os.system("python3 /root/JFM/Assets/Add.py")
    
def Delete():
    os.system("python3 /root/JFM/Assets/Delete.py")
    
def Dirlist():
    os.system("python3 /root/JFM/Assets/DirList.py")
    
def Check():
    os.system("python3 /root/JFM/Assets/Check.py")
    
def Move():
    os.system("python3 /root/JFM/Assets/Move.py")
    
def Copy():
    os.system("python3 /root/JFM/Assets/Copy.py")

def Makedir():
    os.system("python3 /root/JFM/Assets/MakeDir.py")
    
def Removedir():
    os.system("python3 /root/JFM/Assets/RemoveDir.py")

def Openfile():
    os.system("python3 /root/JFM/Assets/OpenFile.py")
    
def Information():
    os.system("python3 /root/JFM/Assets/Information.py")

run=1
while(run==1):
    print('''
Juice File Manager 4.0
=======================================''')
    dec=int(input('''1.Read a file
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

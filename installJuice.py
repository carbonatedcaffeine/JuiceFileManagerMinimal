import os

ans = input('''
JuiceFileManager Installer (BETA)
#################################

welcome to the juice file manager installer!
this will download all the required assets for
JFM.

Proceed? (y/n) #: ''')

if ans = 'y':
  ans = input('''
JuiceFileManager Installer (BETA)
#################################

Where Would You Like To Install
To?

1. Downloads Folder (~/Downloads)

2. Root Of Filesystem (/)

3. Root User Folder (/root) (For Always Root Users)

#: ''')
  if ans = '1':
    os.system("mkdir ~/Downloads/JFM")
    os.system("mkdir ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Add.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Check.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Copy.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Delete.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/DirList.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Extra.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Information.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/MakeDir.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Move.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/OpenFile.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/OpenFile.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/OpenWeb.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Read.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/RemoveDir.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Update.py -P ~/Downloads/JFM/Assets")
    os.system("wget https://github.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/blob/Juice-File-Manager-Beta-4.0/assets/Write.py -P ~/Downloads/JFM/Assets")
    #Not Done
    
    
    

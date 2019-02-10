import os

ans = input('''
JuiceFileManager Installer (BETA)
#################################

welcome to the juice file manager installer!
this will download all the required assets for
JFM.

Proceed? (y/n) #: ''')

if ans == 'y':
    ans = input('''
JuiceFileManager Installer (BETA)
#################################

Where Would You Like To Install
To?

1. Downloads Folder (~/Downloads)

2. Root Of Filesystem (/)

3. Root User Folder (/root) (For Always Root Users)

4. Home Folder (~/)

#: ''')
    if ans == '1':
        os.system("mkdir ~/Downloads/JFM")
        os.system("mkdir ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P ~/Downloads/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/juicefilemanager4.0-1.py -O ~/Downloads/juicefilemanager4.0.py")
        
    if ans == '2':
        os.system("mkdir /JFM")
        os.system("mkdir /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P /JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/juicefilemanager4.0-2.py -O /juicefilemanager4.0.py")
        
    if ans == '3':
        os.system("mkdir /root/JFM")
        os.system("mkdir /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P /root/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/juicefilemanager4.0-3.py -O /root/juicefilemanager4.0.py")
        
    if ans == '4':
        os.system("mkdir ~/JFM")
        os.system("mkdir ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P ~/JFM/Assets")
        os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/juicefilemanager4.0-1.py -O ~/juicefilemanager4.0.py")
    
    

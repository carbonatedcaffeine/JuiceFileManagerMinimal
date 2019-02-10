import os
import shutil

ans = input('''
Juice File Manager 4.0 Update
=======================================

1. install wget, svn and update

2. update

#: ''')

if ans == '1':
  os.system("sudo apt-get update")
  os.system("sudo apt-get install wget")
  ans = input('''
Juice File Manager 4.0 Update
=======================================

what kind of install do you have?

1. ~/Downloads

2. /

3. /root

#: ''')
  if ans == '1':
    os.system("rm -r ~/Downloads/JFM/Assets/Add.py ~/Downloads/JFM/Assets/Check.py ~/Downloads/JFM/Assets/Copy.py ~/Downloads/JFM/Assets/Delete.py ~/Downloads/JFM/Assets/DirList.py ~/Downloads/JFM/Assets/Extra.py ~/Downloads/JFM/Assets/Information.py ~/Downloads/JFM/Assets/MakeDir.py ~/Downloads/JFM/Assets/Move.py ~/Downloads/JFM/Assets/OpenFile.py ~/Downloads/JFM/Assets/OpenWeb.py ~/Downloads/JFM/Assets/Read.py ~/Downloads/JFM/Assets/RemoveDir.py ~/Downloads/JFM/Assets/Write.py ~/Downloads/JFM/Assets/Update.py")
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
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P ~/Downloads/JFM/")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P ~/Downloads/JFM/Assets")
    os.system("cp ~/Update.py ~/Downloads/JFM/Assets")
    print('DONE')
    
  if ans == '2':
    os.system("rm -r /JFM/Assets/Add.py /JFM/Assets/Check.py /JFM/Assets/Copy.py /JFM/Assets/Delete.py /JFM/Assets/DirList.py /JFM/Assets/Extra.py /JFM/Assets/Information.py /JFM/Assets/MakeDir.py /JFM/Assets/Move.py /JFM/Assets/OpenFile.py /JFM/Assets/OpenWeb.py /JFM/Assets/Read.py /JFM/Assets/RemoveDir.py /JFM/Assets/Write.py /JFM/Assets/Update.py")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P /JFM/")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P /JFM/Assets")
    os.system("cp ~/Update.py /JFM/Assets")
    print('DONE')
    
  if ans == '3':
    os.system("rm -r /root/JFM/Assets/Add.py /root/JFM/Assets/Check.py /root/JFM/Assets/Copy.py /root/JFM/Assets/Delete.py /root/JFM/Assets/DirList.py /root/JFM/Assets/Extra.py /root/JFM/Assets/Information.py /root/JFM/Assets/MakeDir.py /root/JFM/Assets/Move.py /root/JFM/Assets/OpenFile.py /root/JFM/Assets/OpenWeb.py /root/JFM/Assets/Read.py /root/JFM/Assets/RemoveDir.py /root/JFM/Assets/Write.py /root/JFM/Assets/Update.py")
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
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P /root/JFM/")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P /root/JFM/Assets")
    os.system("cp ~/Update.py /root/JFM/Assets")
    print('DONE')

if ans == '2':
  ans = input('''
Juice File Manager 4.0 Update
=======================================

what kind of install do you have?

1. ~/Downloads

2. /

3. /root

#: ''')
  if ans == '1':
    os.system("rm -r ~/Downloads/JFM/Assets/Add.py ~/Downloads/JFM/Assets/Check.py ~/Downloads/JFM/Assets/Copy.py ~/Downloads/JFM/Assets/Delete.py ~/Downloads/JFM/Assets/DirList.py ~/Downloads/JFM/Assets/Extra.py ~/Downloads/JFM/Assets/Information.py ~/Downloads/JFM/Assets/MakeDir.py ~/Downloads/JFM/Assets/Move.py ~/Downloads/JFM/Assets/OpenFile.py ~/Downloads/JFM/Assets/OpenWeb.py ~/Downloads/JFM/Assets/Read.py ~/Downloads/JFM/Assets/RemoveDir.py ~/Downloads/JFM/Assets/Write.py ~/Downloads/JFM/Assets/Update.py")
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
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P ~/Downloads/JFM/")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P ~/Downloads/JFM/Assets")
    os.system("cp ~/Update.py ~/Downloads/JFM/Assets")
    print('DONE')
    
  if ans == '2':
    os.system("rm -r /JFM/Assets/Add.py /JFM/Assets/Check.py /JFM/Assets/Copy.py /JFM/Assets/Delete.py /JFM/Assets/DirList.py /JFM/Assets/Extra.py /JFM/Assets/Information.py /JFM/Assets/MakeDir.py /JFM/Assets/Move.py /JFM/Assets/OpenFile.py /JFM/Assets/OpenWeb.py /JFM/Assets/Read.py /JFM/Assets/RemoveDir.py /JFM/Assets/Write.py /JFM/Assets/Update.py")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P /JFM/")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P /JFM/Assets")
    os.system("cp ~/Update.py /JFM/Assets")
    print('DONE')
    
  if ans == '3':
    os.system("rm -r /root/JFM/Assets/Add.py /root/JFM/Assets/Check.py /root/JFM/Assets/Copy.py /root/JFM/Assets/Delete.py /root/JFM/Assets/DirList.py /root/JFM/Assets/Extra.py /root/JFM/Assets/Information.py /root/JFM/Assets/MakeDir.py /root/JFM/Assets/Move.py /root/JFM/Assets/OpenFile.py /root/JFM/Assets/OpenWeb.py /root/JFM/Assets/Read.py /root/JFM/Assets/RemoveDir.py /root/JFM/Assets/Write.py /root/JFM/Assets/Update.py")
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
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -P /root/JFM/")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -P /root/JFM/Assets")
    os.system("cp ~/Update.py /root/JFM/Assets")
    print('DONE')

  

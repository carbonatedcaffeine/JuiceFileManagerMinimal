import os

ans = input('''
==============================
JuiceFileManager Addon Manager
==============================

What Kind Of Install Do You Have?

1. ~/Downloads

2. /root

3. /

4. ~/

#: ''')

if ans == '1':
  print('''
==============================
JuiceFileManager Addon Manager
==============================
welcome to the addon manager!
please wait till we import some
packages from github...
''')
  os.system("mkdir ~/Downloads/JFM/Addons")
  os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/AddonManager/addonAssets/AdminOptions.py -P ~/Downloads/JFM/Assets")
  ans = input('''
==============================
JuiceFileManager Addon Manager
==============================
would you like to install any
addons?

1. Admin Options

2. No (Will Delete Package)

#: ''')
  if ans == '1':
    os.system("cp ~/Downloads/JFM/Addons/AdminOptions.py ~/Downloads/JFM/Assets")
    os.system("rm ~/Downloads/JFM/Addons/AdminOptions.py")
    os.system("rm -R ~/Downloads/JFM/Addons")
    print('Done')
  
  if ans == '2':
    os.system("rm ~/Downloads/JFM/Addons/AdminOptions.py")
    os.system("rm -R ~/Downloads/JFM/Addons")
    
    
if ans == '2':
  print('''
==============================
JuiceFileManager Addon Manager
==============================
welcome to the addon manager!
please wait till we import some
packages from github...
''')
  os.system("mkdir /root/JFM/Addons")
  os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/AddonManager/addonAssets/AdminOptions.py -P /root/JFM/Assets")
  ans = input('''
==============================
JuiceFileManager Addon Manager
==============================
would you like to install any
addons?

1. Admin Options

2. No (Will Delete Package)

#: ''')
  if ans == '1':
    os.system("cp /root/JFM/Addons/AdminOptions.py /root/JFM/Assets")
    os.system("rm /root/JFM/Addons/AdminOptions.py")
    os.system("rm -R ~/Downloads/JFM/Addons")
    print('Done')
  
  if ans == '2':
    os.system("rm /root/JFM/Addons/AdminOptions.py")
    os.system("rm -R /root/JFM/Addons")
    
if ans == '3':
  print('''
==============================
JuiceFileManager Addon Manager
==============================
welcome to the addon manager!
please wait till we import some
packages from github...
''')
  os.system("mkdir /JFM/Addons")
  os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/AddonManager/addonAssets/AdminOptions.py -P /JFM/Assets")
  ans = input('''
==============================
JuiceFileManager Addon Manager
==============================
would you like to install any
addons?

1. Admin Options

2. No (Will Delete Package)

#: ''')
  if ans == '1':
    os.system("cp /JFM/Addons/AdminOptions.py /JFM/Assets")
    os.system("rm /JFM/Addons/AdminOptions.py")
    os.system("rm -R /JFM/Addons")
    print('Done')
  
  if ans == '2':
    os.system("rm /JFM/Addons/AdminOptions.py")
    os.system("rm -R /JFM/Addons")
    
if ans == '4':
  print('''
==============================
JuiceFileManager Addon Manager
==============================
welcome to the addon manager!
please wait till we import some
packages from github...
''')
  os.system("mkdir ~/JFM/Addons")
  os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/AddonManager/addonAssets/AdminOptions.py -P ~/JFM/Assets")
  ans = input('''
==============================
JuiceFileManager Addon Manager
==============================
would you like to install any
addons?

1. Admin Options

2. No (Will Delete Package)

#: ''')
  if ans == '1':
    os.system("cp ~/JFM/Addons/AdminOptions.py ~/JFM/Assets")
    os.system("rm ~/JFM/Addons/AdminOptions.py")
    os.system("rm -R ~/JFM/Addons")
    print('Done')
  
  if ans == '2':
    os.system("rm ~/JFM/Addons/AdminOptions.py")
    os.system("rm -R ~/JFM/Addons")

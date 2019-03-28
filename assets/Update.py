import os
import shutil

ans = input('''
=======================================
Juice File Manager 4.0 Update
=======================================
This will update all your packages!!!

(Y/N)#: ''')

if ans == 'y':
  ans = input('''
=======================================
Juice File Manager 4.0 Update
=======================================

what kind of install do you have?

1. ~/Downloads/JFM/

2. /JFM/

3. /root/JFM/

4. ~/JFM/

#: ''')
  if ans == '1':
    os.system("rm -r ~/Downloads/JFM/Assets/Add.py ~/Downloads/JFM/Assets/Check.py ~/Downloads/JFM/Assets/Copy.py ~/Downloads/JFM/Assets/Delete.py ~/Downloads/JFM/Assets/DirList.py ~/Downloads/JFM/Assets/Extra.py ~/Downloads/JFM/Assets/Information.py ~/Downloads/JFM/Assets/MakeDir.py ~/Downloads/JFM/Assets/Move.py ~/Downloads/JFM/Assets/OpenFile.py ~/Downloads/JFM/Assets/OpenWeb.py ~/Downloads/JFM/Assets/Read.py ~/Downloads/JFM/Assets/RemoveDir.py ~/Downloads/JFM/Assets/Write.py ~/Downloads/JFM/Assets/Update.py")
    print('[<->               ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -q -P ~/Downloads/JFM/Assets")
    print('[ <->              ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -q -P ~/Downloads/JFM/Assets")
    print('[  <->             ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -q -P ~/Downloads/JFM/Assets")
    print('[   <->            ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -q -P ~/Downloads/JFM/Assets")
    print('[    <->           ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -q -P ~/Downloads/JFM/Assets")
    print('[     <->          ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -q -P ~/Downloads/JFM/Assets")
    print('[      <->         ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -q -P ~/Downloads/JFM/Assets")
    print('[       <->        ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -q -P ~/Downloads/JFM/Assets")
    print('[        <->       ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -q -P ~/Downloads/JFM/Assets")
    print('[         <->      ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -q -P ~/Downloads/JFM/Assets")
    print('[          <->     ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -q -P ~/Downloads/JFM/Assets")
    print('[           <->    ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -q -P ~/Downloads/JFM/Assets")
    print('[            <->   ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -q -P ~/Downloads/JFM/Assets")
    print('[             <->  ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -q -P ~/Downloads/JFM/Assets")
    print('[              <-> ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -q -P ~/Downloads/JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/ShowReadme.py -q -P ~/Downloads/JFM/Assets")
    print('DONE')
    
  if ans == '2':
    os.system("rm -r /JFM/Assets/Add.py /JFM/Assets/Check.py /JFM/Assets/Copy.py /JFM/Assets/Delete.py /JFM/Assets/DirList.py /JFM/Assets/Extra.py /JFM/Assets/Information.py /JFM/Assets/MakeDir.py /JFM/Assets/Move.py /JFM/Assets/OpenFile.py /JFM/Assets/OpenWeb.py /JFM/Assets/Read.py /JFM/Assets/RemoveDir.py /JFM/Assets/Write.py /JFM/Assets/Update.py")
    print('[<->               ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -q -P /JFM/Assets")
    print('[ <->              ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -q -P /JFM/Assets")
    print('[  <->             ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -q -P /JFM/Assets")
    print('[   <->            ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -q -P /JFM/Assets")
    print('[    <->           ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -q -P /JFM/Assets")
    print('[     <->          ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -q -P /JFM/Assets")
    print('[      <->         ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -q -P /JFM/Assets")
    print('[       <->        ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -q -P /JFM/Assets")
    print('[        <->       ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -q -P /JFM/Assets")
    print('[         <->      ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -q -P /JFM/Assets")
    print('[          <->     ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -q -P /JFM/Assets")
    print('[           <->    ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -q -P /JFM/Assets")
    print('[            <->   ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -q -P /JFM/Assets")
    print('[             <->  ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -q -P /JFM/Assets")
    print('[              <-> ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -q -P /JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/ShowReadme.py -q -P /JFM/Assets")
    print('DONE')
    
  if ans == '3':
    os.system("rm -r /root/JFM/Assets/Add.py /root/JFM/Assets/Check.py /root/JFM/Assets/Copy.py /root/JFM/Assets/Delete.py /root/JFM/Assets/DirList.py /root/JFM/Assets/Extra.py /root/JFM/Assets/Information.py /root/JFM/Assets/MakeDir.py /root/JFM/Assets/Move.py /root/JFM/Assets/OpenFile.py /root/JFM/Assets/OpenWeb.py /root/JFM/Assets/Read.py /root/JFM/Assets/RemoveDir.py /root/JFM/Assets/Write.py /root/JFM/Assets/Update.py")
    print('[<->               ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -q -P /root/JFM/Assets")
    print('[ <->              ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -q -P /root/JFM/Assets")
    print('[  <->             ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -q -P /root/JFM/Assets")
    print('[   <->            ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -q -P /root/JFM/Assets")
    print('[    <->           ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -q -P /root/JFM/Assets")
    print('[     <->          ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -q -P /root/JFM/Assets")
    print('[      <->         ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -q -P /root/JFM/Assets")
    print('[       <->        ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -q -P /root/JFM/Assets")
    print('[        <->       ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -q -P /root/JFM/Assets")
    print('[         <->      ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -q -P /root/JFM/Assets")
    print('[          <->     ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -q -P /root/JFM/Assets")
    print('[           <->    ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -q -P /root/JFM/Assets")
    print('[            <->   ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -q -P /root/JFM/Assets")
    print('[             <->  ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -q -P /root/JFM/Assets")
    print('[              <-> ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -q -P /root/JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/ShowReadme.py -q -P /root/JFM/Assets")
    print('DONE')
  
  if ans == '4':
    os.system("rm -r ~/JFM/Assets/Add.py ~/JFM/Assets/Check.py ~/JFM/Assets/Copy.py ~/JFM/Assets/Delete.py ~/JFM/Assets/DirList.py ~/JFM/Assets/Extra.py ~/JFM/Assets/Information.py ~/JFM/Assets/MakeDir.py ~/JFM/Assets/Move.py ~/JFM/Assets/OpenFile.py ~/JFM/Assets/OpenWeb.py ~/JFM/Assets/Read.py ~/JFM/Assets/RemoveDir.py ~/JFM/Assets/Write.py ~/JFM/Assets/Update.py")
    print('[<->               ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Add.py -q -P ~/JFM/Assets")
    print('[ <->              ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Check.py -q -P ~/JFM/Assets")
    print('[  <->             ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Copy.py -q -P ~/JFM/Assets")
    print('[   <->            ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Delete.py -q -P ~/JFM/Assets")
    print('[    <->           ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/DirList.py -q -P ~/JFM/Assets")
    print('[     <->          ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Extra.py -q -P ~/JFM/Assets")
    print('[      <->         ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Information.py -q -P ~/JFM/Assets")
    print('[       <->        ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/MakeDir.py -q -P ~/JFM/Assets")
    print('[        <->       ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Move.py -q -P ~/JFM/Assets")
    print('[         <->      ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenFile.py -q -P ~/JFM/Assets")
    print('[          <->     ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/OpenWeb.py -q -P ~/JFM/Assets")
    print('[           <->    ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Read.py -q -P ~/JFM/Assets")
    print('[            <->   ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/RemoveDir.py -q -P ~/JFM/Assets")
    print('[             <->  ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Update.py -q -P ~/JFM/Assets")
    print('[              <-> ]')
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/Write.py -q -P ~/JFM/Assets")
    os.system("wget https://raw.githubusercontent.com/EnderNightLord-ChromeBook/JuiceFileManagerMinimal/master/assets/ShowReadme.py -q -P ~/JFM/Assets")
    print('DONE')
   

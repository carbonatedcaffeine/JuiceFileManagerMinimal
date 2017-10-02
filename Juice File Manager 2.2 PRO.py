import shutil
import os
from tkinter import*
HEIGHT = 100
WIDTH = 500
window = Tk()

def Read():        #For reading files
    path=input("Enter the location of file to read:")
    file=open(path,"r")
    print(file.read()) 
    input('Press Enter...')  
    file.close()

def Write():    #For writing or creating files
    path=input("Enter the location of file to write or create:")
    if os.path.isfile(path):
        print('Rebuilding Existing file') #For existing file
    else:
        print('Creating new file') #For new file
    text=input("Enter the text to write:")
    file=open(path,"w")
    file.write(text)

def Add():      # Adding text to a file
    path=input("Enter the file location:")
    text=input("Enter the text to write:")
    file=open(path,"a")
    file.write('\n'+text)


def Delete():          #Deleting a File
    path=input("Enter the location of file to be write or create:")
    if os.path.exists(path):      # checks if the file exists
        print('File Found')     #For existing file
        os.remove(path)          #os.remove(file path) is used to delete
        print('File has been deleted')
    else:
        print('File Does\'nt exist')    #Is no file exist



def Dirlist():      #Listing files in a directory
    path=input("Enter the Directory location to list:")
    sortlist=sorted(os.listdir(path))       #Sorting and listing files
    i=0
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1




def Move():        #For moving or renameing file
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


def Copy():       #For copying
    path1=input('Enter the location of File to copy or rename:')
    path2=input('Enter the location to copy:')
    shutil.copy(path1,path2)
    print('File copied')


def Makedir():            #For creating directory
    path=input("Enter the directory name with location to make \neg. C:\\Hello\\Newdir \nWhere newdir is new directory:")
    os.makedirs(path) 
    print('Directory Created')


def Removedir():             #For removing Directory
    path=input('Enter the location of Directory:')
    treedir=int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir==1:
        os.rmdir(path)
    if treedir==2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir==3:
        exit()


def Openfile():
    path=input('Enter the location of Program:')
    try:
        os.startfile(path)
    except:
        print('File not found')

def Build():
    print('''
                       Detailed Build Information
Created On:Linux
Channel:Stable
Build Date: 18 september 2017
Version:2.2''')

def Other():
    print('''
                                 Other
WebSite: (Coming Soon)
Update News for 2.2: 1. New software sources
Made By:Camden Bruce
Thanks Too:Python
Other Apps:Juice Program Loader''')



window.title('Juice File Manager (JFM)')
buttonA = Button(window, text='Read Text/Things that have text', command=Read)
buttonB = Button(window, text='Write to a file', command=Write)
buttonC = Button(window, text='Add To File', command=Add)
buttonD = Button(window, text='Delete', command=Delete)
buttonE = Button(window, text='DIR LIST', command=Dirlist)
#this is where F used to be this button is buggy so getting into it
buttonG = Button(window, text='Move', command=Move)
buttonH = Button(window, text='Copy', command=Copy)
buttonI = Button(window, text='Make Dir', command=Makedir)
buttonJ = Button(window, text='Remove Dir', command=Removedir)
buttonK = Button(window, text='Open File (Python/.py', command=Openfile)
buttonL = Button(window, text='Detailed Build Information', command=Build)
buttonM = Button(window, text='Other/News/Updates', command=Other)



c = Canvas(window, width=WIDTH, height=HEIGHT, bg='purple')
c.pack()
buttonA.pack()
buttonB.pack()
buttonC.pack()
buttonD.pack()
buttonE.pack()
#buttonF.pack() (this button is broken at this moment come back in another update)
buttonG.pack()
buttonH.pack()
buttonI.pack()
buttonJ.pack()
buttonK.pack()
buttonL.pack()
buttonM.pack()




#                               !!!Developer Notes!!!

#1. This is not copyright you can use this and copy as much as you like
#2. This is a free software if you break this or edit please know what your doing if broken just download another copy

#Other software sources : Download at Google + and will take you website

#               VERY BRIEF DETAILS ON COMPUTER THIS WAS BUILT ON

# Made on linux on a samsung ARM chromebook 
# Using CROUTON
# USER NAME:ender-chronos
# Desktop Environment:Xfce4
#                                    !ThankYou!

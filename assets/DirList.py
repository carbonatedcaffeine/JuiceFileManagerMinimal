import os 
import shutil

path=input("Enter the Directory location to list:")
sortlist=sorted(os.listdir(path))       #Sorting and listing files
i=0
while(i<len(sortlist)):
    print(sortlist[i]+'\n')
    i+=1
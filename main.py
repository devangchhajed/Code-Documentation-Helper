from os import listdir
from os.path import isfile, join
import os

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

dirName = './main';

# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)

# Print the files
for elem in listOfFiles:
    print(elem)

print ("****************")

# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    


n=input("name : ")
out=open(n,"w+")
data=""# Print the files    
for elem in listOfFiles:
    print(elem)
    f=open(elem,"r", errors='ignore')
    x=str(f.read())
    out.write(elem)    
    out.write("\n")    
    out.write(x)    
    out.write("\n")    
    out.write("\n")    
    f.close()

out.close()
    
    
    


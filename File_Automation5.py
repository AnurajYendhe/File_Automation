# Display the size of each file in the directory
import os
import time
from sys import *

def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)
    for foldername, subfoldername, filename in os.walk(DirName):
        print("Current Directory name : ",foldername)
        for fname in filename:
            fname = foldername+'/'+fname
            print(fname,":",os.path.getsize(fname),"byte")
def main():
    print("-------------Automation using Python---------")
    print("----------File Subsystem Automation-----------")

    print("Automation Script Name ",argv[0])

    if(len(argv) == 2):
        if((argv[1] == "-H") or (argv[1] == "-h")):
            print("Help : This automation script is used to perform File Automation and Display the size of files")
            exit()
        elif((argv[1] == "-U") or (argv[1] == "-u")):
            print("Usage : Name_Of_Script Path_Of_Directory")
            print("Example : Demo.py Anuraj")
            exit()

        else:
            startTime = time.time()
            DirectoryTravel(argv[1])
            endTime = time.time()
            print("The script took time to execute as : ",endTime - startTime)
        
    else:
        print("Error : Invalid Numbers of Arguments.")
if __name__ == "__main__":
    main()
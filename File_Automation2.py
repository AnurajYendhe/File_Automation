# Check file is exists in current direct or not
import os
import time
from sys import *

def DirectoryTravel(DirName,file):
    print("We are going to Scan the Directory : ",DirName)
    for foldername, subfoldername, filename in os.walk(DirName):
        for fname in filename:
            if(file == fname):
                print(fname) 

def main():
    print("-------------Automation using Python---------")
    print("----------File Subsystem Automation-----------")

    print("Automation Script Name ",argv[0])

    if(len(argv) == 2):
        if((argv[1] == "-H") or (argv[1] == "-h")):
            print("Help : This automation script is used to perform File Automation and check file is present in current directory or not")
            exit()
        elif((argv[1] == "-U") or (argv[1] == "-u")):
            print("Usage : Name_Of_Script Path_Of_Directory Name_Of_File")
            print("Example : Demo.py Anuraj Assignment1_10.py")
            exit()

        else:       
            print("Error : Invalid Arguments.")

    elif(len(argv) == 3):
        startTime = time.time()
        DirectoryTravel(argv[1],argv[2])
        endTime = time.time()
        print("The script took time to execute as : ",endTime - startTime)

    else:
        print("Error : Invalid Numbers of Arguments.")
if __name__ == "__main__":
    main()
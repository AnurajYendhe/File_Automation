# Display the Name of file have maximun size
import os
import time
from sys import *

def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)
    max = 0
    for foldername, subfoldername, filename in os.walk(DirName):
        print("Current Directory name : ",foldername)
        for fname in filename:
            filepath = os.path.join(foldername,fname)
            size = os.path.getsize(filepath)
            if(max < size):
                max = size
                maxFile = filepath
    print(maxFile,"having maximun size is : ",max)
    
def main():
    print("-------------Automation Script---------")

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
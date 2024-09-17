# Display Names of file in the current directory
import os
from sys import *

def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)
    counter = 0
    for foldername, subfoldername, filename in os.walk(DirName):
        for fname in filename:
            print(fname)
            counter = counter + 1 
    print("Total numbers of files in that directory is : ",counter)
            
def main():
    print("-------------Automation using Python---------")
    print("------------File Subsystem Automation-------")

    print("Automation Script Name ",argv[0])

    if(len(argv) == 2):
        if((argv[1] == "-H") or (argv[1] == "-h")):
            print("Help : This automation script is used to perform File Automation and display name of files in current directory.")
            exit()
        elif((argv[1] == "-U") or (argv[1] == "-u")):
            print("Usage : Name_Of_Script Path_Of_Directory")
            print("Example : Demo.py Anuraj")
            exit()

        else:       
            DirectoryTravel(argv[1])
    else:
        print("Error : Invalid Numbers of Arguments.")
if __name__ == "__main__":
    main()
# File Automation : Find the duplicates files in input directory

import os
import time
import hashlib
from sys import * 

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DirectoryTrevel(DirName):
    print("We are going to scan directory : ",DirName)

    flag = os.path.isabs(DirName)
    if(flag == False):
        DirName = os.path.abspath(DirName)

    exist = os.path.exists(DirName)

    if(exist == True):
        dups = dict()
        
        for folderName, subfolderName, filesName in os.walk(DirName):
            print("Current folder name is : ",folderName)
            for file in filesName:
                filepath = os.path.join(folderName,file)
                checksum = hashfile(filepath)

                if checksum in dups:
                    dups[checksum].append(filepath)
                else:
                    dups[checksum] = [filepath]

        return dups                   
    else:
        print("Error : Invalid path")

def checkdups(value):
    if(len(value) > 1):
        return value

def printResult(Arr):
    results = list(filter(checkdups,Arr.values()))

    if(len(results) > 0):
        print("Duplicate files found")
        print("Following are duplicate files.")
        print("   ")
        for result in results:
            for subresult in result:
                print(subresult)
                print("   ")
    else:
        print("No duplicate file found")

def main():
    print("------Automation using Python------")
    print("-----File Subsystems Automation-----")
    print("Automation script Name is : ",argv[0])

    if(len(argv) == 2):
        if((argv[1] == "-H") or (argv[1] == "-h")):
            print("Help : This automation script is use to display name of duplicates files in the directory.")
            exit()

        elif((argv[1] == "-U") or (argv[1] == "-u")):
            print('Usage : DirectoryChecksum.py "Path_of_directory"')
            print('Example : DirectoryCopy.py "Demo"')
            exit()

        else:
            try:
                startTime = time.time()
                Arr = dict()
                Arr = DirectoryTrevel(argv[1])
                printResult(Arr)
                endTime = time.time()
                print("The script took time for execute as : ",endTime - startTime)

            except ValueError:
                print("Error : invalid datatype of input")

            except Exception as Err:
                print("Error : invalid inputs",Err)

    else:
        print("Error : Invalid Numbers of Arguments.")
        exit()
if __name__ == "__main__":
    main()
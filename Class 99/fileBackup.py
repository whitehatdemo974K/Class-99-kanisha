import os
import shutil
import time

source= input("Enter the source folder: ")
destination= input("Enter the destination: ")
source=source+'/'
destination=destination+'/'
source= input("Enter the time folder: ")
time=time+'/'


listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)
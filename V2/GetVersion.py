import json
import os, sys
from io import open
import time

def GetVersion ():
    
    Comando = '''wmic /output:C:\VersionList.txt product where "Vendor like '%vsblty%'" get Name, Version'''
    print ("////////////////////////////////////////////////////////////////")
    print (" Get Version")
    print ("////////////////////////////////////////////////////////////////")
    #print (Comando)
    os.system(Comando)
    time.sleep(1)
    # ok 
    i = 0
    Versiones = []
    f = open("C:/VersionList.txt", "r")
    while(True):
        linea = f.readline()
        i += 1
        
        if (i == 3):
            print(str(i) + "-" + linea)
            VersionClient = linea
        
        if (i == 5):
            print(str(i) + "-" + linea)
            VersionService = linea
        
        if not linea:
            break
    f.close()
    Versiones = [VersionClient, VersionService]
    return Versiones


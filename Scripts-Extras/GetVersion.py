import json
import os, sys
from io import open

def GetVersion ():
    i = 0
    Versiones = []
    f = open("C:/Users/Mijail/Documents/vsblty-Tool/Scripts-Extras/ListadoSoftware.txt", "r")
    while(True):
        linea = f.readline()
        i += 1
        #print (i)
        if (i == 3):
            print ("add db")
            print(str(i) + "-" + linea)
            VersionClient = linea
        if (i == 5):
            print ("add db")
            print(str(i) + "-" + linea)
            VersionService = linea
        Versiones = [VersionClient, VersionService]
        if not linea:
            break
    f.close()
    return Versiones

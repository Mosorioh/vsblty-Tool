import os
import os, sys
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil
# intérprete para operaciones de entrada y salida basadas en archivos
from io import open
# Hostname
import socket 
# Json
import json
# Date Time
import time
from datetime import date
from datetime import datetime, timedelta
import datetime 
# DB
import pymysql
# GUID
import uuid 

def RemoveFolderlog ():
    print ("*******************************************************************")
    print ("///////////////////////////////////////////////////////////////////")
    print ("- Eliminando Folder Logs and Savephotos")
    print ("///////////////////////////////////////////////////////////////////")
    print ("*******************************************************************")

    #Remover  carpeta
    try:
        # Remove path Folder KingSalmon
        PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
        rmtree(PathLog)
        print (" - La Carpeta de Logs ha sido Eliminada")
        time.sleep(.100)
        
    except FileNotFoundError:
        print (" - Folder KingSalmon No Exists")

    #Remover carpeta
    try:
        # Remove path Folder savephotos
        PathsavePhotos = "C:/ProgramData/VsbltyTmp/"
        rmtree(PathsavePhotos)
        print (" - La Carpeta de SavePhotos ha sido Eliminada")
        time.sleep(.100)
        
    except FileNotFoundError:
        print (" - Folder VsbltyTmp No Exists")


def CreateFolderBackup (GuidTest, today):
    #crear carpeta
    try:
        # change the destination path
        Fecha = str(today)[0:10]
        FolderTest = "C:/ProgramData/Vsblty-Test/Identification-Results/"  + Fecha + " - " + str(GuidTest)
        makedirs(FolderTest)
        print (" - Creating Folder of Test-", GuidTest)
    except FileExistsError:
        print (" - Folder Exists")
    
    return FolderTest

def CreateFolderCiclo (FolderTest, CicloActual):
    #crear carpeta
    try:
        # change the destination path
        NewFolderTest = FolderTest + "/CICLO"  + " -" + str(CicloActual)
        makedirs(NewFolderTest)
        print (" - Creating Folder of Result Ciclo-", CicloActual)
    except FileExistsError:
        print (" - Folder Exists")

    return NewFolderTest

def MoverFolder (FolderCiclo):
    #crear carpeta
    try:
        # change the destination path
        PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
        dirs = os.listdir(PathLog)
        for file in dirs:
            Archivo = PathLog + file
            print (" - Moviendo Archivo Log: ", Archivo)
            shutil.move(Archivo, FolderCiclo)
            time.sleep(1)
    except FileExistsError:
        print (" - Folder Exists")

    try:
        FolderSavephotos = "C:/ProgramData/VsbltyTmp/KingSalmon/"
        print (" - Moviendo Folder SavePhotos: ", FolderSavephotos)
        shutil.move(FolderSavephotos, FolderCiclo)
        time.sleep(1)
    except FileExistsError:
        print (" - folder SavePhotos No Exists") 
    
    try:
        Usage = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"
        print (" - Moviendo Folder Usage: ", Usage)
        shutil.move(Usage, FolderCiclo)
        time.sleep(1)
    except FileExistsError:
        print (" - folder Usage No Exists") 
    except FileNotFoundError:
        print (" - folder Usage No Exists") 

    
    return Archivo
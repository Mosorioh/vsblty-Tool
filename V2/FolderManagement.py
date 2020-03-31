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
    print ("")
    print ("///////////////////////////////////////////////////////////////////")
    print ("- Remove Folder From Log and Savephotos")

    #Remover  carpeta
    try:
        # Remove path Folder KingSalmon
        print (" - Removiendo Carpetas logs")
        PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
        rmtree(PathLog)
        time.sleep(.200)
        
    except FileNotFoundError:
        print (" - Folder KingSalmon No Exists")

    #Remover carpeta
    try:
        # Remove path Folder savephotos
        print (" - Removiendo Carpetas savephotos")
        PathsavePhotos = "C:/ProgramData/VsbltyTmp/"
        rmtree(PathsavePhotos)
        
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

def CreateFolderCiclo (FolderTest, CountTest):
    #crear carpeta
    try:
        # change the destination path
        NewFolderTest = FolderTest + "/CICLO"  + " -" + str(CountTest)
        makedirs(NewFolderTest)
        print (" - Creating Folder of Result Ciclo-", CountTest)
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
        print (" - Moviendo Folder SavePhotos: ", Archivo)
        shutil.move(FolderSavephotos, FolderCiclo)
        time.sleep(1)
    except FileExistsError:
        print (" - folder SavePhotos No Exists") 

    
    return Archivo
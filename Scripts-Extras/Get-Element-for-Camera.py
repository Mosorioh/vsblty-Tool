import os
import os, sys
import time
import datetime
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil

# comentario
import json
from io import open

# Date Time
from datetime import date
from datetime import datetime, timedelta
import datetime 
# DB
import pymysql

#//////////////////////////////////
# Setting
#/////////////////////////////////

Cam1 = "10.10.10.10"
Cam2 = "20.20.20.20"
Cam3 = "30.30.30.30"
Cam4 = "40.40.40.40"
FolderFrameReceived = "FrameReceived"
FolderBeforeProcessingOpenVino = "BeforeProcessingOpenVino"


#/////////////////////////////////////
# FolderFrameReceived
#//////////////////////////////////////

path= "C:/ProgramData/Vsblty-Test/Identification-Results/2020-03-29 - 3177995b-8680-47f2-8004-217a5a68eb84/2020-03-29 CICLO -3/KingSalmon/TempPhotos/" + FolderFrameReceived + "/"
dirs = os.listdir(path)
#print (dirs)
Busqueda = str(dirs)
print ("---- Elementos en Folder (Frame Received)")
print ("Total Frame en Carpeta",len(dirs))
FrameCam1 = Busqueda.count(Cam1)
FrameCam2 = Busqueda.count(Cam2)
FrameCam3 = Busqueda.count(Cam3)
FrameCam4 = Busqueda.count(Cam4)
total = FrameCam1 + FrameCam2 + FrameCam3 + FrameCam4
print ("Elementos Cam1: ", FrameCam1)
print ("Elementos Cam2: ", FrameCam2)
print ("Elementos Cam3: ", FrameCam3)
print ("Elementos Cam4: ", FrameCam4)
print ("Total: ", total)
input ()

#/////////////////////////////////////
# FolderFrameReceived
#//////////////////////////////////////

path= "C:/ProgramData/Vsblty-Test/Identification-Results/2020-03-29 - 3177995b-8680-47f2-8004-217a5a68eb84/2020-03-29 CICLO -3/KingSalmon/TempPhotos/" + FolderBeforeProcessingOpenVino + "/"
dirs = os.listdir(path)
#print (dirs)
Busqueda = str(dirs)
print ("----- Elementos en Folder (Frame Received)")
print ("Total Frame en Carpeta",len(dirs))
FrameCam1 = Busqueda.count(Cam1)
FrameCam2 = Busqueda.count(Cam2)
FrameCam3 = Busqueda.count(Cam3)
FrameCam4 = Busqueda.count(Cam4)
total = FrameCam1 + FrameCam2 + FrameCam3 + FrameCam4
print ("Elementos Cam1: ", FrameCam1)
print ("Elementos Cam2: ", FrameCam2)
print ("Elementos Cam3: ", FrameCam3)
print ("Elementos Cam4: ", FrameCam4)
print ("Total: ", total)
input ()

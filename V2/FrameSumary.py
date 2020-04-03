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


#/////////////////////////////////////
# FolderFrameReceived
#//////////////////////////////////////

def FrameReceived (TestID, GuidTest, CountTest, IpCameras):

    Folder = "FrameReceived"
    # Ruta y elementos en la carpeta FrameReceived
    from Setting import PathFolderFrameReceived
    PathOrigen = PathFolderFrameReceived
    dirs = os.listdir(PathOrigen)
    #print (dirs)

    # List Camera
    Cam1 = IpCameras[0]
    try:
        Cam2 = IpCameras[1]
    except IndexError:
        print ("Camara 2 not is Setting") 
        Cam2 = "CameraNull"
    try:
        Cam3 = IpCameras[2]
    except IndexError:
        print ("Camara 3 not is Setting") 
        Cam3 = "CameraNull"
    try:
        Cam4 = IpCameras[3]
    except IndexError:
        print ("Camara 4 not is Setting") 
        Cam4 = "CameraNull"

    

    # Buscar 
    Busqueda = str(dirs)
    TotalFrameFolder = len(dirs)
    FrameCam1 = Busqueda.count(Cam1)
    FrameCam2 = Busqueda.count(Cam2)
    FrameCam3 = Busqueda.count(Cam3)
    FrameCam4 = Busqueda.count(Cam4)
    total = FrameCam1 + FrameCam2 + FrameCam3 + FrameCam4

    FrameReceived = [TotalFrameFolder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, total]


    print ("---- Elementos en Folder (Frame Received)")
    print ("Path: ", PathOrigen)
    print (TestID)
    print (GuidTest)
    print (CountTest)
    
    print ("Total Frame en Carpeta", TotalFrameFolder)
    print ("Elementos Cam1: ", FrameCam1)
    print ("Elementos Cam2: ", FrameCam2)
    print ("Elementos Cam3: ", FrameCam3)
    print ("Elementos Cam4: ", FrameCam4)
    print ("Total: ", total)

    from AddFrameSummary import AddFrameSummary
    AddFrameSummary (TestID, GuidTest, CountTest, Folder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, total)

    return FrameReceived

def BeforeProcessing (TestID, GuidTest, CountTest, IpCameras):
    
    Folder = "BeforeProcessing"
    # Ruta y elementos en la carpeta BeforeProcessing
    from Setting import PathFolderBeforeProcessing
    PathOrigen = PathFolderBeforeProcessing
    dirs = os.listdir(PathOrigen)
    #print (dirs)

    # List Camera
    Cam1 = IpCameras[0]
    try:
        Cam2 = IpCameras[1]
    except IndexError:
        print ("Camara 2 not is Setting") 
        Cam2 = "CameraNull"
    try:
        Cam3 = IpCameras[2]
    except IndexError:
        print ("Camara 3 not is Setting") 
        Cam3 = "CameraNull"
    try:
        Cam4 = IpCameras[3]
    except IndexError:
        print ("Camara 4 not is Setting") 
        Cam4 = "CameraNull"


    # Buscar 
    Busqueda = str(dirs)
    TotalFrameFolder = len(dirs)
    FrameCam1 = Busqueda.count(Cam1)
    FrameCam2 = Busqueda.count(Cam2)
    FrameCam3 = Busqueda.count(Cam3)
    FrameCam4 = Busqueda.count(Cam4)
    total = FrameCam1 + FrameCam2 + FrameCam3 + FrameCam4

    FrameBeforeProcessing = [TotalFrameFolder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, total]


    print ("---- Elementos en Folder (Frame BeforeProcessing)")
    print ("Path: ", PathOrigen)
    print ("Total Frame en Carpeta", TotalFrameFolder)
    print ("Elementos Cam1: ", FrameCam1)
    print ("Elementos Cam2: ", FrameCam2)
    print ("Elementos Cam3: ", FrameCam3)
    print ("Elementos Cam4: ", FrameCam4)
    print ("Total: ", total)

    from AddFrameSummary import AddFrameSummary
    AddFrameSummary (TestID, GuidTest, CountTest, Folder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, total)

    return FrameBeforeProcessing

def FrameLocalPhotos (TestID, GuidTest, CountTest, IpCameras):
    
    Folder = "LocalPhotos"
    # Ruta y elementos en la carpeta BeforeProcessing
    from Setting import PathFolderFrameLocalPhotos
    PathOrigen = PathFolderFrameLocalPhotos
    dirs = os.listdir(PathOrigen)
    print ("path LocalPhotos: ", PathOrigen)

    # List Camera
    Cam1 = IpCameras[0]
    try:
        Cam2 = IpCameras[1]
    except IndexError:
        print ("Camara 2 not is Setting") 
        Cam2 = "CameraNull"
    try:
        Cam3 = IpCameras[2]
    except IndexError:
        print ("Camara 3 not is Setting") 
        Cam3 = "CameraNull"
    try:
        Cam4 = IpCameras[3]
    except IndexError:
        print ("Camara 4 not is Setting") 
        Cam4 = "CameraNull"


    # Buscar 
    Busqueda = str(dirs)
    TotalFrameFolder = len(dirs)
    FrameCam1 = Busqueda.count(Cam1)
    FrameCam2 = Busqueda.count(Cam2)
    FrameCam3 = Busqueda.count(Cam3)
    FrameCam4 = Busqueda.count(Cam4)
    #total = FrameCam1 + FrameCam2 + FrameCam3 + FrameCam4

    # LocalPhotos no tiene ip de la camara
    #FrameLocalPhotos = [TotalFrameFolder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, total]
    FrameLocalPhotos = TotalFrameFolder


    print ("---- Elementos en Folder (Frame FrameLocalPhotos)")
    print ("Path: ", PathOrigen)
    print ("Total Frame en Carpeta", TotalFrameFolder)
    print ("Elementos Cam1: ", FrameCam1)
    print ("Elementos Cam2: ", FrameCam2)
    print ("Elementos Cam3: ", FrameCam3)
    print ("Elementos Cam4: ", FrameCam4)
    print ("Total: ", FrameLocalPhotos)

    from AddFrameSummary import AddFrameSummary
    AddFrameSummary (TestID, GuidTest, CountTest, Folder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, FrameLocalPhotos)

    return FrameLocalPhotos

def FrameAfterIdentification (TestID, GuidTest, CountTest, IpCameras):
    
    Folder = "AfterIdentification"
    # Ruta y elementos en la carpeta BeforeProcessing
    from Setting import PathFolderFrameAfterIdentification
    PathOrigen = PathFolderFrameAfterIdentification
    dirs = os.listdir(PathOrigen)
    #print (dirs)

    # List Camera
    Cam1 = IpCameras[0]
    try:
        Cam2 = IpCameras[1]
    except IndexError:
        print ("Camara 2 not is Setting") 
        Cam2 = "CameraNull"
    try:
        Cam3 = IpCameras[2]
    except IndexError:
        print ("Camara 3 not is Setting") 
        Cam3 = "CameraNull"
    try:
        Cam4 = IpCameras[3]
    except IndexError:
        print ("Camara 4 not is Setting") 
        Cam4 = "CameraNull"

    # Buscar 
    Busqueda = str(dirs)
    TotalFrameFolder = len(dirs)
    FrameCam1 = Busqueda.count(Cam1)
    FrameCam2 = Busqueda.count(Cam2)
    FrameCam3 = Busqueda.count(Cam3)
    FrameCam4 = Busqueda.count(Cam4)
    total = FrameCam1 + FrameCam2 + FrameCam3 + FrameCam4

    FrameAfterIdentification = [TotalFrameFolder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, total]


    print ("---- Elementos en Folder (Frame FrameAfterIdentification)")
    print ("Path: ", PathOrigen)
    print ("Total Frame en Carpeta", TotalFrameFolder)
    print ("Elementos Cam1: ", FrameCam1)
    print ("Elementos Cam2: ", FrameCam2)
    print ("Elementos Cam3: ", FrameCam3)
    print ("Elementos Cam4: ", FrameCam4)
    print ("Total: ", total)

    from AddFrameSummary import AddFrameSummary
    AddFrameSummary (TestID, GuidTest, CountTest, Folder, FrameCam1, FrameCam2, FrameCam3, FrameCam4, total)

    return FrameAfterIdentification
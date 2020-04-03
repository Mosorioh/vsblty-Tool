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

#/////////////////////////////////////////////////////
#*****************************************************
#--------- Setting -------------
#*****************************************************
#/////////////////////////////////////////////////////



#///////////////////////////////////////////
# Fecha Actual
#///////////////////////////////////////////
today = date.today()

#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)

#///////////////////////////////////////////
# Get Hostname
#///////////////////////////////////////////
Hostname = socket.gethostname()

#///////////////////////////////////////////
# Get version
#///////////////////////////////////////////
Version = "4.20.402.1"

#///////////////////////////////////////////
# Get Identification Service
#///////////////////////////////////////////
from GetGlobalVars import EdgeDetection
EdgeDetection = EdgeDetection
if (EdgeDetection == "true"):
        IdentificationService = 1
        #   Edge = 1
if (EdgeDetection == "false"):
        IdentificationService = 0
        #   Cloud = 0


#///////////////////////////////////////////
# Get Between Pictures
#///////////////////////////////////////////
from GetGlobalVars import TimeBetweenPictures
BetweenPictures = TimeBetweenPictures

#///////////////////////////////////////////
# Get Camera Mode
#///////////////////////////////////////////
def CameraMode (PollingCamera, TotalCameraSetting):
        if (PollingCamera == "true"):              
                CameraMode = "Polling"
        if (PollingCamera == "false" and TotalCameraSetting == 1):
                CameraMode = "Simple" 
        if (PollingCamera == "false" and  TotalCameraSetting > 1):
                CameraMode = "Multiple" 

        return CameraMode


#///////////////////////////////////////////
# Get Numero de Ciclos por cada Prueba
#///////////////////////////////////////////
NumerodeCiclos = 1

#///////////////////////////////////////////
# Duracion Por Prueba
#///////////////////////////////////////////
DuracionTest = 600

#///////////////////////////////////////////
# Descripcion
#///////////////////////////////////////////
Descripcion = "(1) Dewey Static"

#///////////////////////////////////////////
# Variables con las Rutas constantes de Archivos
#///////////////////////////////////////////
PathLogs = "C:/ProgramData/Vsblty/KingSalmon/"
PathFolderBeforeProcessing = "C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/BeforeProcessingOpenVino/"
PathFolderFrameReceived = "C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/FrameReceived/"
PathFolderFrameLocalPhotos = "C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/LocalPhotos/"
PathFolderFrameAfterIdentification = "C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/AfterIdentification/"

#///////////////////////////////////////////
# Parametros de Busqueda
#///////////////////////////////////////////
BusquedaLogIdentCloud = "[CLOUD Detection][FaceAnalysis] Identified Person"
BusquedaLogIdentEdge = "[EDGE Detection] Identified Person >> Name:"
BusquedaLogError = "ERROR"

ParametroBusqueda = [BusquedaLogIdentCloud, BusquedaLogIdentEdge, BusquedaLogError]


Setting = [
        today,
        GuidTest, 
        Hostname, 
        Version, 
        IdentificationService,
        BetweenPictures, 
        CameraMode,
        NumerodeCiclos,
        DuracionTest,
        Descripcion
        ]
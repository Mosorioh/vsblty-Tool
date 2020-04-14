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

#///////////////////////////////////////////////////////////////////////////////////////////////
# Start Test
#///////////////////////////////////////////////////////////////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("")
StartTest = datetime.datetime.now()
print ("Inicio De Prueba", StartTest)
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")


#///////////////////////////////////////////////////////////////////////////////////////////////
# Asegurando que la aplicacion no se esta ejecutando antes de iniciar la prueba
#///////////////////////////////////////////////////////////////////////////////////////////////
# La siguiente Liena mata todos los procesos abierdos del Cliente
print ("")
os.system('taskkill -f -im vsb*')
print("")

#///////////////////////////////////////////////////////////////////////////////////////////////
# Detener el Servicio de Windows
#///////////////////////////////////////////////////////////////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("")
print ("Deteniendo El Servicio de Windows" )
# Siguiente linea detiene el Servicio de Windowns
os.system('net stop VisionCaptorServices')
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
print("")

#///////////////////////////////////////////////////////////////////////////////////////////////
# - Eliminar Carpeta de Logs
# - Limpiar Los de la Pruebas
#///////////////////////////////////////////////////////////////////////////////////////////////
from FolderManagement import RemoveFolderlog
RemoveFolderlog ()

#///////////////////////////////////////////////////////////////////////////////////////////////
# - Get Setting 
#///////////////////////////////////////////////////////////////////////////////////////////////
from Setting import Setting

today = Setting[0]
GuidTest = Setting[1]
Hostname = Setting[2]
VersionClient = Setting[3]
VersionService = Setting[4]
IdentificationService = Setting[6]
FaceAnalysisOptimization = Setting[7]
OVServicesType = Setting[8]
BetweenPictures = Setting[9]
Ciclos = Setting[10]
DuracionCiclo = Setting[11]
Descripcion = Setting[12]

# FaceAnalysisOptimization
if (int(FaceAnalysisOptimization) == 0):
    Optimized = "Frame Optimized"
if (int(FaceAnalysisOptimization) == 1):
    Optimized = "Time Optimized"

# ServicesType
if (int(OVServicesType) == 0):
    ServicesType = "One service per Camera"
if (int(OVServicesType) == 1):
    ServicesType = "One service per all cameras"

# //////////////////////////////////////
# Global vars "PollingCamera"
#///////////////////////////////////////
from GetGlobalVars import PollingCamera
PollingCamera = PollingCamera

# //////////////////////////////////////
# Camaras datail
#///////////////////////////////////////
from GetCamera import GetCameraList
GetCameraList = GetCameraList(PollingCamera)
TotalCameraSetting = len(GetCameraList)

# //////////////////////////////////////
# Camera Mode
#///////////////////////////////////////
from Setting import CameraMode
CameraMode = CameraMode (PollingCamera, TotalCameraSetting)

print("")
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("Setting Test")
print ("///////////////////////////////////////////////////////////////////")
print ("Date: ", today)
print ("GuidTest: ", GuidTest)
print ("Hostname: ", Hostname)
print ("Camera Mode: ", CameraMode)
print ("Cameras Config: ", TotalCameraSetting)
print ("Identification Service: ", IdentificationService)
print ("Face Analysis Optimization: ", Optimized)
print ("Services Type: ", ServicesType)
print ("Between Pictures: ", BetweenPictures)
print ("Ciclos: ", Ciclos)
print ("Duracion Ciclo: ", DuracionCiclo)
print ("Descripcion: ", Descripcion)
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

# Sleep para ver la configuracion del Cliente
print ("En 15 Segundos Comienza los ciclos de pruebas")
time.sleep(15)

#///////////////////////////////////////////////////////////////////////////////////////////////
# - Crear Registro de Test
#///////////////////////////////////////////////////////////////////////////////////////////////
from AddNewTest import addtest
addtest (GuidTest, Hostname, VersionClient, VersionService, CameraMode, TotalCameraSetting, IdentificationService, Optimized, ServicesType, BetweenPictures, Ciclos, DuracionCiclo, Descripcion)
time.sleep(5)

#///////////////////////////////////////////////////////////////////////////////////////////////
# Get Test-Id Creado segun el GUID
#///////////////////////////////////////////////////////////////////////////////////////////////
from GetTestId import GetTestId
TestID = GetTestId (GuidTest)
print("")
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("Test Id: ", TestID)
print ("Guid Test: ", GuidTest)
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

#///////////////////////////////////////////////////////////////////////////////////////////////
# Guardar Camaras Configuradas
#///////////////////////////////////////////////////////////////////////////////////////////////
print("")
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("")
print ("   -- Camera Setting")

# Get Data Cameras
# GetCameraList es un arreglo con todas las propiedades de la camara obtenidas de Global Vars

# Camera 1
Camera1 = GetCameraList[0]

# Crear Registro De la camara 1
from AddCameraTest import AddCameraTest
AddCameraTest (TestID, GuidTest, Camera1)

# Se Agrega Ip Address de la camara 1 a la Lista
IpCameras = [Camera1[4]]

# Camera 2
try:
    Camera2 = GetCameraList[1]
    # Crear Registro De la camara 2
    AddCameraTest (TestID, GuidTest, Camera2)
    IpCameras.append (Camera2[4])
    #print ("Camara Creada: ", Camera2 [0])
except IndexError:
    print (" - Camara 2 not is Setting") 

# Camera 3
try:
    Camera3 = GetCameraList[2]
    # Crear Registro De la camara 3
    AddCameraTest (TestID, GuidTest, Camera3)
    IpCameras.append (Camera3[4])
    #print ("Camara Creada: ", Camera3 [0])
except IndexError:
    print (" - Camara 3 not is Setting")

# Camera 4
try:
    Camera4 = GetCameraList[3]
    # Crear Registro De la camara 4
    AddCameraTest (TestID, GuidTest, Camera4)
    IpCameras.append (Camera4[4])
    #print ("Camara Creada: ", Camera4 [0])
except IndexError:
    print (" - Camara 4 not is Setting") 

print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

#///////////////////////////////////////////////////////////////////////////////////////////////
# Lista de cameras IP
#///////////////////////////////////////////////////////////////////////////////////////////////
print ("")
print ("List IP Address: ", IpCameras)
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

#///////////////////////////////////////////////////////////////////////////////////////////////
# Crear Carpetas Respaldo del Test
#///////////////////////////////////////////////////////////////////////////////////////////////
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

from FolderManagement import CreateFolderBackup
FolderTest = CreateFolderBackup (GuidTest, today)
print ("  - Test Folder: ", FolderTest)

print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

# **********************************************************************************************
#///////////////////////////////////////////////////////////////////////////////////////////////
# Ciclos de Pruebas
#///////////////////////////////////////////////////////////////////////////////////////////////
# **********************************************************************************************
print ("")
CicloActual = 1

while CicloActual <= Ciclos:
    print ("///////////////////////////////////////////////////////////////////")
    print ("                       New Test Cycle", CicloActual)
    print ("///////////////////////////////////////////////////////////////////")

    # Crear carpeta respaldo por cada Ciclo definido, detro de la carpeta del Test 
    from FolderManagement import CreateFolderCiclo
    FolderCiclo = CreateFolderCiclo (FolderTest, CicloActual)

    #////////////////////////////////////////
    # Start Client 
    #///////////////////////////////////////
    StartTestCliente = str(datetime.datetime.now())
    print (" - Fecha: ", today)
    print (" - Test Cycle: ", CicloActual)
    print (" - Start Client: ", StartTestCliente) 

    #///////////////////////////////////////
    # El Cliente se incia llamando a un archivo .bat  
    #///////////////////////////////////////
    os.startfile('C:\\Users/Mijail/Documents/vsblty-Tool/Scripts-Extras/Start-Client.bat')
    
    print ("")
    print ("***********************")
    print ("  -- Client is Running, Analizando Frame and people...")
    print ("************************")
    print ("")

    #///////////////////////////////////////
    # Inicia el Tiempo o duracion de cada ciclos 
    # tiempo configurado en DuracionCiclo
    #///////////////////////////////////////

    #///////////////////////////////////////
    # Take and Insert Performance Data
    #///////////////////////////////////////
    SleepTest = 0
    
    while (SleepTest < DuracionCiclo):
        # cada 15 segundos se toman los valores de Ram y CPU
        time.sleep(15)

        # Take Ram y Cpu 
        from Performance import GetProcessID, GetValueCpu, GetValueRam
        PID = GetProcessID()
        Cpu = GetValueCpu(PID)
        Ram = GetValueRam(PID)

        # Insertamos en la DB los datos de Ram y Cpu
        from AddPerformance import AddPerformance
        AddPerformance (TestID, GuidTest, CicloActual, PID, Cpu, Ram)
        #
        SleepTest = SleepTest + 15
    
    #///////////////////////////////////////
    # Close Client  
    #///////////////////////////////////////
    print ("")
    os.system('taskkill -f -im vsb*')
    print ("************************")
    StopTestCliente =  datetime.datetime.now()
    print ("  -- Stop Client", StopTestCliente)
    print ("************************")
    print ("")
    time.sleep(1)

    # **********************************************************************************************
    #///////////////////////////////////////////////////////////////////////////////////////////////
    # Analisis de Log 
    #///////////////////////////////////////////////////////////////////////////////////////////////
    # **********************************************************************************************

    #///////////////////////////////////////
    # Log Identificaciones
    # Este metodo Busca dentro del Log cuantas personas se Identificarion
    # La variable "TotalLogIdentificacion" Indica Cuantas identificaciones se tubieron en el Ciclo
    #///////////////////////////////////////
    print ("*******************************************************************")
    print ("///////////////////////////////////////////////////////////////////")
    print ("   --- LOG IDENTIFICATION")
    print ("///////////////////////////////////////////////////////////////////")
    print ("*******************************************************************")
    from AnalysisLog import AnalysisLog
    TotalLogIdentificacion = AnalysisLog (TestID, GuidTest, CicloActual, IdentificationService)

    #///////////////////////////////////////
    # Log Face Analysis Function took
    # Este metodo Busca dentro del Log cuantas veces se llamo a la funcion Face Analysis Function
    # La variable "CallFunction" Indica Cuantas se llamo a la Funcion en el Ciclo
    #///////////////////////////////////////
    print ("*******************************************************************")
    print ("///////////////////////////////////////////////////////////////////")
    print ("   --- LOG Face Analysis Function took")
    print ("///////////////////////////////////////////////////////////////////")
    print ("*******************************************************************")
    from AnalysisLogFaceAnalysisFun import AnalysisLogFaceAnalysis
    CallFunction = AnalysisLogFaceAnalysis (TestID, GuidTest, CicloActual)

    print (TotalLogIdentificacion)
    print (CallFunction)
    input ()

    CicloActual += 1
    
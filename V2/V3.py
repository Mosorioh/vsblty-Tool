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

# //////////////////////////////////////
# Detener el Servicio de Windows
#///////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("Deteniendo El Servicio de Windows" )
os.system('net stop VisionCaptorServices')
print ("///////////////////////////////////////////////////////////////////")
print ("")

# //////////////////////////////////////
# Peticiones a otros archivos
#///////////////////////////////////////
from Setting import Setting
#print ("Setting: ", Setting)

today = Setting[0]
GuidTest = Setting[1]
Hostname = Setting[2]
CameraMode = Setting[7]
IdentificationService = Setting[5]
BetweenPictures = Setting[6]
Version = Setting[3]
VersionService = Setting[4]
NumerodeCiclos = Setting[8]
DuracionTest = Setting[9]
Descripcion = Setting[10]
FaceAnalysisOptimization = Setting[11]

  
# //////////////////////////////////////
# Global vars
#///////////////////////////////////////
from GetGlobalVars import PollingCamera
PollingCamera = PollingCamera
print (PollingCamera)

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
print ("Camera Mode: ", CameraMode)


#/////////////////////////////////////////////////////////////////////////////////////
# ***************
# Proceso (1) 
# - Nuevo Registro Test
# ***************
#/////////////////////////////////////////////////////////////////////////////////////

# //////////////////////////////////////
# Crear Nuevo Registro test
#///////////////////////////////////////
from addtest import addtest
# call function addtest
addtest (today, GuidTest, Hostname, NumerodeCiclos, DuracionTest, Descripcion, Version, IdentificationService, BetweenPictures, CameraMode, TotalCameraSetting, VersionService, FaceAnalysisOptimization)

# //////////////////////////////////////
# Get Test-Id Creado segun el GUID
#///////////////////////////////////////
from GetTestId import GetTestId
# call function GetTestId
TestID = GetTestId (GuidTest)
print ("Identificacion: ", IdentificationService)
print ("Test Id: ", TestID)
#input ()


#/////////////////////////////////////////////////////////////////////////////////////
# ***************
# Proceso (1.2) 
# - Guardar Camaras Configuradas
# - 
# ***************
#/////////////////////////////////////////////////////////////////////////////////////
print ("")
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
# Camera 1
Camera1 = GetCameraList[0]
from AddCameraTest import AddCameraTest
AddCameraTest (TestID, GuidTest, Camera1)
print (Camera1)
IpCameras = [Camera1[4]]

# Camera 2
try:
    Camera2 = GetCameraList[1]
    AddCameraTest (TestID, GuidTest, Camera2)
    IpCameras.append (Camera2[4])
    print (Camera2)
except IndexError:
    print ("Camara 2 not is Setting") 

# Camera 3
try:
    Camera3 = GetCameraList[2]
    AddCameraTest (TestID, GuidTest, Camera3)
    IpCameras.append (Camera3[4])
    print (Camera3)
except IndexError:
    print ("Camara 3 not is Setting")

# Camera 4
try:
    Camera4 = GetCameraList[3]
    AddCameraTest (TestID, GuidTest, Camera4)
    IpCameras.append (Camera4[4])
    print (Camera4)
except IndexError:
    print ("Camara 4 not is Setting") 

print ("")
print ("List IP Address: ", IpCameras)

#/////////////////////////////////////////////////////////////////////////////////////
# ***************
# Proceso (2) 
# - Remover Carpeta de Log, esto para limpiar la prueba
# - Crear Carpeta de respaldo
# ***************
#/////////////////////////////////////////////////////////////////////////////////////
from FolderManagement import RemoveFolderlog
# call function RemoveFolderlog, para rever carpeta
RemoveFolderlog ()

from FolderManagement import CreateFolderBackup
# Call Funtion CreateFolderBackup
FolderTest = CreateFolderBackup (GuidTest, today)
print (FolderTest)


#/////////////////////////////////////////////////////////////////////////////////////
# ***************
# Proceso (3) 
# - Inicion de Prueba y Ciclos configurados
# - Start Client and Stop Client
# ***************
#/////////////////////////////////////////////////////////////////////////////////////
print ("")
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print (" - Datos Test")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
print ("  --- Setting Test")
print ("       - Date: ", today)
print ("       - Hostname: ", Hostname)
print ("       - Test Numero: ", TestID)
print ("       - GUID: ", GuidTest)
print ("       - Ciclos Definidos: ", NumerodeCiclos)
print ("       - Duracion por Ciclo: ", DuracionTest, "Segundos")
print ("       - Path Test: ", FolderTest)
print ("")

#////////////////////////////////////////
# Proceso (3.1) 
#///////////////////////////////////////
CountTest = 1
while CountTest <= NumerodeCiclos:
    print ("///////////////////////////////////////////////////////////////////")
    print ("                       New Test Cycle")
    print ("///////////////////////////////////////////////////////////////////")
    # Crear carpeta respaldo por cada Ciclo definido, detro de la carpeta del Test 
    from FolderManagement import CreateFolderCiclo
    # Call Funtion CreateFolderCiclo
    FolderCiclo = CreateFolderCiclo (FolderTest, CountTest)

    #////////////////////////////////////////
    # Start Client (3.2)
    #///////////////////////////////////////
    StartTestCliente = str(datetime.datetime.now())
    print (" - Fecha", today)
    print (" - Test Cycle", CountTest)
    print (" - Start Cliente", StartTestCliente) 
    #///////////////////////////////////////
    # El Cliente se incia llamando a un archivo .bat  
    #///////////////////////////////////////
    os.startfile('C:\\Users/Mijail/Documents/vsblty-Tool/Scripts-Extras/Start-Client.bat')
    
    print ("***********")
    print ("  -- Client is Running, Analizando Frame and Person...")
    print ("***********")
    #///////////////////////////////////////
    # Inicia el Tiempo de espera para cerrar el cliente (3.3)
    #///////////////////////////////////////
    #
    # En este punto se debe ingresar todas las funciones referente a pruebas mientras el
    # Cliente esta en ejecucion, Ejemplo Ram y Cpu
    #///////////////////////////////////////

    #///////////////////////////////////////
    # Take PERFORMANCE DATA
    #///////////////////////////////////////
    SleepTest = 0
    while (SleepTest < DuracionTest):
        time.sleep(15)
        from Performance import GetProcessID, GetValueCpu, GetValueRam
        PID = GetProcessID()
        Cpu = GetValueCpu(PID)
        Ram = GetValueRam(PID)
        #
        from AddPerformance import AddPerformance
        AddPerformance (TestID, GuidTest, CountTest, PID, Cpu, Ram)
        #
        SleepTest = SleepTest + 15
    
    #///////////////////////////////////////
    # Close Client  (3.4)
    #///////////////////////////////////////
    os.system('taskkill -f -im vsb*')
    StopTestCliente =  datetime.datetime.now()
    print ("  -- Stop Client", StopTestCliente)
    print ("***********")
    print ("")
    time.sleep(1)

    #///////////////////////////////////////
    # Analisis de Log  (3.5)
    #///////////////////////////////////////
    
    # Identificaciones
    print ("///// Log Identificaciones ///////")
    from AnalysisLog import AnalysisLog
    TotalFaceIdentificacion = AnalysisLog (GuidTest, IdentificationService, today, TestID, CountTest, Hostname)
    
    # Errores
    print ("///// Log Error ///////")
    from AnalysisLogError import AnalysisLogError
    TotalError = AnalysisLogError (TestID, GuidTest, CountTest, Hostname, Version)

    # Emails
    print ("///// Log Emails ///////")
    from AnalysisLogEmails import AnalysisLogEmails
    TotalEmails = AnalysisLogEmails (TestID, GuidTest, CountTest)

    # Face Analysis Function took
    print ("///// Log Face Analysis Function took ///////")
    from AnalysisLogFaceAnalysisFun import AnalysisLogFaceAnalysis
    AnalysisLogFaceAnalysis (TestID, GuidTest, CountTest)

    #/////////////////////////////////////////////////////
    # Frame Summary 3.6 
    # Frame en FrameReceived
    # Frame en BeforeProcessing
    #/////////////////////////////////////////////////////
    
    # Frame en FrameReceived
    from FrameSumary import FrameReceived
    TotalFrameReceived = FrameReceived (TestID, GuidTest, CountTest, IpCameras)

    # Frame en BeforeProcessing
    from FrameSumary import BeforeProcessing
    TotalBeforeProcessing = BeforeProcessing (TestID, GuidTest, CountTest, IpCameras)

    # Frame en BeforeProcessing
    from FrameSumary import FrameLocalPhotos
    TotalFrameLocalPhotos = FrameLocalPhotos (TestID, GuidTest, CountTest, IpCameras)
    
    # Frame en AfterIdentification
    from FrameSumary import FrameAfterIdentification
    TotalFrameAfterIdentification = FrameAfterIdentification (TestID, GuidTest, CountTest, IpCameras)

    print ("")
    print ("/////////////////////////////////////////////////////////")
    print ("Total Face Identificacion", TotalFaceIdentificacion)
    print ("Total Frame Received", TotalFrameReceived)
    print ("Total Frame Before-Processing", TotalBeforeProcessing)

    # get Ave de CPU y Ram
    from GetAverage import AveragePerformance
    Average = AveragePerformance (TestID)
    CpuAvg = Average[0]
    RamAvg = Average[1]

    #////////////////////////////////////////////////////
    # *******************
    # process Analisi json File Metricas
    # *******************
    #///////////////////////////////////////////////////
    from AnalysisJsonMetrics import AnalysisJsonMetrics
    JsonFileData = AnalysisJsonMetrics(TestID, GuidTest, CountTest)
    TotalFilesGenerados = JsonFileData[0]
    TotalFileMetricsIdentification = JsonFileData[1]
    TotalFIleSinPersonEngagements = JsonFileData[2]

    #///////////////////////////////////////////////////
    # Insertar resultados tptales CycleSummary DB
    from AddCycleSummary import addCycleSummary
    addCycleSummary (TestID, GuidTest, CountTest, TotalFaceIdentificacion, TotalFrameReceived[0], TotalBeforeProcessing[0], TotalError, TotalFrameLocalPhotos, TotalFrameAfterIdentification[0], CpuAvg, RamAvg, TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements, TotalEmails)
    #input()

    #/////////////////////////////////////////////////////
    # Frame Summary 3.7
    # Respaldar Archivo 
    #/////////////////////////////////////////////////////
    print ("")
    print ("*****************************************************************")
    print ("/////////////////////////////////////////////////////////////////////////////////")
    print (" - Respaldar Archivos generados en el ciclo de prueba-", CountTest)
    print ("/////////////////////////////////////////////////////////////////////////////////")
    print ("*****************************************************************")
    print ("------ Mover Process LOG -----")    
    print ("/////////////////////////////////////////////////////////////////////////////////")
    # Mover Carpeta
    from FolderManagement import MoverFolder
    MoverFolder (FolderCiclo)
    print ("/////////////////////////////////////////////////////////////////////////////////")


    #///////////////////////////////////////
    # Ciclo + 1
    #///////////////////////////////////////
    CountTest +=1
    print("")
    #print("Ciclo", CountTest)
    #///////////////////////////////////////
    # Fin de ciclo, 
    #///////////////////////////////////////
    print ("")
    print ("///////////////////////////////////////////////////////////////////////////////")
    print (" - Sleep de 5 Segundo")
    print ("///////////////////////////////////////////////////////////////////////////////")
    time.sleep(5)


print ("*****************************************************************")
print ("*****************************************************************")
print ("End Task Ciclos") 
print ("*****************************************************************")
print ("*****************************************************************")

# //////////////////////////////////////
# Detener el Servicio de Windows
#///////////////////////////////////////

print ("///////////////////////////////////////////////////////////////////")
print ("Iniciando el Servicio de Windows")
os.system('net start VisionCaptorServices')
print ("///////////////////////////////////////////////////////////////////")
print ("")


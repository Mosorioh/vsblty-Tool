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
# Peticiones a otros archivos
#///////////////////////////////////////
from Setting import Setting
#print ("Setting: ", Setting)

today = Setting[0]
GuidTest = Setting[1]
Hostname = Setting[2]
CameraMode = Setting[6]
IdentificationService = Setting[4]
BetweenPictures = Setting[5]
Version = Setting[3]
NumerodeCiclos = Setting[7]
DuracionTest = Setting[8]
Descripcion = Setting[9]
Recurso = 2
  
# //////////////////////////////////////
# Camaras datail
#///////////////////////////////////////
from Cameras import Cameras
print ("Cameras", Cameras) 

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
addtest (today, GuidTest, Hostname, NumerodeCiclos, DuracionTest, Descripcion, Recurso, Version, IdentificationService, BetweenPictures, CameraMode)

# //////////////////////////////////////
# Get Test-Id Creado segun el GUID
#///////////////////////////////////////
from GetTestId import GetTestId
# call function GetTestId
TestID = GetTestId (GuidTest)
print ("Test Id: ", TestID)

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

    SleepTest = 0
    while (SleepTest < DuracionTest):
        time.sleep(29)
        from Performance import GetProcessID, GetValueCpu, GetValueRam
        PID = GetProcessID()
        Cpu = GetValueCpu(PID)
        Ram = GetValueRam(PID)
        #
        from AddPerformance import AddPerformance
        AddPerformance (TestID, GuidTest, CountTest, PID, Cpu, Ram)
        #
        SleepTest = SleepTest + 30
    
    

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
    from AnalysisLog import AnalysisLog
    TotalFaceIdentificacion = AnalysisLog (GuidTest, IdentificationService, today, TestID, CountTest, Hostname)



    #/////////////////////////////////////////////////////
    # Frame Summary 3.6 
    # Frame en FrameReceived
    # Frame en BeforeProcessing
    #/////////////////////////////////////////////////////
    
    # Frame en FrameReceived
    from FrameSumary import FrameReceived
    TotalFrameReceived = FrameReceived (TestID, GuidTest, CountTest)

    # Frame en BeforeProcessing
    from FrameSumary import BeforeProcessing
    TotalBeforeProcessing = BeforeProcessing (TestID, GuidTest, CountTest)

    # Frame en BeforeProcessing
    from FrameSumary import FrameLocalPhotos
    TotalFrameLocalPhotos = FrameLocalPhotos (TestID, GuidTest, CountTest)
    
    # Frame en AfterIdentification
    from FrameSumary import FrameAfterIdentification
    TotalFrameAfterIdentification = FrameAfterIdentification (TestID, GuidTest, CountTest)

    print ("")
    print ("/////////////////////////////////////////////////////////")
    print ("Total Face Identificacion", TotalFaceIdentificacion)
    print ("Total Frame Received", TotalFrameReceived)
    print ("Total Frame Before-Processing", TotalBeforeProcessing)

    from AddCycleSummary import addCycleSummary
    addCycleSummary (TestID, GuidTest, CountTest, TotalFaceIdentificacion, TotalFrameReceived[0], TotalBeforeProcessing[0])
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



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
# DB
import pymysql
# GUID
import uuid 
import time
from datetime import date
from datetime import datetime, timedelta
from datetime import datetime
import psutil

# DB
import pymysql
# GUID
import uuid 

Conexion = [
    "181.199.66.129",
    "Qatest",
    "Quito.2019",
    "AnalisisJson",
]
CpuList = []
RamList = []



ahora = datetime.now()
Fecha =  ahora.strftime("%Y-%m-%d")
Hora = ahora.strftime("%H-%M-%S")



#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)

Duracionminutos = input("Ingrese la duracion de la prueba en minutos: ")
Duracion =  int(Duracionminutos) * 60
print ("Duracion: ", Duracion, "Segundos")
# ///////////////////////
print ("************************************************************")
print ("Seleccione el Ecenario de Prueba: ")
print ("Modo Simple Camera = 1")
print ("Modo Multiple Camera = 2")
CameraMode = input("Seleccione: ")
CameraMode = int(CameraMode)

# //////////////////////
if (CameraMode == 1):
    print ("La Prueba se realiza en Modo Simple camera")
    FolderMode = "Simple"
    
if (CameraMode == 2):
    print ("La Prueba se realiza en Modo Multiple camera")
    FolderMode = "Multiple"

print ("Opcion Seleccionada fue:", CameraMode)
print ("Folder mode", FolderMode)




#/////////////////////////////////////////////
# Crear Folder Test
#//////////////////////////////////////////////
try:
    # change the destination path
    FolderTest = "C:/ProgramData/Vsblty-Test/Json-Test/"  + Fecha + "/" + FolderMode + " - " + GuidTest 
    makedirs(FolderTest)
    print (" - Creating Folder of Test-",  GuidTest )
except FileExistsError:
    print (" - Folder Exists")

try:
    # change the destination path
    FolderTestKingSalmon = FolderTest + "/KingSalmon/"
    FolderTestUsage = FolderTest + "/Usage/"
    makedirs(FolderTestKingSalmon)
    makedirs(FolderTestUsage)
    print (" - Creating Folder Resplados")

except FileExistsError:
    print (" - Folder Exists")

#///////////////////////////////////////////////////////////////////////////////////////////////
# Start Test
#///////////////////////////////////////////////////////////////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("")
print ("Inicio De Prueba", ahora)
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")



#///////////////////////////////////////////////////////////////////////////////////////////////
# Asegurando que la aplicacion no se esta ejecutando antes de iniciar la prueba
#///////////////////////////////////////////////////////////////////////////////////////////////
# La siguiente Liena mata todos los procesos abierdos del Cliente
print ("")
os.system('taskkill -f -im vsb*')
time.sleep(3)
print("")


#///////////////////////////////////////////////////////////////////////////////////////////////
#Remover  carpeta
#///////////////////////////////////////////////////////////////////////////////////////////////
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
    PathsavePhotos = "C:/ProgramData/VsbltyTmp/25"
    rmtree(PathsavePhotos)
    print (" - La Carpeta de SavePhotos ha sido Eliminada")
    time.sleep(.100)
    
except FileNotFoundError:
    print (" - Folder VsbltyTmp No Exists")

#Remover carpeta
try:
    # Remove path Folder savephotos
    PathsavePhotos = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"
    rmtree(PathsavePhotos)
    print (" - La Carpeta de Usage ha sido Eliminada")
    time.sleep(.100)
    
except FileNotFoundError:
    print (" - Folder Usage No Exists")

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

#///////////////////////////////////////
# El Cliente se incia llamando a un archivo .bat  
#///////////////////////////////////////
os.startfile('C:/Start-Client.bat')

#//////////////////////////////////////////////////////////////
# Process ID
# ////////////////////////////////////////////////////////////
def GetProcessID ():
    try:
        # Definimos el nombre de la Aplicacion que deseamos obtener el PID
        process_name = "Vsblty.VisionCaptor.exe"
        pid = None
        while pid == None:
            for proc in psutil.process_iter():
                if process_name in proc.name():
                    pid = proc.pid
        return pid
    except ProcessLookupError:
        print ("Error al obtener ID, App not Run")

#//////////////////////////////////////////////////////////////
# Process CPU
# ////////////////////////////////////////////////////////////
def GetValueCpu (PID):
    p = psutil.Process(PID)
    p_cpu = p.cpu_percent(interval=1)/10
    CpuValue = (p_cpu * 2.7) # 3.5 y 3 fue una prueba mas exacta
    CPU = int(CpuValue)
    return CPU

#//////////////////////////////////////////////////////////////
# Process RAM
# ////////////////////////////////////////////////////////////
def GetValueRam (PID):

    py = psutil.Process(PID)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
    memoryUseValue = memoryUse*1000
    MemoryUse = int(memoryUseValue)
    return MemoryUse


#///////////////////////////////////////
# Take and Insert Performance Data
#///////////////////////////////////////
SleepTest = 0

while (SleepTest < Duracion):
    # cada 15 segundos se toman los valores de Ram y CPU
    time.sleep(15)

    # Take Ram y Cpu 

    PID = GetProcessID()
    Cpu = GetValueCpu(PID)
    Ram = GetValueRam(PID)

    if (Cpu > 100):
        Cpu = 100

    RamList.append(Ram)
    CpuList.append(Cpu)

    print ("Performance Data Taken in: ",  ahora, " - Ram: ",Ram, "MB")
    SleepTest = SleepTest + 15

print ("")
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print ("")
print ("Ram: ", RamList)
print ("Valor Maximo Ram: ", max(RamList))
AvgRam = sum(RamList) / len(RamList)
# Printing average of the list 
print("Average Ram =", round(AvgRam, 2)) 
print ("///////////////////////////////////////")
print ("Cpu: ", CpuList)
print ("Valor Maximo Cpu: ", max(CpuList))
AvgCpu = sum(CpuList) / len(CpuList)
# Printing average of the list 
print("Average Cpu =", round(AvgCpu, 2)) 
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")



  



#///////////////////////////////////////
# Close Client  
#///////////////////////////////////////
ahora = datetime.now()
print ("")
os.system('taskkill -f -im vsb*')
print ("************************")
print ("  -- Stop Client", ahora)
print ("************************")
print ("")

#///////////////////////////////////////
# Mover Folder Log
#///////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print ("")
try:
    # change the destination path
    PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
    dirs = os.listdir(PathLog)
    for file in dirs:
        Archivo = PathLog + file
        print (" - Copiando Archivo Log: ", Archivo)

        shutil.copy(Archivo, FolderTestKingSalmon)
        time.sleep(.100)
except FileExistsError:
    print (" - Folder Exists")

print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

#///////////////////////////////////////
# Mover Folder Usage
#///////////////////////////////////////
print ("")
try:
    # change the destination path
    PathLog = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"
    dirs = os.listdir(PathLog)
    for file in dirs:
        Archivo = PathLog + file
        print (" - Copiando Archivo Log: ", Archivo)
        
        shutil.copy(Archivo, FolderTestUsage)
        time.sleep(.100)
except FileExistsError:
    print (" - Folder Exists")

print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")
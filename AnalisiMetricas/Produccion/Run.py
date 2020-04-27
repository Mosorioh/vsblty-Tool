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

# Group listas
from itertools import groupby


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Inicializacion De variables 
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
ahora = datetime.now()
Fecha =  ahora.strftime("%Y-%m-%d")
Hora = ahora.strftime("%H-%M-%S")
CpuList = []
RamList = []

PathGlobalVars = "C:/KioskServicesMedia/Exhibit Media/GlobalVars.json"
PathMetrics = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Generamos Un GUID 
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Datos de Entrada
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Duracion
print ("************************************************************")
Duracionminutos = input("Ingrese la duracion de la prueba en minutos: ")
Duracion =  int(Duracionminutos) * 60
print ("************************************************************")
FacesEstimadas = input("Ingrese el Total de Faces Estimadas: ")
FacesEstimadas = int(FacesEstimadas)
print ("************************************************************")
IdentificacionesEstimadas = input("Ingrese el Total de Indentificaciones Estimadas: ")
IdentificacionesEstimadas = int(IdentificacionesEstimadas)
# ///////////////////////
print ("************************************************************")
print ("Seleccione el Ecenario de Prueba: ")
print ("   - Modo Simple Camera = 1")
print ("   - Modo Multiple Camera = 2")
print ("   - Modo Polling Camera = 3")
CameraMode = input("Seleccione: ")
CameraMode = int(CameraMode)
print ("************************************************************")
# //////////////////////
if (CameraMode == 1):
    print ("La Prueba se realiza en Modo Simple camera")
    FolderMode = "Simple"
    
if (CameraMode == 2):
    print ("La Prueba se realiza en Modo Multiple camera")
    FolderMode = "Multiple"

if (CameraMode == 3):
    print ("La Prueba se realiza en Modo Polling camera")
    FolderMode = "Polling"


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# GET-Endpoint-Setting
# Funcion para obtener la Configuracion del Endpoint, desde el archivo de Globalvars.json
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def Getvaribles(CameraMode, PathGlobalVars):
    #Iniciamos Lista que contendra toda la configuracion del Endpoint
    EndpointSetting = []
    with open(PathGlobalVars) as contenido:
        Globalvars = json.load(contenido)

        #encoded
        data_string = json.dumps(Globalvars)

        #Decoded
        decoded = json.loads(data_string)

        #////////////////////////////////////////////
        #
        #////////////////////////////////////////////
        EdgeDetection = str(decoded["List"][95]["Value"])
        FaceAnalysisOptimization = str(decoded["List"][93]["Value"])
        TimeBetweenPictures = str(decoded["List"][109]["Value"])
        ReocurringVisitor = str(decoded["List"][105]["Value"])
        ObjectDetection = str(decoded["List"][82]["Value"])
        NatsServer =  str(decoded["List"][74]["Value"])
        NatsServerUrl =  str(decoded["List"][75]["Value"])
        NatsSubscriber =  str(decoded["List"][73]["Value"])
        NatsSubscriberEndpoint = str(decoded["List"][72]["Value"])
        LiveEndpointData = str(decoded["List"][71]["Value"])
        Identity = str(decoded["List"][69]["Value"])
        EnticeOnly = str(decoded["List"][68]["Value"])
        SAD = str(decoded["List"][66]["Value"])
        BodyDetection = str(decoded["List"][65]["Value"])
        EmailPublisherThreshold = str(decoded["List"][56]["Value"])
        EmailPublisherExpiration = str(decoded["List"][54]["Value"])
        DemograhicDataExpiration = str(decoded["List"][53]["Value"])
        DemographicRulesTimer = str(decoded["List"][52]["Value"])
        PollingCamera = str(decoded["List"][27]["Value"])
        ContentSwappedInterval = str(decoded["List"][10]["Value"])
        ServicesType = str(decoded["List"][104]["Value"])

        # #///////////////////////
        # Camera
        # #///////////////////////
        CountCamera = 0

        CameraList = str(decoded["CameraList"])
        TotalCamaras = CameraList.count("HardwareName")
        i = 0
        while (i < TotalCamaras):
            

            CameraUse = str(decoded["CameraList"][i]["CameraUse"])

            if (CameraMode == 2 and CameraUse == "Multi_Camera"):
                CountCamera += 1

            if (CameraMode == 3 and CameraUse == "Polling_Camera"):
                CountCamera += 1
                
            i += 1

        if (CountCamera == 0):
            CountCamera = 1

        if (CameraMode == 2):
            CountCamera = CountCamera + 1 

        #///////////////////////
        # Asignamos configuracion a la Lista
        #///////////////////////
        
        EndpointSetting = [EdgeDetection, FaceAnalysisOptimization, 
        TimeBetweenPictures, ReocurringVisitor, ObjectDetection,
        NatsServer, NatsServerUrl, NatsSubscriber, NatsSubscriberEndpoint, LiveEndpointData,
        Identity, EnticeOnly, SAD, BodyDetection, EmailPublisherThreshold,
        EmailPublisherExpiration, DemograhicDataExpiration, DemographicRulesTimer, 
        PollingCamera, ContentSwappedInterval, ServicesType, CountCamera]

    return EndpointSetting

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Setting Global Vars
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    EndpointSetting = Getvaribles(CameraMode, PathGlobalVars)
except FileNotFoundError:
    print ("   -  El Archivo de Global vars no fue encontrado en el disco C")
    PathGlobalVars = "D:/KioskServicesMedia/Exhibit Media/GlobalVars.json"
    print ("     -  Buscando el el Disco D")
    EndpointSetting = Getvaribles(CameraMode, PathGlobalVars)

# ///////////////////////////////////
# Servcicio de Identificacion (Cloud o Edge)
# ///////////////////////////////////
EdgeDetection = EndpointSetting[0]
if (EdgeDetection == "true"):
        IdentificationService = 1
        Identification = "Edge"
        #   Edge = 1
if (EdgeDetection == "false"):
        IdentificationService = 0
        Identification = "Cloud"
        #   Cloud = 0

# ///////////////////////////////////
# TimeBetweenPictures
# ///////////////////////////////////
TimeBetweenPictures = EndpointSetting[2]

# ///////////////////////////////////
# Face Analysis Optimization
# ///////////////////////////////////
FaceAnalysisOptimization = int(EndpointSetting[1])

if (FaceAnalysisOptimization == 1):
        AnalysisOptimization = "Time Optimized"
        #   1 - Time Optimized       
if (FaceAnalysisOptimization == 0):
        AnalysisOptimization = "Frame Optimized"
        #   0 - Frame Optimized

# ///////////////////////////////////
# Servicio de Identificacion por Camara
# ///////////////////////////////////
OVServicesType = int(EndpointSetting[20])

if (OVServicesType == 1):
        ServicesTypeCamera = "One Service for all cameras"
        #   1 - One Service for all cameras       
if (OVServicesType == 0):
        ServicesTypeCamera = "One Service per camera"
        #   0 - One Service per camera

# ///////////////////////////////////
# ContentSwappedInterval 
# ///////////////////////////////////
ContentSwappedInterval  = EndpointSetting[19]
# convertir dato de Global Vars a Sedundo
ftr = [3600,60,1]
ContentSwappedInterval = sum([a*b for a,b in zip(ftr, map(int,ContentSwappedInterval.split(':')))])

# ///////////////////////////////////
# EmailPublisherExpiration
# ///////////////////////////////////
EmailPublisherExpiration = EndpointSetting[15]
# convertir dato de Global Vars a Sedundo
ftr = [3600,60,1]
EmailPublisherExpiration = sum([a*b for a,b in zip(ftr, map(int,EmailPublisherExpiration.split(':')))])

# ///////////////////////////////////
#  Otras Variables GLobales
# ///////////////////////////////////
EmailPublisherThreshold = EndpointSetting[14]
CountCamera  = EndpointSetting[21]

# ///////////////////////////////////
# Hostname 
# ///////////////////////////////////
Hostname = socket.gethostname()


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Print Setting Endpoint
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("")
print ("   -  Hostname: ", Hostname)
print ("   -  Servicio Identificacion: ", Identification)
print ("   -  Time Between Pictures: ", TimeBetweenPictures)
print ("   -  Face Analysis Optimization: ", AnalysisOptimization)
print ("   -  ServicesType: ", ServicesTypeCamera)
print ("   -  Json Generados Cada: (", ContentSwappedInterval, ") Segundos")
print ("   -  Envio de Email Cada: (", EmailPublisherExpiration, ") Segundos")
print ("   -  Email Publisher Threshold: ", EmailPublisherThreshold, "%")
print ("")
print ("   -  Guid Test: ", GuidTest)
print ("      -  Duration Test: ", Duracionminutos, " Minutos (", Duracion, ") Segundos")
print ("      -  Camera Mode: ", FolderMode)
print ("      -  Cameras: ", CountCamera)
print ("   -  Estimaciones: ")
print ("      -  Total de Faces Estimadas: ", FacesEstimadas)
print ("      -  Total de Identificaciones Estimadas: ", IdentificacionesEstimadas)
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Crear Folder Test
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    # change the destination path
    FolderTest = "C:/ProgramData/Vsblty-Test/Json-Test/"  + Fecha + "/" + FolderMode + " - " + GuidTest 
    makedirs(FolderTest)
    print (" - Creating Folder of Test-",  GuidTest )
    print ("   - Path Folder: ",FolderTest)
except FileExistsError:
    print (" - Folder Exists")

try:
    # change the destination path
    FolderTestKingSalmon = FolderTest + "/KingSalmon/"
    FolderTestUsage = FolderTest + "/Usage/"
    makedirs(FolderTestKingSalmon)
    makedirs(FolderTestUsage)
    print (" - Creating Folder Backup Test")
    print ("    - /KingSalmon/")
    print ("    - /Usage/")

except FileExistsError:
    print (" - Folder Exists")

print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Asegurando que la aplicacion no se esta ejecutando antes de iniciar la prueba
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print ("")
print ("   -- Verificando que la Aplicacion no esta en ejecucion")
os.system('taskkill -f -im vsb*')
# esperamos 3 segundos para validar que la aplicacion se cerro
time.sleep(3)
print("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Remover carpeta de log y json, Iniciar test de forma Limpia
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Remover carpeta Log
try:
    # Remove path Folder KingSalmon
    PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
    rmtree(PathLog)
    print (" - La Carpeta de Logs ha sido Eliminada")
    time.sleep(.100)
    
except FileNotFoundError:
    print (" - Folder KingSalmon No Exists")

# Remover carpeta Usage
try:
    # Remove path Folder savephotos
    PathsavePhotos = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"
    rmtree(PathsavePhotos)
    print (" - La Carpeta de Usage ha sido Eliminada")
    time.sleep(.100)
    
except FileNotFoundError:
    print (" - Folder Usage No Exists")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Detener el Servicio de Windows
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print ("")
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

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# El Cliente se incia llamando a un archivo .bat  
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
StartClient = datetime.now()
print ("Iniciando la Aplicaion", StartClient)
print ("  - Luego de", Duracionminutos, "Minutos la Aplicacion sera cerrada")
os.startfile('C:/Start-Client.bat')
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

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
    # Print dato Ram
    ahora = datetime.now()
    print ("Performance Data Taken in: ",  ahora, " - Ram: ",Ram, "MB")

    # En ocaciones el Cpu esta a mayor que el 100% (corregimos error)
    if (Cpu > 100):
        Cpu = 100
    # Agregamos Elementos a la Lista
    RamList.append(Ram)
    CpuList.append(Cpu)

    
    SleepTest = SleepTest + 15

print ("")
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////") 
print ("")
print ("   - Valores obtenidos de Ram: ", RamList)
print ("     - Valor Maximo Ram: ", max(RamList), "MB")
AvgRam = sum(RamList) / len(RamList)
print ("     - Average Ram =", round(AvgRam, 2), "MB") 
print ("///////////////////////////////////////")
print ("   - Vaores obtenidos de Cpu: ", CpuList)
print ("     - Valor Maximo Cpu: ", max(CpuList), "%")
AvgCpu = sum(CpuList) / len(CpuList)
print ("     - Average Cpu =", round(AvgCpu, 2), "%") 
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Close Client  
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
StoptClient = datetime.now()
print ("")
os.system('taskkill -f -im vsb*')
print ("************************")
print ("  -- Stop Client", StoptClient)
print ("************************")
print ("")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Mover Folder Log
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Mover Folder Usage
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print ("")
try:
    # change the destination path
    PathLog = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"
    dirs = os.listdir(PathLog)
    for file in dirs:
        Archivo = PathLog + file
        print (" - Copiando Archivo Json: ", Archivo)
        
        shutil.copy(Archivo, FolderTestUsage)
        time.sleep(.100)
except FileExistsError:
    print (" - Folder Exists")

print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")

def AnalysisJsonMetrics (PathMetrics):
    print ("********************************************")
    print ("******************************************************")
    print ("          Inicio Analisis de los Archivos Json Metrics")
    print ("******************************************************")
    print ("********************************************")
    # Verificar la cantidad de archivos Log que se generaron

    print ("Ruta Folder: ", PathMetrics)
    # variable dirs contiene la lista de archivos generados
    dirs = os.listdir(PathMetrics)
    #print (dirs)
    # variable (i) define el nuemro de identificaciones detectadas (item)
    

    FaceIdDetectados = 0
    FaceConDemographics = 0
    PersonasNoIdentificadas = 0 
    TotalIdentificaciones = 0
    Filetype = 0
    FileMain = 0 
    FileMultiple = 0
    FileSindemographics = 0
    PersonasDetectas = []
    FileN = 0
    File1K = 1
    
    # segun la cantidad de archivos generados (dirs) se recorre uno a uno
    for file in dirs:
        # Creamos la ruta y el archivo que vamos a trabajar
        PathFileMetrics = PathMetrics + file
        Filetype = file.find("000000000000.Usa")
        
        if (Filetype > 0):
            FileMultiple += 1
            #FiletypeR = "Multiple"
        if (Filetype < 0): 
            FileMain += 1
            #FiletypeR = "Main"


        #print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        #print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        #print ("File: ",PathFileMetrics)
        #print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        #print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")

        # 
        FileType = PathFileMetrics.find("json")
        #print (FileType)
        if  FileType > 1:

            ExcluirFIle = PathFileMetrics.find("APICallsCount")
            #print ("APICallsCount: ",ExcluirFIle)

            if ExcluirFIle > 1:
                print ("El Archivo APICallsCount no se procesara")
            else:
                

                
                #print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                # Asignar Guid para cada Archivo
                #///////////////////////////////////////////
                # Generamos Un GUID 
                #///////////////////////////////////////////

                #///////////////////////////////////////////
                with open(PathFileMetrics, ) as contenido:

                    #TotalFilesGenerados += 1
                    FileN += 1
                    

                    datajson = json.load(contenido)

                    #encoded
                    data_string = json.dumps(datajson)

                    #Decoded
                    decoded = json.loads(data_string)

                    data_string = json.dumps(datajson)



                    # ///////////////////////////////////
                    # Get data     "personEngagements"
                    # ///////////////////////////////////
                    try:
                        personEngagements = decoded["personEngagements"]
                    except:
                        personEngagements = None

                    print ("***********************************************")
                    print ("File #: ", FileN)
                    print ("Verificando si el Archivo tiene Face")
                    #print ("Person-Engagements: ", personEngagements)
                    
                    # Verificar cuantos elementos o faces hay en el archivo
                    # Si faces detectadas es igual a -1, el archivo no tiene faces 
                    FaceIds = len(personEngagements) 
                    
                   
                    if (FaceIds == 0):
                        print ("     -- El archivo no contine Faces")
                        File1K = File1K + 1
                        
                    if (FaceIds > 0):
                        
                        # Incrementamos el nuemro de facesdetetctadas 
                        # Estas faces tienen o no infromacion demografica
                        FaceIdDetectados = FaceIdDetectados + FaceIds
                        print ("     -- Face Ids en el Archivo: ",FaceIds)
                    print ("***********************************************")
                    #print (FaceIds)
                    #input ()
                    # ///////////////////////////////////
                    # Por cada FaceId detectado se realiza validaciones
                    # Bloque mas Importante, Informacion del Test
                    # ///////////////////////////////////
                    while 0 < FaceIds:

                        FaceIds = FaceIds - 1
                        Name = None
                        bioRecordId = None
                        demographics = None
                        
                        # ///////////////////////////////////
                        # Datos Demograficos
                        # ///////////////////////////////////
                        
                        try:
                            FaceId = personEngagements[FaceIds]["faceId"]
                        except:
                            FaceId = None
                            
                        # ///////////////////////////////////
                        # Datos demograficos
                        # ///////////////////////////////////
                        try:
                            demographics = personEngagements [FaceIds]["demographics"]
                            #Confidence = personEngagements [contador]["demographics"]["identificationConfidence"]
                            #age = personEngagements [contador]["demographics"]["age"]
                            #sex = personEngagements [contador]["demographics"]["sex"]
                            bioRecordId = demographics ["bioRecordId"]
                            print ("BioRecordId: ", bioRecordId)

                            # Numero de  personas detectadas con Informacion Demografica
                            FaceConDemographics += 1

                            # Personas No Identificadas
                            if bioRecordId == "00000000-0000-0000-0000-000000000000":
                                PersonasNoIdentificadas += 1
                                print ("File: ", file)

                            # Personas Identifcadas 
                            if bioRecordId != "00000000-0000-0000-0000-000000000000":
                                Name = demographics ["IdentityName"]
                                PersonasDetectas.append(Name)
                                TotalIdentificaciones += 1
                            print ("   FaceId: ", FaceId)
                            print ("   - Name: ", Name)
                            print ("     BioId: ", bioRecordId)
                            
                        except:
                            print ("Error Obteniendo datos demograficos")
                            # Numero de  Faces detectadas sin Informacion Demografica
                            FileSindemographics += 1
                            print ("File: ", file)
                            # incrementa el numero de archivos sin informacion demofrafica
                           

    #//////////////////////////////////////////////////////////////
    # Procesamiento de resultados
    #//////////////////////////////////////////////////////////////

    #print (PersonasDetectas)

    # Lista de personas que posiblemente esten en la db
    #people = ["Denver  Edge", 'El Profesor Edge', 'Nairobi Edge', 'Tokio  Edge', 'Miyagui' ]

   


    #from People import people
    #people = people
    print ("")
    #from BioRecord import people
    #people = people

    people = [
        'Patrick Beverley  Edge',
        'Lou Williams  Edge',
        'Montrezl Harrell Edge',
        'Paul George  Edge',
        'Doc Rivers',
        'Kawhi Leonard  Edge',
        '723c608d-0c9a-4c35-975d-99f7b8df1f4f',
        '10029981-e45f-4024-b8f3-68eeaf4b7736',
        'e6352538-916f-41d7-83c2-f7b780725dae',
        '7da7cf78-a1c4-421c-ab12-3b1fecc8bcbb',
        '511f79a1-fc98-4737-93f1-e47481a86e2b', 
        '4a7d16ca-6424-4276-bf54-761ed473da49',
        'El Profesor Edge',
        'Helsinki  Edge',
        'Nairobi Edge',
        'Tokio  Edge',
        '9f6fefd4-bf84-454e-b690-93a1bcf63e14',
        '236b6422-b69b-49e1-8238-2e46dad22fdb',
        'c8582854-dfd2-4a39-9111-f128e5d125e1',
        'b009f4f0-2ebe-41d7-b3dc-638c4918d97e'

    ]


    print ("Bioercord List: ", people)
    #input ()
    

    c = groupby(PersonasDetectas)
    # convertimos el Groupby en unDiccionario con las Personas agrupadas
    dic = {} 
    for k, v in c:
        dic[k] = list(v)
    dic

    # Get personas agrupadas
    values= dic.values()

    print ("")
    print ("//////////////////////////////////")
    #print ("Dic: ", dic)
    FacesIdentification = len(values)
    ListPepople = len(people)
    print ("Total de Personas Identificadas: ", FacesIdentification)
    print ("Identificaciones: ", values)
    print ("//////////////////////////////////")
    print ("")
    # Ciclo para ver las personas detectdatas y las veces que fueron detectadas
    i = 0
    Item = 1
    #while (i < FacesIdentification):
    while (i < ListPepople):
        valor = str(dic.get(people[i]))
        person = valor[2:-2]
        VecesDetectada = PersonasDetectas.count(person)
        if (VecesDetectada > 0):
            print ("**************************************************************")
            print ("Deteccion: ", Item)
            print ("Person: ",person)
            print ("Detectado: ", VecesDetectada, " Veces")
            print ("**************************************************************")
            Item = Item + 1
        #input ()
        i = i + 1
        
    print ("//////////////////////////////////////////////////////////////")
    #input ()
            
    #//////////////////////////////////////////////////////////////
    # Procesamiento de resultados
    #//////////////////////////////////////////////////////////////

    # Archivos generados
    FileMainR = FileMain  
    JsonGenerados = FileMainR + FileMultiple 
    # estimacion de faces por camara
        # para main tiene 6 caras "Clippers"
    #FacesMainEstimadas = FileMainR * 6
        # para Multiple camara se asume que son 25 json cada 10 min
    #FacesMultiEstimadas = 25 * 4


    # calculo de efectividad
    EfectividadFacesdetected = "{0:.2f}".format((FaceConDemographics * 100 / FacesEstimadas))
    #print (EfectividadFacesdetected)
    Efectividadidentidicaciones = "{0:.2f}".format((TotalIdentificaciones * 100 / IdentificacionesEstimadas))
    
    #print (Efectividadidentidicaciones)

    # ////////////////////////////////////////////////////
    # Resultados
    # ////////////////////////////////////////////////////
    print ("")
    print ("///////////////////////////////////////////////////")                     
    print ("***************************************************")
    print ("***************************************************")                   
    print ("///////////////////////////////////////////////////")
    print ("Total de Archivos Generados: ", JsonGenerados )
    print ("   -- File Main: ", FileMainR)
    print ("   -- FIle Multiple: ", FileMultiple)
    #print ("////////////////////////////////////////")
    #print ("   -- Faces para Main: ", FacesMainEstimadas)
    #print ("   -- Faces para Multiple: ", FacesMultiEstimadas)
    #print ("   -- Detecciones Estimadas: ",FacesEstimadas)
    print ("///////////////////////////////////////////////////") 
    print ("***************************************************")
    print ("///////////////////////////////////////////////////")    
    print ("----  Faces Detectadas: ", FaceIdDetectados)
    print ("////////////////////////////////////////")
    print ("  - Faces Con Demographics:    ", FaceConDemographics)
    print ("  - Faces Sin Demographics:    ", FileSindemographics)
    print ("  - La suma debe ser igual Faces Detectadas.")
    print ("////////////////////////////////////////")
    print ("  - Total Identificaciones:    ", TotalIdentificaciones)
    print ("  - Personas NO Identificadas: ", PersonasNoIdentificadas)
    print ("  - La suma debe ser igual Faces Con Demographics.")
    print ("////////////////////////////////////////")
    #print ("  - Detecciones Estimadas:         ", FacesEstimadas)
    #print ("  - Identificaciones Estimadas:    ", IdentificacionEstimada)
    print ("  - Efectividad Detecciones:       ", EfectividadFacesdetected, "%")
    print ("  - Efectividad Identificaciones:  ", Efectividadidentidicaciones, "%")
    print ("///////////////////////////////////////////////////")
    print ("  - Total File de 1K: ",File1K)
    print ("***************************************************")
    print ("***************************************************") 

    DataAnalisis = [
        JsonGenerados, 
        FileMainR, 
        FileMultiple, 
        FaceIdDetectados,
        FaceConDemographics, 
        FileSindemographics, 
        TotalIdentificaciones, 
        PersonasNoIdentificadas,
        EfectividadFacesdetected,
        Efectividadidentidicaciones]
                
                                            


                        
                    
                #JsonFileData = [TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements]

                        
    return DataAnalisis

DataAnalisis = AnalysisJsonMetrics (PathMetrics)



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Print Setting Endpoint
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print ("*******************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("")
print ("   -  Hostname: ", Hostname)
print ("   -  Servicio Identificacion: ", Identification)
print ("   -  Time Between Pictures: ", TimeBetweenPictures)
print ("   -  Face Analysis Optimization: ", AnalysisOptimization)
print ("   -  ServicesType: ", ServicesTypeCamera)
print ("   -  Json Generados Cada: (", ContentSwappedInterval, ") Segundos")
print ("   -  Envio de Email Cada: (", EmailPublisherExpiration, ") Segundos")
print ("   -  Email Publisher Threshold: ", EmailPublisherThreshold, "%")
print ("")
print ("   -  Guid Test: ", GuidTest)
print ("      -  Duration Test: ", Duracionminutos, " Minutos (", Duracion, ") Segundos")
print ("      -  Camera Mode: ", FolderMode)
print ("      -  Cameras: ", CountCamera)
print ("   -  Estimaciones: ")
print ("      -  Total de Faces Estimadas: ", FacesEstimadas)
print ("      -  Total de Identificaciones Estimadas: ", IdentificacionesEstimadas)
print ("")
print ("*******************************************************************")
print ("   -  Backup Folder: ",FolderTest)
print ("")
print ("*******************************************************************")
print ("   -  Inicio de la Aplicaion", StartClient)
print ("   -  Stop de la Aplicaion", StoptClient)
print ("")
print ("*******************************************************************")
print ("   -  Performance")
print ("")
print ("      -  RAM")
print ("         - Valores obtenidos de Ram: ", RamList)
print ("         - Valor Maximo Ram: ", max(RamList), "MB")
AvgRam = sum(RamList) / len(RamList)
print ("         - Average Ram =", round(AvgRam, 2), "MB") 
print ("")
print ("      -  CPU")
print ("         - Vaores obtenidos de Cpu: ", CpuList)
print ("         - Valor Maximo Cpu: ", max(CpuList), "%")
AvgCpu = sum(CpuList) / len(CpuList)
print ("         - Average Cpu =", round(AvgCpu, 2), "%") 
print ("")
print ("*******************************************************************")
print ("   -  Archivos Json Generados")
print ("         - Total Archivos: ", DataAnalisis[0])
print ("         - Archivos Main: ", DataAnalisis[1])
print ("         - Archivos Multiple: ", DataAnalisis[2])
print ("")
print ("*******************************************************************")
print ("   -  Faces detectadas")
print ("         - Total Faces: ", DataAnalisis[3])
print ("         - Total Faces Con Demografia: ", DataAnalisis[4])
print ("         - Total Faces Sin Demografia: ", DataAnalisis[5])
print ("")
print ("*******************************************************************")
print ("   -  Personas Identificadas")
print ("         - Total de Personas Identificadas: ", DataAnalisis[8])
print ("         - Identificaciones: ", DataAnalisis[9])
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("*******************************************************************")






input ()
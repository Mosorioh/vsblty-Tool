import json
import os, sys
from io import open
import smtplib
import pymysql.cursors
import datetime 
import time
import uuid 

#///////////////////////////////////////////
# Generamos Un GUID para Identificar la prueba
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
# Convertimos el GUID obtenido con "uuid.uuid4", en una cadena para poder guardar en la DB
# la Variable "GuidTest" define el Id de la Prueba Actual, a demas este valor es constante durante toda la prueba.
GuidTest = str(IdUnico)

#///////////////////////////////////////////
# GET-Endpoint-Setting
# Funcion para obtener la Configuracion del Endpoint, desde el archivo de Globalvars.json
#//////////////////////////////////////////
def GetEnpointSetting():
    #Iniciamos Lista que contendra toda la configuracion del Endpoint
    EndpointSetting = []
    with open("C:/KioskServicesMedia/Exhibit Media/GlobalVars.json") as contenido:
        Globalvars = json.load(contenido)

        #encoded
        data_string = json.dumps(Globalvars)

        #Decoded
        decoded = json.loads(data_string)
        #print ("--- 1 --")
        #print ('DATA:', repr(Globalvars))

        data_string = json.dumps(Globalvars)
        #print ("--- 2 --")
        #print ('JSON:', data_string)
        
        # Asignamos a una variable el resultado,
        # En el Primer elemento ["List"], es el padre de donde queremos buscar o seleccionar el valor o propiedad 
        # En el segundo elemento [0], es la propiedad que deseamos obtener
        # el tercer elemeto ["Value"], es el valor de la propiedad
        # Asignacion de Valores
        #print ("**********************************")
        #print ("--- Get Endpoint Global Vars --")
        ContentSwappedInterval = str(decoded["List"][10]["Value"])
        CameraHardwareName = str(decoded["List"][16]["Value"])
        IPAddress = str(decoded["List"][19]["Value"])
        IsPollingCamera =  str(decoded["List"][27]["Value"])
        PollingCameraInterval =  str(decoded["List"][28]["Value"])
        #SnapshotURL =  str(decoded["List"][32]["Value"])
        CollectAnalytics =  str(decoded["List"][46]["Value"])
        #ConfidenceThresholdVizsafe =  str(decoded["List"][47]["Value"])
        DemograhicDataExpirationTime =  str(decoded["List"][51]["Value"])
        EmailPublisherBioRecordExpiration  =  str(decoded["List"][52]["Value"])
        EmailPublisherIdentificationTriggerThreshold = str(decoded["List"][54]["Value"])
        EnableUseVizsafe = str(decoded["List"][58]["Value"])
        IsBodyDetectionTurnedOn = str(decoded["List"][63]["Value"])
        Sad = str(decoded["List"][64]["Value"])
        IsIdentitySearchTurnedOn = str(decoded["List"][66]["Value"])
        LiveEndpointData = str(decoded["List"][68]["Value"])
        NotificationEmailIdentifiacion = str(decoded["List"][69]["Value"])
        ObjectDetection = str(decoded["List"][71]["Value"])
        #NotificationEmailObjectDetection = str(decoded["List"][74]["Value"])
        FaceDetectionAggressiveness = str(decoded["List"][82]["Value"])
        OpenVinoFace = str(decoded["List"][83]["Value"])
        FaceDetectionModel = str(decoded["List"][84]["Value"])
        PersonDetectionType = str(decoded["List"][90]["Value"])
        ReocurringVisitor = str(decoded["List"][92]["Value"])
        #MaximumNumberOfPersonsInFRDatabase = str(decoded["List"][93]["Value"])
        #NotificationEmailReocurringVisitor = str(decoded["List"][94]["Value"])
        #TimeSendInfoToVizsafe = str(decoded["List"][96]["Value"])
        # Seleccionar informacnion de camera List
        #CameraUse = str(decoded["CameraList"][0]["CameraUse"])

        #///////////////////////
        # Asignamos configuracion a la Lista
        #///////////////////////
        EndpointSetting = [ContentSwappedInterval,CameraHardwareName, IPAddress, IsPollingCamera, PollingCameraInterval, CollectAnalytics, DemograhicDataExpirationTime, EmailPublisherBioRecordExpiration, EmailPublisherIdentificationTriggerThreshold, EnableUseVizsafe, IsBodyDetectionTurnedOn, Sad, IsIdentitySearchTurnedOn, LiveEndpointData, NotificationEmailIdentifiacion, ObjectDetection, FaceDetectionAggressiveness, OpenVinoFace, FaceDetectionModel, PersonDetectionType, ReocurringVisitor]
      
    return EndpointSetting

#///////////////////////////////////////////
# GET-Endpoint-Info
# Funcion para obtener la Informacion de Endpoint, desde el archivo de LayoutTemplate
#//////////////////////////////////////////

def getinfo():
    with open("C:/KioskServicesMedia/Exhibit Media/LayoutTemplate.json") as contenido:
        EndpointInfo = json.load(contenido)

        #encoded
        data_string = json.dumps(EndpointInfo)

        #Decoded
        decoded = json.loads(data_string)

        data_string = json.dumps(EndpointInfo)      
       
        # Asignamos a una variable el resultado,
        CustomerId = str(decoded["EndpointInfo"]["CustomerId"])
        StoreId = str(decoded["EndpointInfo"]["StoreId"])
        EndpointId = str(decoded["EndpointInfo"]["EndpointId"])
        HostName = str(decoded["EndpointInfo"]["EndpointName"])

        #///////////////////////
        # Asignamos configuracion a la Lista
        #///////////////////////
        GetInfoENdpoint  = [CustomerId, StoreId,EndpointId, HostName]
        #print (GetInfoENdpoint)
    return GetInfoENdpoint

#///////////////////////////////////////////
# GET-Version-Client
# Funcion para obtener la Version del Cliente, desde el archivo de Log
#//////////////////////////////////////////
def GetVersionClient():
    #//////////////////////////////////
	# Verificar la cantidad de archivos que existen dentro del directorio
	# Indicamos la ruta de donde se quieren leer los archivos
    path= "C:/ProgramData/Vsblty/KingSalmon/"
    dirs = os.listdir(path)
    #SearchVersion = "AppVersion"
    for file in dirs:
        ruta = "C:/ProgramData/Vsblty/KingSalmon/"
        archivo = file
        rutacompleta = ruta + archivo
        
        # La aplicaicon lee y guarada en la variable "archivo_texto" toda la informacion 
        archivo_texto=open (rutacompleta, "r")

        # Se lee Linea por linea
        lineas_texto=archivo_texto.readlines()

        #---------------- Inicio de Busqueda
        # Buscar segun el valor del parametro
        # Por cada linea se valida si contiene el Texto que fue eniado como parametro 

        for ClientLine in lineas_texto:
            if "AppVersion" in ClientLine: #busqueda por el parametro "TextLogSearch"
                AppVersion = ClientLine[138:150]

    return AppVersion

#///////////////////////////////////////////
# GET-Endpoint-Test
# Funcion para obtener de la DB, la ultima prueba que se ejecuto para el Endpoint
# Si la respuesta es Null, se TestNumero = 1
#//////////////////////////////////////////
# Connect to the database
def EndpointTest():
    getinfodos = getinfo()
    EndpointId = getinfodos[2]
    #print (EndpointId)
    connection = pymysql.connect(host='192.168.2.147',
        user='qatest',
        password='Quito.2019',
        db='tooltest',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `TestNumero` FROM `test` WHERE `EndpointId`=%s ORDER BY `TestNumero` DESC LIMIT 1"
            cursor.execute(sql, (EndpointId,))
            result = cursor.fetchone()
            #print (result)
            if result == None:
                TestNumero = 1
                #print (TestNumero)
            else:
                TestNumero = int(result.get('TestNumero')) + 1
                #print (TestNumero)
            #input ()
    finally:
        connection.close()
    return TestNumero

#/////////////////////////////////////////////////////////
AppVersion = GetVersionClient()

#/////////////////////////////////////////////////////////
GetInfoENdpoint = getinfo()

CustomerId = GetInfoENdpoint [0]
EndpointId = GetInfoENdpoint [2]
HostName = GetInfoENdpoint [3]

#/////////////////////////////////////////////////////////
EndpointSetting = GetEnpointSetting()

CameraHardwareName = EndpointSetting[1]
Pollingcamera = EndpointSetting[3]
CollectAnalytics = EndpointSetting[5]
DemograhicDataExpiration = EndpointSetting[6]
EmailExpiration = EndpointSetting[7]
EmailThreshold = EndpointSetting[8]
EnableUseVizsafe = EndpointSetting[9] 
BodyDetection = EndpointSetting[10]
Sad = EndpointSetting[11]
IdentitySearch = EndpointSetting[12]
LiveEndpointData = EndpointSetting[13]
ObjectDetection = EndpointSetting[15]
FaceDetectionAggressiveness = EndpointSetting[16]
OpenVinoFace = EndpointSetting[17]
FaceDetectionModel = EndpointSetting[18]
PersonDetectionType  = EndpointSetting[19]
ReocurringVisitor = EndpointSetting[20]

#/////////////////////////////////////////////////////////
TestNumero = EndpointTest()

DateTest = datetime.datetime.now()

#///////////////////////////////////////////
# Insert registros en la DB
# Guid, Info, Setting, Version (Tabla test)
#//////////////////////////////////////////

# Connect to the database
connection = pymysql.connect(host='192.168.2.147',
    user='qatest',
    password='Quito.2019',
    db='tooltest',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
# Create a new record
                         
        sql = "INSERT INTO `test` (`GuidTest`, `EndpointId`, `HostName`, `DateTest`, `VersionClient`, `TestNumero`, `CamaraType`,  `CollectAnalytics`,  `Pollingcamera`, `DemograhicDataExpiration`, `EmailExpiration`,  `EmailThreshold`,  `EnableUseVizsafe`, `BodyDetection`, `Sad`, `IdentitySearch`,  `LiveEndpointData`, `ObjectDetection`, `FaceDetectionAggressiveness`,  `OpenVinoFace`,  `FaceDetectionModel`, `PersonDetectionType`, `ReocurringVisitor`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (GuidTest, EndpointId, HostName, DateTest, AppVersion, TestNumero, CameraHardwareName, CollectAnalytics, Pollingcamera, DemograhicDataExpiration, EmailExpiration, EmailThreshold, EnableUseVizsafe, BodyDetection, Sad, IdentitySearch, LiveEndpointData, ObjectDetection, FaceDetectionAggressiveness, OpenVinoFace, FaceDetectionModel, PersonDetectionType, ReocurringVisitor))
        
# connection is not autocommit by default. So you must commit to save
# your changes.
        connection.commit()

finally:
    connection.close()

#////////////////////////////////////////////
# Funcion Log Search 
#///////////////////////////////////////////
def LogSearch(GuidTest, TextLogSearch, TestNumero):

	#//////////////////////////////////
	# Definimos las Lista
    LogList = []
    ItemLog = 0
    
	#//////////////////////////////////
	# Verificar la cantidad de archivos que existen dentro del directorio
	# Indicamos la ruta de donde se quieren leer los archivos
    path= "C:/ProgramData/Vsblty/KingSalmon/"
    dirs = os.listdir(path)
    #SearchVersion = "AppVersion"
    for file in dirs:
        ruta = "C:/ProgramData/Vsblty/KingSalmon/"
        archivo = file
        rutacompleta = ruta + archivo
        
        # La aplicaicon lee y guarada en la variable "archivo_texto" toda la informacion 
        archivo_texto=open (rutacompleta, "r")

        # Se lee Linea por linea
        lineas_texto=archivo_texto.readlines()

        #---------------- Inicio de Busqueda
        # Buscar segun el valor del parametro
        # Por cada linea se valida si contiene el Texto que fue eniado como parametro 

        
        for ClientLine in lineas_texto:
                #////////////////////////////////////
                if TextLogSearch in ClientLine: # busqueda por el parametro "TextLogSearch" 
					# por cada Linea que contenga el parametro sacamos
                    LogDateLine=ClientLine[:19] # Fecha Linea Log
                    LogInfo = ClientLine[38:] # Informacion del Log (Informacion de la Linea)
                    ItemLog = ItemLog + 1 # Numero de Item o Log
                    ReadFile  = [ItemLog, LogDateLine, LogInfo, TextLogSearch, archivo, AppVersion]
                    LogList.append(ReadFile)
                    #print (ReadFile)
                    #print (LogList)

                    
                    # ///////////////////////////////
                    # preparar Conexio a La DB
                    #/////////////////////////
                    #print ("Count List:", CountPesronList)
                    # Connect to the database
                    connection = pymysql.connect(host='localhost',
                        user='Qatest',
                        password='Quito.2019',
                        db='tooltest',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

                    try:
                        with connection.cursor() as cursor:
                    # Create a new record
                            
                            # ////////////////////////////
                            # Obtener Informacion de Endpoint
                            # Funcion getinfo()
                            getinfodos = getinfo()
                            CustomerId = getinfodos[0]
                            EndpointId = getinfodos[2]
                            HostName = getinfodos[3]
                            DateTest1 = datetime.datetime.now()
                            
                            
                          
                            #sql = "INSERT INTO `matchprobability` (`GuidTest`, `CustomerId`, `EndpointId`, `Hostname`, `DataTest`, `TestNumero`) VALUES (%s, %s, %s, %s, %s, %s)"
                            #cursor.execute(sql, (GuidTest, CustomerId, EndpointId, HostName, dateTest, TestNumero))
                                                        
                            sql = "INSERT INTO `error_log` (`GuidTest`, `DateTest`, `CustomerId`, `EndpointId`, `HostName`, `AppVersion`, `TestNumero`, `ErrorNumero`,  `ErrorInfo`,  `ErrorFile`, `ErrorTag`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql,(GuidTest, DateTest1, CustomerId, EndpointId, HostName, AppVersion, TestNumero, ItemLog, LogInfo, archivo, TextLogSearch))
                           
                            #cursor.execute(sql, (ErrorClient, ErrorClient, ErrorClient, ErrorClient, ErrorClient, ErrorClient, ErrorClient))


                    # connection is not autocommit by default. So you must commit to save
                    # your changes.
                            connection.commit()

                    #with connection.cursor() as cursor:
                    # Read a single record
                    #sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                    #cursor.execute(sql, ('webmaster@python.org',))
                    #result = cursor.fetchone()
                    #print(result)
                    finally:
                        connection.close()

                    
                        
    #return ReadFile
    return LogList

#////////////////////////////////////////////
# Invocar o llamar a la Funcion LogSearch [FORCED RESTART]
#///////////////////////////////////////////
ListErrors = LogSearch (GuidTest, "[Unhandled Exception][FORCED RESTART]", TestNumero)

#////////////////////////////////////////////
# Verficar Status por set de Pruebas
#///////////////////////////////////////////

#//////////////////////////////////////////
# [FORCED RESTART]
#StatusTestRESTART = "Passed"
TotalErrores = len(ListErrors)
if TotalErrores > 0:
    StatusTestRESTART = "Failed"
else:
    StatusTestRESTART = "Pass"

#////////////////////////////////////////////
# Update Status Test Por cada prueba se actualiza
# Por ahora solo esta la prueba [FORCED RESTART]
#///////////////////////////////////////////
#print (EndpointId)
connection = pymysql.connect(host='192.168.2.147',
    user='qatest',
    password='Quito.2019',
    db='tooltest',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "UPDATE `test` SET `ErroresTest` = %s WHERE `GuidTest` = %s"
        cursor.execute(sql, (StatusTestRESTART, GuidTest))
        connection.commit()

   
finally:
    connection.close()




#for ListError in ListErrors:
    #print (ListError)


input()

import os
import os, sys
import time
import datetime
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil

# Hostname
import socket 
# comentario
import json
from io import open

# Date Time
from datetime import date
from datetime import datetime, timedelta
import datetime 
# DB
import pymysql
# GUID
import uuid 


#///////////////////////////////////////////
# Generamos Un GUID para Identificar la prueba
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
# Convertimos el GUID obtenido con "uuid.uuid4", en una cadena para poder guardar en la DB
# la Variable "GuidTest" define el Id de la Prueba Actual, a demas este valor es constante durante toda la prueba.


#/////////////////////////////////////////////////////
#/////////////////////////////////////////////////////
#--------- Setting -------------
#/////////////////////////////////////////////////////
#/////////////////////////////////////////////////////

# Main Data
GuidTest = str(IdUnico)
Hostname = socket.gethostname()
#
Version = "4.20.327.2"
#
#IdentificationService = "Cloud"
IdentificationService = "Edge"
#
BetweenPictures = 1
#
CameraMode = "Simple" 
#CameraMode = "Multiple" 
#CameraMode = "Polling" 
#
DateTest = str(datetime.datetime.now())
NumerodeCiclos = 4
DuracionTest = 600
Descripcion = "(1) Videos Lebrom "
# El recurso debe ser tomado del Global vars
Recurso = "http://181.199.66.129/vsblty/Recursos/Videos/Lebron%20James.mp4"

# Data Secundary
Fecha = DateTest[0:10]
today = date.today()
CountTest = 1

#/////////////////////////////////////////////////////
#/////////////////////////////////////////////////////
# Crear registro de Pruebas
# Guid and Setting (Tabla test)
#/////////////////////////////////////////////////////
#/////////////////////////////////////////////////////

# Connect to the database
connection = pymysql.connect(host='181.199.66.129',
                            user='Qatest',
                            password='Quito.2019',
                            db='Log-identificacion',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
# Create a new record
                         
        sql = "INSERT INTO `Test` (`Fecha`, `GUID`, `Hostname`, `TotalCiclos`, `Duracion`, `Descripcion`,  `Recurso`,  `Version`,  `IdentificationService`,  `BetweenPictures`,  `CameraMode`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (DateTest, GuidTest, Hostname, NumerodeCiclos, DuracionTest, Descripcion, Recurso, Version, IdentificationService, BetweenPictures, CameraMode))
        
# connection is not autocommit by default. So you must commit to save
# your changes.
        connection.commit()
        print ("Registro test Insertado corectamente")

finally:
    connection.close()

print (GuidTest)
#input ()
#///////////////////////////////////////////
# GET-Test-Numero
# Funcion para obtener de la DB, la ultima prueba que se ejecuto 
# Si la respuesta es Null, se TestNumero = 1
#//////////////////////////////////////////
# Connect to the database
def GetTestId(GuidTest):
    #print (EndpointId)
    connection = pymysql.connect(host='181.199.66.129',
                                    user='Qatest',
                                    password='Quito.2019',
                                    db='Log-identificacion',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `Id` FROM `Test` WHERE `GUID` = %s"
            cursor.execute(sql, (GuidTest)) 
            result = cursor.fetchone()
            print ("Resultado:", result)
            TestNumero = int(result.get('Id'))
            print ("Id", TestNumero)
            #input ()
            
    finally:
        connection.close()

    return TestNumero


# Obtener el numero del test atraves de la funcion Tetsnumero
TestID = GetTestId(GuidTest)


#/////////////////////////////////////////////////////
#--------- Proceso 1 -------------
#/////////////////////////////////////////////////////
print ("")
print ("///////////////////////////////////////////////////////////////////")
print ("PROCESS (1)")
print ("///////////////////////////////////////////////////////////////////")
print ("- Remove Folder From Log and Savephotos")
print ("- Obtain test sequence (Test number)")
print ("- Verify and Create Test Backup folder (C:/ProgramData/Vsblty-Test/)")
print ("///////////////////////////////////////////////////////////////////")

#Remover  carpeta
try:
    # change the destination path
    print (" - Removiendo Carpetas logs")
    PathLog = "C:/ProgramData/Vsblty/KingSalmon/"
    rmtree(PathLog)
    time.sleep(.200)
    
except FileNotFoundError:
    print (" - Folder KingSalmon No Exists")

#Remover carpeta
try:
    # change the destination path
    print (" - Removiendo Carpetas savephotos")
    PathsavePhotos = "C:/ProgramData/VsbltyTmp/"
    rmtree(PathsavePhotos)
    
except FileNotFoundError:
    print (" - Folder VsbltyTmp No Exists")


#input ()


#crear carpeta
try:
    # change the destination path
    FolderTest = "C:/ProgramData/Vsblty-Test/Identification-Results/"  + Fecha + " - " + str(GuidTest)
    makedirs(FolderTest)
    print (" - Creating Folder of Test-", GuidTest)
except FileExistsError:
    print (" - Folder Exists")




#/////////////////////////////////////////////////////
#--------- Proceso 2 -------------
#/////////////////////////////////////////////////////
print ("")
print ("*****************************************************************")
print ("///////////////////////////////////////////////////////////////////")
print ("PROCESS (2)")
print ("///////////////////////////////////////////////////////////////////")
print (" - Inicio de Test y Ciclos")
print ("  --- Setting Test")
print ("       - Date: ", Fecha)
print ("       - Hostname: ", Hostname)
print ("       - Test Numero: ", TestID)
print ("       - GUID: ", GuidTest)
print ("       - Ciclos Definidos: ", NumerodeCiclos)
print ("       - Duracion por Ciclo: ", DuracionTest, "Segundos")
print ("")


#////////////////////////////////////////
# Iniciar el Cliente
#///////////////////////////////////////
while CountTest <= NumerodeCiclos:
    print ("///////////////////////////////////////////////////////////////////")
    print ("                       New Test Cycle")
    print ("///////////////////////////////////////////////////////////////////")
    StartTestCliente = str(datetime.datetime.now())
    #
    #crear carpeta
    try:
        # change the destination path
        NewFolderTest = FolderTest + "/"  + Fecha  + " " + "CICLO -" + str(CountTest)
        makedirs(NewFolderTest)
        print (" - Creating Folder of Result Ciclo-", CountTest)
    except FileExistsError:
        print (" - Folder Exists")

    print (" - Test Cycle", CountTest)

    #print ("Start Cliente", StartTestCliente) 
    print (" - Fecha", Fecha)

    #input ()
    # Iniciar Client
    print (" - Start Cliente", StartTestCliente)   
    os.startfile('C:\\Users/Mijail/Documents/VSBLTY-Identificacion-Log/Scripts-Extras/Start-Client.bat')
    print ("***********")
    print ("  -- Client is Running, Analizando Frame and Person...")
    print ("***********")

    
    # Tiempo de espera para cerrar el cliente
    time.sleep(DuracionTest)

    # close Client
    os.system('taskkill -f -im vsb*')
    StopTestCliente =  datetime.datetime.now()
    print ("  -- Stop Client", StopTestCliente)
    print ("***********")
    print ("")
    time.sleep(1)

    #//////////////////////////////////
	# Verificar la cantidad de archivos que existen dentro del directorio
	# Indicamos la ruta de donde se quieren leer los archivos
    path= "C:/ProgramData/Vsblty/KingSalmon/"
    dirs = os.listdir(path)
    i = 0

    print ("********************************************")
    print ("******************************************************")
    print ("          Inicio de Analisis del Log")
    print ("******************************************************")
    print ("********************************************")

    #//////////////////////////////////
	# Verificar la cantidad de archivos que existen dentro del directorio
	# Indicamos la ruta de donde se quieren leer los archivos
    #//////////////////////////////////
    for file in dirs:
        ruta = "C:/ProgramData/Vsblty/KingSalmon/"
        archivo = file
        rutacompleta = ruta + archivo
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("File: ",rutacompleta)
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        # La aplicaicon lee y guarada en la variable "archivo_texto" toda la informacion 
        archivo_texto=open (rutacompleta, "r")
        
        

        # Se lee Linea por linea
        lineas_texto=archivo_texto.readlines()

        # ////////////////////////////////////////////////////////////
        # Inicio de Busqueda
        # Por cada linea se valida si contiene el Texto que se desea encontrar 
        # Para este caso es: "[EDGE Detection] Identified Person >> Name:"
        # ////////////////////////////////////////////////////////////

        for ClientLine in lineas_texto:
            #if "[EDGE Detection] Identified Person >> Name:" in ClientLine: #busqueda por el parametro Alex Morgan Cloud
            if "[CLOUD Detection][FaceAnalysis] Identified Person" in ClientLine: #busqueda por el parametro Alex Morgan Cloud            
                # ////////////////////////////////////////////////////////////
                # Obtener la posicion de cada Propiedad
                # ////////////////////////////////////////////////////////////
                Timeline = ClientLine[0:19]

                PosicionNamePerson = ClientLine.find("Person") + 6
                PosicionPersonId = ClientLine.find("PersonId")
                PosicionGroupId  = ClientLine.find("GroupId") 
                PosicionMatchProbability = ClientLine.find("MatchProbability") 
                PosicionLocalPersistedFaceId = ClientLine.find("LocalPersistedFaceId")

                CortePersonId = PosicionPersonId + 10
                CorteGroupId = PosicionGroupId + 9 
                CorteMatchProbability = PosicionMatchProbability + 18
                CorteLocalPersistedFaceId = ClientLine.find("LocalPersistedFaceId") + 22
                Matchsincoma = CorteLocalPersistedFaceId - 25
                


                # ///////////////////////////////////////////////////////////
                # print ("PosicionNamePerson ", PosicionNamePerson)
                # print ("PosicionPersonId ", PosicionPersonId)
                # print ("PosicionGroupId ", PosicionGroupId)
                # print ("PosicionMatchProbability ", PosicionMatchProbability)
                # print ("PosicionLocalPersistedFaceId ", PosicionLocalPersistedFaceId)

                # ///////////////////////////////////////////////////////////
                #input ()
                # ///////////////////////////////////////////////////////////
                NamePerson = ClientLine[PosicionNamePerson:PosicionPersonId]
                
                PersonId = -1
                GroupId = -1
                MatchProbability = -1
                LocalPersistedFaceId = -1
            

                  
                print ("Name person:", NamePerson)
                print ("Id   person:", PersonId)
                print ("GroupId    :", GroupId)
                print ("MatchPro-2   :", MatchProbability)
                print ("LocalPer   :", LocalPersistedFaceId)
            
                #input ()
                

                # ////////////////////////////////////////////////////////////
                # Obtener el valor de cada propiedad segun la posicion
                # ///////////////////////////////////////////////////////////

                # ////////////////////////////////////////////////////////////
                # imprimir los valores encontrados en cada linea
                # ///////////////////////////////////////////////////////////
                i +=1
                print ("Date Test:         ", today)
                print ("Test Numero:       ", TestID)
                print ("Ciclo Test:        ", CountTest)
                print ("Item:              ", i)
                print ("Hostname:          ", Hostname)
                print ("File:              ", archivo)
                print ("Time:              ", Timeline)
                print ("Name:              ", NamePerson)

                print ("PersonId:          ", PersonId)
                print ("Match Probability: ", MatchProbability)
                print ("GroupId:           ", GroupId)
                print ("LocalPersistedId:  ", LocalPersistedFaceId)
                
                print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                #input ()
                
                # Connect to the database
                connection = pymysql.connect(host='181.199.66.129',
                                            user='Qatest',
                                            password='Quito.2019',
                                            db='Log-identificacion',
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor)
                try:
                    with connection.cursor() as cursor:
                # Create a new record
                                        
                        sql = "INSERT INTO `Identificacion` (`Item`, `File`, `Timeline`, `Name`, `PersonId`, `MatchProbability`, `GroupId`, `LocalPersistedId`, `TestID`, `CicloTest`, `StartCiclo`, `Hostname`, `GuidTest`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (i, archivo, Timeline, NamePerson, PersonId, MatchProbability, GroupId, LocalPersistedFaceId, TestID, CountTest, StartTestCliente, Hostname, GuidTest))
                         


                # connection is not autocommit by default. So you must commit to save
                # your changes.
                        connection.commit()

                finally:
                    connection.close()
        # Close opend file
        archivo_texto.close()

     

    # ////////////////////////////////////////////////////////////
    # Por cada Archivo dentro del directorio, se realiza un ciclo for para recorrer cada linea y verificar hits  
    # ////////////////////////////////////////////////////////////
    time.sleep(1)

    rutaFrameReceived = "C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/FrameReceived/"
    dirsFrameReceived = os.listdir(rutaFrameReceived)
    elementosFrameReceived = len(dirsFrameReceived)
    
    #
    rutaBeforeProcessing = "C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/BeforeProcessingOpenVino/"
    dirsBeforeProcessing = os.listdir(rutaBeforeProcessing)
    elementosBeforeProcessing = len(dirsBeforeProcessing)
    
    #
    rutaFaceAPIResults = "C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/Face API Results/"
    dirsFaceAPIResults = os.listdir(rutaFaceAPIResults)
    elementosFaceAPIResults = len(dirsFaceAPIResults)

    print(TestID)
    print(GuidTest)
    print(CountTest)
    print (i)
    print(elementosFrameReceived)
    print(elementosBeforeProcessing)
    print(elementosFaceAPIResults)
    #input()


    # Connect to the database
    connection = pymysql.connect(host='181.199.66.129',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
    # Create a new record
                            
            sql = "INSERT INTO `CycleSummary` (`IdTest`, `GuidTest`, `Ciclo`, `TotalIdentificacion`, `TotalFrameReceived`, `TotalBeforeProcessing`, `TotalFaceAPIResults`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, i, elementosFrameReceived, elementosBeforeProcessing, elementosFaceAPIResults))
                


    # connection is not autocommit by default. So you must commit to save
    # your changes.
            connection.commit()

    finally:
        connection.close()

    CountTest +=1

    #/////////////////////////////////////////////////////
    #--------- Proceso 3 -------------
    #/////////////////////////////////////////////////////

    print ("")
    print ("*****************************************************************")
    print ("/////////////////////////////////////////////////////////////////////////////////")
    print (" - Respaldar Archivos generados en el ciclo de prueba-", CountTest)
    print ("/////////////////////////////////////////////////////////////////////////////////")
    print ("*****************************************************************")
    print ("------ Mover Process LOG -----")    
    print ("/////////////////////////////////////////////////////////////////////////////////")
    for file in dirs:
        Archivo = path + file
        print (" - Moviendo Archivo Log: ", Archivo)
        shutil.move(Archivo, NewFolderTest)
    print ("/////////////////////////////////////////////////////////////////////////////////")
    time.sleep(1)
    print ("------ Mover Process Photos-----")
    print ("///////////////////////////////////////////////////////////////////////////////")

    #/////////////////////////////////////////////////////
    #--------- Proceso 4 -------------
    #/////////////////////////////////////////////////////

  


    print ("*****************************************************************")
    try:
        FolderSavephotos = "C:/ProgramData/VsbltyTmp/KingSalmon/"
        print (" - Moviendo Folder SavePhotos: ", Archivo)
        shutil.move(FolderSavephotos, NewFolderTest)
        time.sleep(1)
        #crear carpeta
        #print ("Creando carpetas del savephotos")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/StreamSnapshot")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/Face API Results")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/LocalDetectedBodies")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/LocalDetectedFaces")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/LocalPhotos")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/NoIdentifiedFaces")
        time.sleep(.200)
        makedirs("C:/ProgramData/VsbltyTmp/KingSalmon/TempPhotos/NoIdentifiedPhotos")
        
    except FileExistsError:
        print (" - folder SavePhotos No Exists")    


    print ("")
    print ("///////////////////////////////////////////////////////////////////////////////")
    print (" - Sleep de 5 Segundo")
    print ("///////////////////////////////////////////////////////////////////////////////")
    time.sleep(5)
    #input() 
print ("*****************************************************************")
print ("*****************************************************************")
print ("End Task Ciclos") 
print ("*****************************************************************")
print ("*****************************************************************")
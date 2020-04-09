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

PathMetrics = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"

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

    TotalIdentificaciones = 0
    Alex = 0
    Dewey = 0
    Lebrom = 0
    Darly = 0
    Lennin = 0 
    Correa = 0
    Kuzma = 0
    Kawhi = 0
    Lou = 0
    Montrezl = 0
    Patrick = 0
    Paul = 0
    Filetype = 0
    FileMain = 0 
    FileMultiple = 0
    FileSindemographics = 0
    
    # segun la cantidad de archivos generados (dirs) se recorre uno a uno
    for file in dirs:
        # Creamos la ruta y el archivo que vamos a trabajar
        PathFileMetrics = PathMetrics + file
        Filetype = file.find("000000000000.Usa")
        if (Filetype > 0):
            FileMultiple += 1
        if (Filetype < 0):
            
            FileMain += 1

        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("File: ",PathFileMetrics)
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")

        # 
        FileType = PathFileMetrics.find("json")
        #print (FileType)
        if  FileType > 1:

            ExcluirFIle = PathFileMetrics.find("APICallsCount")
            #print ("APICallsCount: ",ExcluirFIle)

            if ExcluirFIle > 1:
                print ("El Archivo APICallsCount no se procesara")
            else:
                

                JsonFileData = []
                print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                # Asignar Guid para cada Archivo
                #///////////////////////////////////////////
                # Generamos Un GUID 
                #///////////////////////////////////////////

                #///////////////////////////////////////////
                with open(PathFileMetrics, ) as contenido:

                    #TotalFilesGenerados += 1

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
                        personEngagements = 1

                    #print (personEngagements)
                    contador = len(personEngagements) - 1 # restamos uno debido a que la list comienza en 0
                    if (contador < 0):
                        FileSindemographics += 1
  

                    # verificamos cuantos Face Fueron detectados el el archivo json   


                    # ///////////////////////////////////
                    # Por cada FaceId detectado se realiza validaciones
                    # Bloque mas Importante, Informacion del Test
                    # ///////////////////////////////////
                    while 0 <= contador:
                        # ///////////////////////////////////
                        # Datos Demograficos
                        # ///////////////////////////////////
                        
                        try:
                            Face = personEngagements[contador]["faceId"]
                        except:
                            Face = None
                            

                        #print ("Face: ",Face)
                        
                        # ///////////////////////////////////
                        # Datos demograficos
                        # ///////////////////////////////////
                        try:
                            demographics = personEngagements [contador]["demographics"]
                            #bioRecordId = None
                            print (demographics)
                            print (bioRecordId)
                        except:
                            demographics = None
                            
                            

                        if (demographics == None):
                            print ("Face No tiene Informacion demografica")
                            
                            
                          
                        else:
                            TotalIdentificaciones += 1
                            bioRecordId = demographics ["bioRecordId"]
                            # ///////////////////////////////////
                            # Validacion de Name y Biorecord
                            # ///////////////////////////////////
                            if bioRecordId != "00000000-0000-0000-0000-000000000000":
                                Name = demographics ["IdentityName"]
                                if (Name == "Darly Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Darly += 1

                                if (Name == "Alex Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Alex += 1

                                if (Name == "Lenin Edge"):
                                    print ("Name: ", Name)
                                    print ("Biorecord: ", bioRecordId)
                                    Lennin += 1

                                if (Name == "Lebrom Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Lebrom += 1

                                if (Name == "Dewey Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Dewey += 1


                                if (Name == "Correa Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Correa += 1
                                
                                if (Name == "Kuzma Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Kuzma += 1
                                
                                # NBA Clipperas
                                if (Name == "Kawhi Leonard"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Kawhi += 1
                                if (Name == "Lou Williams Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Lou += 1
                                if (Name == "Montrezl Harrell Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Montrezl += 1
                                if (Name == "Patrick Beverley Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Patrick += 1
                                if (Name == "Paul George Edge"):
                                    print ("Biorecord: ", bioRecordId)
                                    print ("Name: ", Name)
                                    Paul += 1
                                                     
                            else:
                                print ("Biorecord: ", bioRecordId)
                                Name = "Unidentified Person"
                            
 
                        contador = contador - 1
                        #input () 


                        
                    
                #JsonFileData = [TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements]
    FileMainR = FileMain - 3 
    JsonGenerados = FileMainR + FileMultiple 

    print ("Total de Archivos Generados: ", JsonGenerados )
    print ("File Main: ", FileMainR)
    print ("FIle Multiple: ", FileMultiple)
    print ("Total Files Sin Informacion (1k): ", FileSindemographics)
    print ("Total Identificaciones: ", TotalIdentificaciones)
    print ("////////////////////////////////////////////")
    print ("Camera 2 --- Alex:", Alex) 
    #print ("Dewey:", Dewey)
    print ("Camera 3    --- Darly:", Darly)                   
    print ("Camera 4    --- Lebrom:", Lebrom)
    print ("Camera 4    --- kuzma:", Kuzma)
    print ("Camera 5    --- Lennin:", Lennin)
    print ("Camera 5    --- Correa:", Correa)
    print ("------ NBA ------")
    print ("Camera Main --- Kawhi:", Kawhi)                   
    print ("Camera Main --- Patrick:", Patrick)
    print ("Camera Main --- Paul:", Paul)
    print ("Camera Main --- Montrezl:", Montrezl)
    print ("Camera Main --- Lou:", Lou)

    input () 
                        
    return JsonFileData

AnalysisJsonMetrics (PathMetrics)
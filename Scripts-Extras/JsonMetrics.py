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
    PersonasDetectas = []
    
    # segun la cantidad de archivos generados (dirs) se recorre uno a uno
    for file in dirs:
        # Creamos la ruta y el archivo que vamos a trabajar
        PathFileMetrics = PathMetrics + file
        Filetype = file.find("000000000000.Usa")
        if (Filetype > 0):
            FileMultiple += 1
        if (Filetype < 0):
            
            FileMain += 1

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
                

                JsonFileData = []
                #print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
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
                            bioRecordId = None
                            #print (demographics)
                            #print (bioRecordId)
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
                                PersonasDetectas.append(Name)


  
 
                            else:
                                #print ("Biorecord: ", bioRecordId)
                                Name = "Unidentified Person"
                            
 
                        contador = contador - 1
                        #input () 


                        
                    
                #JsonFileData = [TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements]
    print ("Personas detect")
    #print (PersonasDetectas)
    Darly = PersonasDetectas.count("Darly Edge")
    Rick = PersonasDetectas.count("Rick Edge")
    Mishone = PersonasDetectas.count("Mishone Edge")
    Negan = PersonasDetectas.count("Negan Edge")
    Mague = PersonasDetectas.count("Mague Edge")
    Alex = PersonasDetectas.count("Alex Morgan Edge")
    Dewey = PersonasDetectas.count("Dewey Edge")
    Romo = PersonasDetectas.count("Romo Edge")
    Curry = PersonasDetectas.count("Curry Edge")
    Lenin = PersonasDetectas.count("Lenin Edge")
    Lebrom = PersonasDetectas.count("Lebrom Edge")
    Correa = PersonasDetectas.count("Correa Edge")
    Kuzma = PersonasDetectas.count("Kuzma Edge")
    Kawhi = PersonasDetectas.count("Kawhi Leonard")
    Lou = PersonasDetectas.count("Lou Williams Edge")
    Montrezl = PersonasDetectas.count("Montrezl Harrell Edge")
    Patrick = PersonasDetectas.count("Patrick Beverley Edge")
    Paul = PersonasDetectas.count("Paul George Edge")

    Luka = PersonasDetectas.count("Luka  Edge")
    Milka = PersonasDetectas.count("Milka  Edge")


    print ("F1 --- Darly Edge: ", Darly)
    print ("F1 --- Rick Edge: ", Rick)
    print ("F1 --- Mishone Edge: ", Mishone)
    print ("F1 --- Negan Edge: ", Negan)
    print ("F1 --- Mague Edge: ", Mague)
    print ("F2 --- Alex Edge: ", Alex)
    
    print ("F4 --- Romo Edge: ", Romo)
    print ("F5 --- Curry Edge: ", Curry)

    print ("B3 --- Lebrom Edge: ", Lebrom)
    print ("B3 --- Dewey Edge: ", Dewey)
    print ("B5 --- Luka Edge: ", Luka)
    print ("B5 --- Milka Edge: ", Milka)
    print ("////////////////////////////////////////")
    FileMainR = FileMain - 3 
    JsonGenerados = FileMainR + FileMultiple 

    print ("Total de Archivos Generados: ", JsonGenerados )
    print ("File Main: ", FileMainR)
    print ("FIle Multiple: ", FileMultiple)
    print ("Total Files Sin Informacion (1k): ", FileSindemographics)
    print ("Total Identificaciones: ", TotalIdentificaciones)
    print ("////////////////////////////////////////////")
 

    input () 
                        
    return JsonFileData

AnalysisJsonMetrics (PathMetrics)
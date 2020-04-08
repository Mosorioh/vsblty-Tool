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


def AnalysisJsonMetrics (TestID, GuidTest, CountTest):
    print ("********************************************")
    print ("******************************************************")
    print ("          Inicio Analisis de los Archivos Json Metrics")
    print ("******************************************************")
    print ("********************************************")
    # Verificar la cantidad de archivos Log que se generaron
    from Setting import PathMetrics
    print ("Ruta Folder: ", PathMetrics)
    # variable dirs contiene la lista de archivos generados
    dirs = os.listdir(PathMetrics)
    #print (dirs)
    # variable (i) define el nuemro de identificaciones detectadas (item)
    TotalFilesGenerados = 0
    TotalFileMetricsIdentification = 0
    TotalFIleSinPersonEngagements = 0
    BodyTrackingCount = 0
    TotalFaces = 0
    
    # segun la cantidad de archivos generados (dirs) se recorre uno a uno
    for file in dirs:
        # Creamos la ruta y el archivo que vamos a trabajar
        PathFileMetrics = PathMetrics + file
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
                
                IdentificacionInJson = 0
                FacesJson = 0
                JsonFileData = []
                print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                # Asignar Guid para cada Archivo
                #///////////////////////////////////////////
                # Generamos Un GUID 
                #///////////////////////////////////////////
                IdUnico = uuid.uuid4()
                GuidFile = str(IdUnico)
                
                #///////////////////////////////////////////
                with open(PathFileMetrics, ) as contenido:

                    TotalFilesGenerados += 1

                    datajson = json.load(contenido)

                    #encoded
                    data_string = json.dumps(datajson)

                    #Decoded
                    decoded = json.loads(data_string)

                    data_string = json.dumps(datajson)

                    # Get Timestamp
                    timestamp = decoded["timestamp"]
                    # Get machine
                    machine = decoded["machine"]
                    # assetName
                    assetName = decoded["assetName"]
                    # engagementType
                    try:
                        engagementType = decoded["engagementType"]
                    except:
                        engagementType = None
                    # contentType
                    contentType = decoded["contentType"]
                    #
                    camera = decoded["camera"]
                    #
                    cameraDescription  = decoded["cameraDescription"]  
                    #
                    BodyCount  = decoded["bodyCount"]
                    #
                    try:
                        BodyTracking  = decoded["bodyTracking"]
                        BodyTrackingCount  =len(BodyTracking)                      
                    except:
                        BodyTrackingCount = 0


                    # ///////////////////////////////////
                    # Get data     "personEngagements"
                    # ///////////////////////////////////
                    try:
                        personEngagements = decoded["personEngagements"]
                    except:
                        personEngagements = 1

                    #print (personEngagements)
                    contador = len(personEngagements) - 1 # restamos uno debido a que la list comienza en 0
                    print ("Contador de personEngagements", contador)
                    #input ()

                    if (contador < 0):
                        TotalFIleSinPersonEngagements += 1

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
                        try:
                            localPersistedFaceId = personEngagements[contador]["localPersistedFaceId"]
                        except:
                            localPersistedFaceId = None

                        # ///////////////////////////////////
                        # Datos demograficos
                        # ///////////////////////////////////
                        try:
                            demographics = personEngagements [contador]["demographics"]
                        except:
                            demographics = None
                            
                        identificationConfidence = ""
                        if (demographics == None):
                            print ("Face No tiene Informacion demografica")
                            age = None
                            Genero = None
                            bioRecordId = None
                            name = None
                            identificationConfidence = None


                            
                            
                        else:
                            bioRecordId = demographics ["bioRecordId"]
                            age = demographics ["age"]
                            sex = demographics ["sex"]
                            identificationConfidence
                            # ///////////////////////////////////
                            # Clasificacion de Genero
                            # ///////////////////////////////////
                            if sex == 1:
                                Genero = "Masculino"
                            else:
                                Genero = "Femenino"
                            # ///////////////////////////////////
                            # Validacion de Name y Biorecord
                            # ///////////////////////////////////
                            if bioRecordId != "00000000-0000-0000-0000-000000000000":
                                name = demographics ["IdentityName"]
                                identificationConfidence = demographics ["identificationConfidence"]
                                IdentificacionInJson += 1
                                TotalFileMetricsIdentification += 1
                            else:
                                name = "Unidentified Person"
                                identificationConfidence = None
                                
                                


                        # ///////////////////////////////////
                        # Imprimir Resultados
                        # ///////////////////////////////////
                        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
                        print ("Test Id: ", TestID)
                        print ("Guid Test: ", GuidTest)
                        print ("Ciclo: ", CountTest)
                        print ("File: ", file)
                        print ("Guid File: ", GuidFile)
                        print ("Time: ", timestamp)
                        print ("Machine: ", machine)
                        print ("assetName", assetName)
                        print ("EngagementType: ", engagementType)
                        print ("ContentType", contentType)
                        print ("FaceId: ", Face)
                        print ("LocalPersistedFaceId: ", localPersistedFaceId)
                        print ("Age: ", age)
                        print ("Genero: ", Genero)
                        print ("Person Name: ", name)
                        print ("BioRecordId: ", bioRecordId)
                        print ("Confidence: ",identificationConfidence) 
                        print ("Camera", camera)
                        print ("Camera Description", cameraDescription)

                        from AddJsonMetricsData import addJsonMetricsData
                        addJsonMetricsData (TestID, GuidTest, CountTest, machine, file, GuidFile, timestamp, assetName, engagementType, contentType, Face, localPersistedFaceId, age, Genero, name, bioRecordId, identificationConfidence, camera, cameraDescription)
                        #input ()

                        contador = contador - 1
                        TotalFaces = TotalFaces + 1
                        FacesJson = FacesJson + 1
                        
                    JsonSummary = [TestID, GuidTest, CountTest, GuidFile, file, timestamp, FacesJson, IdentificacionInJson, BodyCount, BodyTrackingCount, camera, cameraDescription, engagementType]
                    #
                    from AddJsonSummary import AddJsonSummary
                    AddJsonSummary (JsonSummary)

                        
                    
                JsonFileData = [TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements]
                        
                        
    return JsonFileData

#print (AnalysisJsonMetrics ())
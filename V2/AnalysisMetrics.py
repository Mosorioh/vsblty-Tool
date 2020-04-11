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



def AnalysisMetrics (TestID, GuidTest, CountTest):
    from Setting import OVServicesType, FaceAnalysisOptimization
    OVServicesType = OVServicesType
    FaceAnalysisOptimization = FaceAnalysisOptimization
    print ("********************************************")
    print ("******************************************************")
    print ("          Inicio Analisis de los Archivos Json Metrics")
    print ("******************************************************")
    print ("********************************************")
    # Verificar la cantidad de archivos Log que se generaron
    PathMetrics = "C:/ProgramData/Vsblty/Kiosk Framework/Usage/"

    print ("Ruta Folder: ", PathMetrics)
    # variable dirs contiene la lista de archivos generados
    dirs = os.listdir(PathMetrics)
    #print (dirs)
    # variable (i) define el nuemro de identificaciones detectadas (item)

    FaceIdDetectados = 0
    FaceConDemographics = 0
    PersonasNoIdentificadas = 0 



    TotalIdentificaciones = 0
    Alex = 0
    Dewey = 0
    Lebrom = 0
    Darly = 0
    #Lennin = 0 
    #Correa = 0
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
                

                #JsonFileData = []
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
                        personEngagements = None

                    print ("***********************************************")
                    print ("Verificando si el Archivo tiene Face")
                    #print ("Person-Engagements: ", personEngagements)
                    
                    # Verificar cuantos elementos o faces hay en el archivo
                    # Si faces detectadas es igual a -1, el archivo no tiene faces 
                    FaceIds = len(personEngagements) 
                    
                   
                    if (FaceIds == 0):
                        print ("     -- El archivo no contine Faces")
                        
                    if (FaceIds > 0):
                        
                        # Incrementamos el nuemro de facesdetetctadas 
                        # Estas faces tienen o no infromacion demografica
                        FaceIdDetectados = FaceIdDetectados + FaceIds
                        print ("     -- Face Ids en el Archivo: ",FaceIds)
                    
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
                            print (FaceId)
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
                            #print ("BioRecordId: ", bioRecordId)

                            # Numero de  personas detectadas con Informacion Demografica
                            FaceConDemographics += 1

                            # Personas No Identificadas
                            if bioRecordId == "00000000-0000-0000-0000-000000000000":
                                PersonasNoIdentificadas += 1

                            # Personas Identifcadas 
                            if bioRecordId != "00000000-0000-0000-0000-000000000000":
                                Name = demographics ["IdentityName"]
                                PersonasDetectas.append(Name)
                                TotalIdentificaciones += 1
                        except:
                            print ("Error Obteniendo datos demograficos")
                            # Numero de  Faces detectadas sin Informacion Demografica
                            FileSindemographics += 1
                            # incrementa el numero de archivos sin informacion demofrafica
                       

                        """
                        print ("***********************************************")
                        print ("FaceID: ",FaceId)
                        print ("***********************************************")
                        #print ("Demographics", demographics)
                        print ("Name: ", Name)
                        print ("BioRecordId: ", bioRecordId)
                        """
    
    # Archivos generados
    FileMainR = FileMain - 3 
    JsonGenerados = FileMainR + FileMultiple 
    # estimacion de faces por camara
        # para main tiene 6 caras "Clippers"
    FacesMainEstimadas = FileMainR * 6
        # para Multiple camara se asume que son 25 json cada 10 min
    FacesMultiEstimadas = 25 * 3
    FacesEstimadas = FacesMainEstimadas + FacesMultiEstimadas
    IdentificacionEstimada = 225

    # calculo de efectividad
    EfectividadFacesdetected = "{0:.2f}".format((FaceConDemographics * 100 / FacesEstimadas))
    #print (EfectividadFacesdetected)
    Efectividadidentidicaciones = "{0:.2f}".format((TotalIdentificaciones * 100 / IdentificacionEstimada))
    
    #print (Efectividadidentidicaciones)

    # ////////////////////////////////////////////////////
    # Resultados
    # ////////////////////////////////////////////////////
    print ("///////////////////////////////////////////////////")                     
    print ("***************************************************")
    print ("Test Id", TestID)
    print ("Guid: ", GuidTest)
    print ("Ciclo: ", CountTest)
    print ("///////////////////////////////////////////////////")                     
    print ("***************************************************")
    print ("***************************************************")                   
    print ("///////////////////////////////////////////////////")
    print ("Total de Archivos Generados: ", JsonGenerados )
    print ("   -- File Main: ", FileMainR)
    print ("   -- FIle Multiple: ", FileMultiple)
    print ("////////////////////////////////////////")
    print ("   -- Faces para Main: ", FacesMainEstimadas)
    print ("   -- Faces para Multiple: ", FacesMultiEstimadas)
    print ("   -- Detecciones Estimadas: ",FacesEstimadas)
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
    print ("  - Detecciones Estimadas:         ", FacesEstimadas)
    print ("  - Identificaciones Estimadas:    ", IdentificacionEstimada)
    print ("  - Efectividad Detecciones:       ", EfectividadFacesdetected, "%")
    print ("  - Efectividad Identificaciones:  ", Efectividadidentidicaciones, "%")
    print ("///////////////////////////////////////////////////")
    print ("***************************************************")
    print ("***************************************************") 

    from AddJsonTest import AddJsonTest
    AddJsonTest (TestID, GuidTest, CountTest, JsonGenerados, FileMainR, FileMultiple, FaceIdDetectados, FaceConDemographics,FileSindemographics, TotalIdentificaciones, PersonasNoIdentificadas, FacesEstimadas, IdentificacionEstimada, EfectividadFacesdetected, Efectividadidentidicaciones, OVServicesType, FaceAnalysisOptimization)
                
                                            


                        
                    
                #JsonFileData = [TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements]
    #input () 
    print ("////////////////////////////////////////")
    print ("Personas Detected")
    print ("////////////////////////////////////////")
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
    #Correa = PersonasDetectas.count("Correa Edge")
    Kuzma = PersonasDetectas.count("Kuzma Edge")
    Kawhi = PersonasDetectas.count("Kawhi Leonard  Edge")
    Lou = PersonasDetectas.count("Lou Williams  Edge")
    Montrezl = PersonasDetectas.count("Montrezl Harrell Edge")
    Patrick = PersonasDetectas.count("Patrick Beverley  Edge")
    Paul = PersonasDetectas.count("Paul George  Edge")
    Luka = PersonasDetectas.count("Luka  Edge")
    Milka = PersonasDetectas.count("Milka  Edge")

     # Clippers
    if (Lou > 0):
        print ("--- Lou Edge: ", Lou)
    if (Patrick > 0):
        print ("--- Patrick Edge: ", Patrick)
    if (Montrezl > 0):
        print ("--- Montrezl Edge: ", Montrezl)
    if (Paul > 0):
        print ("--- Paul Edge: ", Paul)
    if (Kawhi > 0):
        print ("--- Kawhi Edge: ", Kawhi)

    print("----------- Camera Main -----------")
    # TWD Elenco
    if (Darly > 0):
        print ("--- Darly Edge: ", Darly)
    if (Rick > 0):
        print ("--- Rick Edge: ", Rick)
    if (Mishone > 0):
        print ("--- Mishone Edge: ", Mishone)
    if (Negan > 0):
        print ("--- Negan Edge: ", Negan)
    if (Mague > 0):
        print ("--- Mague Edge: ", Mague)
    
   
    # Usa Fotbol    
    if (Alex > 0):
        print ("--- Alex Edge: ", Alex)

    # Extras
    if (Romo > 0):
        print ("--- Romo Edge: ", Romo)
    if (Curry > 0):
        print ("--- Curry Edge: ", Curry)
    if (Lebrom > 0):
        print ("--- Lebrom Edge: ", Lebrom)
    if (Dewey > 0):
        print ("--- Dewey Edge: ", Dewey)
    if (Luka > 0):
        print ("--- Luka Edge: ", Luka)
    if (Milka > 0):
        print ("--- Milka Edge: ", Milka)
    if (Kuzma > 0):
        print ("--- Kuzma Edge: ", Kuzma)
    if (Lenin > 0):
        print ("--- Lenin Edge: ", Lenin)



    #input () 
                        
    #return JsonFileData

#AnalysisMetrics (PathMetrics)
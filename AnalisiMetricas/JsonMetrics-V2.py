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
# Group listas
from itertools import groupby

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
                

                JsonFileData = []
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
        'Tokio  Edge'    
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
    FacesEstimadas = 540
    IdentificacionEstimada = 540

    # calculo de efectividad
    EfectividadFacesdetected = "{0:.2f}".format((FaceConDemographics * 100 / FacesEstimadas))
    #print (EfectividadFacesdetected)
    Efectividadidentidicaciones = "{0:.2f}".format((TotalIdentificaciones * 100 / IdentificacionEstimada))
    
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
                
                                            


                        
                    
                #JsonFileData = [TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements]
    

    input () 
                        
    return JsonFileData

AnalysisJsonMetrics (PathMetrics)
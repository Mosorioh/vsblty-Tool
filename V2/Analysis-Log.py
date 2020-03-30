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

IdentificationService = 1

def AnalysisLog (IdentificationService):

    print ("********************************************")
    print ("******************************************************")
    print ("          Inicio de Analisis del Log")
    print ("******************************************************")
    print ("********************************************")
    # Verificar la cantidad de archivos Log que se generaron
    from Setting import PathLogs
    print ("Ruta Log: ", PathLogs)
    # variable dirs contiene la lista de archivos generados
    dirs = os.listdir(PathLogs)
    # variable (i) define el nuemro de identificaciones detectadas (item)
    i = 0
    # segun la cantidad de archivos generados (dirs) se recorre uno a uno
    for file in dirs:
        # Creamos la ruta y el archivo que vamos a trabajar
        PathFileLog = PathLogs + file
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("File: ",PathFileLog)
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print ("/////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        # La aplicaicon lee y guarada en la variable "archivo_texto" toda la informacion 
        archivo_texto=open (PathFileLog, "r")
        
        # Se lee Linea por linea
        lineas_texto=archivo_texto.readlines()

        #///////////////////////////////////////////
        # Por cada linea del archivo log, buscamos el parametro
        #///////////////////////////////////////////
        from Setting import ParametroBusqueda

        for ClientLine in lineas_texto:
            #/////////////////////////////////////
            # Para cloud
            #/////////////////////////////////////
            
            if (IdentificationService == 1):
                print ("Cloud")
                if ParametroBusqueda[0] in ClientLine: 
                    print (ParametroBusqueda[0])
                    print ("ok Cloud")

            #/////////////////////////////////////
            # Para Edge
            #/////////////////////////////////////

            if (IdentificationService == 2):
                print ("Edge")
                if ParametroBusqueda[1] in ClientLine: 
                    print (ParametroBusqueda[1])
                    print ("ok Edge")
                    
                    # ////////////////////////////////////////////////////////////
                    # Obtener la posicion de cada Propiedad
                    # ////////////////////////////////////////////////////////////
                    
                    Timeline = ClientLine[0:19]
                    PosicionNamePerson = ClientLine.find("Person") + 6
                    PosicionPersonId = ClientLine.find("PersonId")
                    PosicionGroupId  = ClientLine.find("GroupId") 
                    PosicionMatchProbability = ClientLine.find("MatchProbability") 
                    #PosicionLocalPersistedFaceId = ClientLine.find("LocalPersistedFaceId")
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
                    PersonId = ClientLine[CortePersonId:PosicionGroupId]
                    GroupId = ClientLine[CorteGroupId:PosicionMatchProbability]
                    MatchProbability = ClientLine[CorteMatchProbability:Matchsincoma]
                    LocalPersistedFaceId = ClientLine[CorteLocalPersistedFaceId:-40]

                    print (i)
                    print ("Timeline:", Timeline)
                    print ("Name person:", NamePerson)
                    print ("Id   person:", PersonId)
                    print ("GroupId    :", GroupId)
                    print ("MatchPro-2   :", MatchProbability)
                    print ("LocalPer   :", LocalPersistedFaceId)
                
                    input ()
                    

                    # ////////////////////////////////////////////////////////////
                    # Obtener el valor de cada propiedad segun la posicion
                    # ///////////////////////////////////////////////////////////

  
     

    # ////////////////////////////////////////////////////////////
    # Por cada Archivo dentro del directorio, se realiza un ciclo for para recorrer cada linea y verificar hits  
    # ////////////////////////////////////////////////////////////
    time.sleep(1)
AnalysisLog (IdentificationService)
input ()
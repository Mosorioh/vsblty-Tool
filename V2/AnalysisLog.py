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

def AnalysisLog (GuidTest, IdentificationService, today, TestID, CountTest, Hostname):

    print ("********************************************")
    print ("******************************************************")
    print ("          Inicio de Analisis del Log")
    print ("******************************************************")
    print ("********************************************")
    # Verificar la cantidad de archivos Log que se generaron
    from Setting import PathLogs
    print ("Ruta Folder: ", PathLogs)
    # variable dirs contiene la lista de archivos generados
    dirs = os.listdir(PathLogs)
    # variable (i) define el nuemro de identificaciones detectadas (item)
    item = 0
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
            
            if (IdentificationService == 0):

                # Get parametro de busqueda para Cloud de Setting 
                parametro=ParametroBusqueda[0]
                from BusquedaIdentificacionCloud import Busquedacloudiden
                # Call funcion BusquedaEdgeiden analizar linea por linea
                # la funcion BusquedaEdgeiden retorna Item
                Busquedacloudiden (parametro, ClientLine)
               
            #/////////////////////////////////////
            # Para Edge
            #/////////////////////////////////////

            if (IdentificationService == 1):
                 
                # Get parametro de busqueda para edge de Setting 
                parametro=ParametroBusqueda[1]
                from BusquedaIdentificacionEdge import BusquedaEdgeiden
                # Call funcion BusquedaEdgeiden analizar linea por linea
                # la funcion BusquedaEdgeiden retorna Item
                item = BusquedaEdgeiden (GuidTest, parametro, ClientLine, today, TestID, CountTest, item, file, Hostname)
                
            

  
     

    # ////////////////////////////////////////////////////////////
    # Por cada Archivo dentro del directorio, se realiza un ciclo for para recorrer cada linea y verificar hits  
    # ////////////////////////////////////////////////////////////
    time.sleep(1)


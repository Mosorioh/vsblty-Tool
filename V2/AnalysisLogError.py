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

def AnalysisLogError (TestID, GuidTest, CountTest, Hostname, Version):

    print ("********************************************")
    print ("******************************************************")
    print ("          Inicio de Analisis del Log (Error)")
    print ("******************************************************")
    print ("********************************************")
    
    # Verificar la cantidad de archivos Log que se generaron
    from Setting import PathLogs
    print ("Ruta Folder: ", PathLogs)
    # variable dirs contiene la lista de archivos generados
    dirs = os.listdir(PathLogs)
    # variable (i) define el nuemro de identificaciones detectadas (item)
    LineaLog = 0
    print (dirs)
    print (LineaLog)
    
    # segun la cantidad de archivos generados (dirs) se recorre uno a uno
    for file in dirs:
        # Creamos la ruta y el archivo que vamos a trabajar
        PathFileLog = PathLogs + file
        print("File open")
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
        LineaLog = 0
        TotalError = 0
        for ClientLine in lineas_texto:
            Timeline = ""
            LineaLog +=1
            InfoLogerror = ""
            # Get parametro de busqueda para los Erorres en log file
            parametro  = ParametroBusqueda[2]
            # Call funcion BusquedaEdgeiden analizar linea por linea
            if parametro in ClientLine:
                Timeline = ClientLine[0:19] 
                InfoLogerror = ClientLine
                TotalError += 1
                from AddLogError import AddLogError
                AddLogError (TestID, GuidTest, CountTest, Hostname, Version, file, Timeline, LineaLog, InfoLogerror)
            

    return TotalError 


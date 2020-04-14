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

def AnalysisLogFaceAnalysis (TestID, GuidTest, CicloActual):
    
    # Verificar la cantidad de archivos Log que se generaron
    from Setting import PathLogs
    print ("Ruta Folder: ", PathLogs)
    # variable dirs contiene la lista de archivos generados
    dirs = os.listdir(PathLogs)
    # variable (i) define el nuemro de identificaciones detectadas (item)
    print (dirs)
    
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
        CallFunction = 0
        
        
        #///////////////////////////////////////////
        # Por cada linea del archivo log, buscamos el parametro
        #///////////////////////////////////////////
        from Setting import ParametroBusqueda

        for ClientLine in lineas_texto:
            
            Timeline = ""
            InfoLog = ""
            # Get parametro de busqueda para los Erorres en log file
            parametro  = ParametroBusqueda[4]
            # Call funcion BusquedaEdgeiden analizar linea por linea
            if parametro in ClientLine:
                Timeline = ClientLine[0:19] 
                InfoLog = ClientLine
                posiciontook =  ClientLine.find("took") + 5
                took = ClientLine[posiciontook:87] 
                # Completamos la cadena con una fecha X ('2020-01-01 '), solo para convertir a time
                Tookdate = '2020-01-01 ' + took
                # convertimos Tookdate en datetime
                date_time_obj = datetime.datetime.strptime(Tookdate, '%Y-%m-%d %H:%M:%S.%f')
                # tomamos el tiempo de la funcion Took ya convertido
                TookTime = date_time_obj.time()

                #print ("Time: ", Timeline)
                #print ("Log: ",InfoLog)
                print ("TookTime: ", TookTime)
                #input ()

                from AddLogFuntionTook import AddLogFuntionTook
                AddLogFuntionTook (TestID, GuidTest, CicloActual, Timeline, InfoLog, TookTime)
                CallFunction += 1
            

    return CallFunction 

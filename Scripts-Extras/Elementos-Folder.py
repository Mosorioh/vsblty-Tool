import os
import os, sys
import time
import datetime
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil

# comentario
import json
from io import open

# Date Time
from datetime import date
from datetime import datetime, timedelta
import datetime 
# DB
import pymysql




#//////////////////////////////////
# Verificar la cantidad de archivos que existen dentro del directorio
# Indicamos la ruta de donde se quieren leer los archivos
path= "C:/ProgramData/Vsblty-Test/Identification-Results/"
dirs = os.listdir(path)
elementos = len(dirs)
print (path)
print(elementos)
input()
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
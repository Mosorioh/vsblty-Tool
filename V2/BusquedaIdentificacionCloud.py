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

def Busquedacloudiden (parametro, ClientLine):
    #print ("Parametro Cloud: ", (parametro))
    if parametro in ClientLine: 
        print ("Linea: ", ClientLine)
    #print ("**********Cloud Funtion")

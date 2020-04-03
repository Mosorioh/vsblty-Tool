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

#///////////////////////////////////////////
# Get Camera Setting
#///////////////////////////////////////////
Cam1 = "10.10.10.10"
RecursoCam1 = "http://181.199.66.129/vsblty/Recursos/Videos/"

Cam2 = "20.20.20.20"
RecursoCam2 = "http://181.199.66.129/vsblty/Recursos/Videos/"

Cam3 = "30.30.30.30"
RecursoCam3 = "http://181.199.66.129/vsblty/Recursos/Videos/"

Cam4 = "40.40.40.40"
RecursoCam4 = "http://181.199.66.129/vsblty/Recursos/Videos/"

Cameras = [
    Cam1,
    RecursoCam1,
    Cam2,
    RecursoCam2,
    Cam3,
    RecursoCam3,
    Cam4,
    RecursoCam4,
    ]
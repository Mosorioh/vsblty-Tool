import os
import time
import datetime
from shutil import rmtree 
print ("Iniciando Servicio")
os.system('net start VisionCaptorServices')
print ("En 30 Segundos se detendra el servicio")
time.sleep(30)

os.system('net stop VisionCaptorServices')

input ()

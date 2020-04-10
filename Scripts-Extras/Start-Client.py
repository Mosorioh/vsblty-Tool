import os
import os, sys
import time
import datetime
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil

# Start 
print ("Start Cliente", datetime.datetime.now()) 
os.startfile('C:\\Users/Mijail/Documents/vsblty-Tool/Scripts-Extras/Start-Client.bat')

# Sleep 
time.sleep(600)

# close Client
os.system('taskkill -f -im vsb*')
StopTestCliente =  datetime.datetime.now()
print ("Stop Client", StopTestCliente)

input ()    
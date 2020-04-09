import os
import os, sys
import time
import datetime
from shutil import rmtree 
from os import makedirs
from os import remove
import shutil

# Start 
print ("Start Cliente") 
os.startfile('C:\\Users/Mijail/Documents/vsblty-Tool/Scripts-Extras/Start-Client.bat')

# Sleep 
time.sleep(3600)

# close Client
os.system('taskkill -f -im vsb*')
StopTestCliente =  datetime.datetime.now()
print ("Stop Client", StopTestCliente)

input ()    
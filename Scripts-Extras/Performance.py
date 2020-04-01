import psutil
import os, sys


#//////////////////////////////////////////////////////////////
# Process ID
# ////////////////////////////////////////////////////////////
def GetProcessID ():
    while True:
        try:
            # Definimos el nombre de la Aplicacion que deseamos obtener el PID
            process_name = "Vsblty.VisionCaptor.exe"
            pid = None
            while pid == None:
                for proc in psutil.process_iter():
                    if process_name in proc.name():
                        pid = proc.pid
            return pid
        except ProcessLookupError:
            print ("Error al obtener ID, App not Run")

# ///////////////////////////////
# Get Process Id
# ///////////////////////////////
PID = GetProcessID ()

#//////////////////////////////////////////////////////////////
# Process CPU
# ////////////////////////////////////////////////////////////
def getValueCpu (PID):
    
    p = psutil.Process(PID)
    p_cpu = p.cpu_percent(interval=1)/10
    Cpu = (p_cpu * 1.9)
    return Cpu

#//////////////////////////////////////////////////////////////
# Process RAM
# ////////////////////////////////////////////////////////////
def GetValueRam (PID):

    py = psutil.Process(PID)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think
    memoryUseValue = memoryUse*1000
    return memoryUseValue

# //////////////////////////////////
# Get CPU
CPU = int(getValueCpu(PID))
# Get Ram
MemoryUse = int(GetValueRam (PID))

print ("--------------------------------------------")
print ("PID: ", PID)
print ("--------------------------------------------")
print ("CPU: ", CPU , "%")
print ("--------------------------------------------")
print ("Ram: ", MemoryUse)

input ()


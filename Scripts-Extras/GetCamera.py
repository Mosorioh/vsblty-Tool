import json
import os, sys
from io import open

from GetGlobalVars import PollingCamera
PollingCamera = PollingCamera


#///////////////////////////////////////////
# GET-Endpoint-Setting
# Funcion para obtener la Configuracion del Endpoint, desde el archivo de Globalvars.json
#//////////////////////////////////////////
def GetEnpointSetting(PollingCamera):
    #Iniciamos Lista que contendra toda la configuracion del Endpoint
    with open("D:/KioskServicesMedia/Exhibit Media/GlobalVars.json") as contenido:
        Globalvars = json.load(contenido)

        #encoded
        data_string = json.dumps(Globalvars)

        #Decoded
        decoded = json.loads(data_string)
       
        # Asignamos a una variable el resultado,
        # En el Primer elemento ["List"], es el padre de donde queremos buscar o seleccionar el valor o propiedad 
        # En el segundo elemento [0], es la propiedad que deseamos obtener
        # el tercer elemeto ["Value"], es el valor de la propiedad
        # Asignacion de Valores
        #print ("**********************************")
        #print ("--- Get Endpoint Global Vars --")

        CameraList = str(decoded["CameraList"])
        TotalCamaras = CameraList.count("HardwareName")
        i = 0
        print ("Cameras Configuradas: ", TotalCamaras)
        Cameras = []
        Countcamera = 0
        while (i < TotalCamaras):
            
            Id = str(decoded["CameraList"][i]["Id"])
            HardwareName = str(decoded["CameraList"][i]["HardwareName"])
            CameraUse = str(decoded["CameraList"][i]["CameraUse"])
            IpCameraAddress = str(decoded["CameraList"][i]["IpCameraAddress"])
            SnapshotUrl = str(decoded["CameraList"][i]["IpCameraSnapshotUrl"])
            VideoUrl= str(decoded["CameraList"][i]["IpCameraVideoStreamUrl"])
            Description = str(decoded["CameraList"][i]["Description"])

            if (PollingCamera == "true" and  CameraUse == "Polling_Camera"):
                Countcamera += 1
                Camara = "Cam" + str(Countcamera)
                Cameras.extend ([Camara, Id, HardwareName, CameraUse, IpCameraAddress, SnapshotUrl, VideoUrl, Description])
                print ("Add Camera type Polling")
            if (PollingCamera == "false" and  CameraUse == "Multi_Camera") or (PollingCamera == "false" and  CameraUse == "Main_Camera"):
                Countcamera += 1
                Camara = "Cam" + str(Countcamera)
                Cameras.extend ([Camara, Id, HardwareName, CameraUse, IpCameraAddress, SnapshotUrl, VideoUrl, Description])
                print ("Add Camera type Multi_Camera and Main")
            i += 1
            
    return Cameras


#/////////////////////////////////////////////////////////
#CamerasList = GetEnpointSetting(PollingCamera)
#print (CamerasList)
#input()

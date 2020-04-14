import json
import os, sys
from io import open

from GetGlobalVars import PollingCamera
PollingCamera = PollingCamera



#///////////////////////////////////////////
# GET-Endpoint-Setting
# Funcion para obtener la Configuracion del Endpoint, desde el archivo de Globalvars.json
#//////////////////////////////////////////
def GetCameraList(PollingCamera):
    print ("")
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
        print ("*******************************************************************")
        print ("///////////////////////////////////////////////////////////////////")
        print ("----- Cameras Configuradas: ", TotalCamaras)
        print ("///////////////////////////////////////////////////////////////////")
        print ("*******************************************************************")
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
                Camara = Countcamera
                Cameras.extend ([Camara, Id, HardwareName, CameraUse, IpCameraAddress, SnapshotUrl, VideoUrl, Description])
                print ("    --  Add Camera type Polling")
            if (PollingCamera == "false" and  CameraUse == "Multi_Camera") or (PollingCamera == "false" and  CameraUse == "Main_Camera"):
                Countcamera += 1
                Camara = Countcamera
                Cameras.extend ([Camara, Id, HardwareName, CameraUse, IpCameraAddress, SnapshotUrl, VideoUrl, Description])
                print ("    --  Add Camera type Multi_Camera and Main")
            i += 1
        
        TotalCamerasSetting = len(Cameras)
        
        CamerasList = []

        if (TotalCamerasSetting == 8):
            # camera 1
            Cam1 = Cameras[0]
            IdCam1 = Cameras[1]
            HardwareNameCam1 = Cameras[2]
            CameraUseCam1 = Cameras[3]
            IpCameraAddressCam1 = Cameras[4]
            SnapshotUrlCam1 = Cameras[5]
            VideoUrlCam1 = Cameras[6]
            DescriptionCam1 = Cameras[7]
            #
            Camera1 = [Cam1, IdCam1, HardwareNameCam1, CameraUseCam1, IpCameraAddressCam1, SnapshotUrlCam1,VideoUrlCam1, DescriptionCam1]
            CamerasList = [Camera1]
        #    
        if (TotalCamerasSetting == 16):
            # camera 1
            Cam1 = Cameras[0]
            IdCam1 = Cameras[1]
            HardwareNameCam1 = Cameras[2]
            CameraUseCam1 = Cameras[3]
            IpCameraAddressCam1 = Cameras[4]
            SnapshotUrlCam1 = Cameras[5]
            VideoUrlCam1 = Cameras[6]
            DescriptionCam1 = Cameras[7]
            # camera 2
            Cam2 = Cameras[8]
            IdCam2 = Cameras[9]
            HardwareNameCam2 = Cameras[10]
            CameraUseCam2 = Cameras[11]
            IpCameraAddressCam2 = Cameras[12]
            SnapshotUrlCam2 = Cameras[13]
            VideoUrlCam2 = Cameras[14]
            DescriptionCam2 = Cameras[15]
            #
            Camera1 = [Cam1, IdCam1, HardwareNameCam1, CameraUseCam1, IpCameraAddressCam1, SnapshotUrlCam1, VideoUrlCam1, DescriptionCam1]
            Camera2 = [Cam2, IdCam2, HardwareNameCam2, CameraUseCam2, IpCameraAddressCam2, SnapshotUrlCam2, VideoUrlCam2, DescriptionCam2]
            # 
            CamerasList = [Camera1, Camera2]
        #    
        if (TotalCamerasSetting == 24):
            # camera 1
            Cam1 = Cameras[0]
            IdCam1 = Cameras[1]
            HardwareNameCam1 = Cameras[2]
            CameraUseCam1 = Cameras[3]
            IpCameraAddressCam1 = Cameras[4]
            SnapshotUrlCam1 = Cameras[5]
            VideoUrlCam1 = Cameras[6]
            DescriptionCam1 = Cameras[7]
            # camera 2
            Cam2 = Cameras[8]
            IdCam2 = Cameras[9]
            HardwareNameCam2 = Cameras[10]
            CameraUseCam2 = Cameras[11]
            IpCameraAddressCam2 = Cameras[12]
            SnapshotUrlCam2 = Cameras[13]
            VideoUrlCam2 = Cameras[14]
            DescriptionCam2 = Cameras[15]
            # camera 3
            Cam3 = Cameras[16]
            IdCam3 = Cameras[17]
            HardwareNameCam3 = Cameras[18]
            CameraUseCam3 = Cameras[19]
            IpCameraAddressCam3 = Cameras[20]
            SnapshotUrlCam3 = Cameras[21]
            VideoUrlCam3 = Cameras[22]
            DescriptionCam3 = Cameras[23]
            #
            Camera1 = [Cam1, IdCam1, HardwareNameCam1, CameraUseCam1, IpCameraAddressCam1, SnapshotUrlCam1, VideoUrlCam1, DescriptionCam1]
            Camera2 = [Cam2, IdCam2, HardwareNameCam2, CameraUseCam2, IpCameraAddressCam2, SnapshotUrlCam2, VideoUrlCam2, DescriptionCam2]
            Camera3 = [Cam3, IdCam3, HardwareNameCam3, CameraUseCam3, IpCameraAddressCam3, SnapshotUrlCam3, VideoUrlCam3, DescriptionCam3]
            # 
            CamerasList = [Camera1, Camera2, Camera3]    
        if (TotalCamerasSetting > 24):
            # camera 1
            Cam1 = Cameras[0]
            IdCam1 = Cameras[1]
            HardwareNameCam1 = Cameras[2]
            CameraUseCam1 = Cameras[3]
            IpCameraAddressCam1 = Cameras[4]
            SnapshotUrlCam1 = Cameras[5]
            VideoUrlCam1 = Cameras[6]
            DescriptionCam1 = Cameras[7]
            # camera 2
            Cam2 = Cameras[8]
            IdCam2 = Cameras[9]
            HardwareNameCam2 = Cameras[10]
            CameraUseCam2 = Cameras[11]
            IpCameraAddressCam2 = Cameras[12]
            SnapshotUrlCam2 = Cameras[13]
            VideoUrlCam2 = Cameras[14]
            DescriptionCam2 = Cameras[15]
            # camera 3
            Cam3 = Cameras[16]
            IdCam3 = Cameras[17]
            HardwareNameCam3 = Cameras[18]
            CameraUseCam3 = Cameras[19]
            IpCameraAddressCam3 = Cameras[20]
            SnapshotUrlCam3 = Cameras[21]
            VideoUrlCam3 = Cameras[22]
            DescriptionCam3 = Cameras[23]
            # camera 4
            Cam4 = Cameras[24]
            IdCam4 = Cameras[25]
            HardwareNameCam4 = Cameras[26]
            CameraUseCam4 = Cameras[27]
            IpCameraAddressCam4 = Cameras[28]
            SnapshotUrlCam4 = Cameras[29]
            VideoUrlCam4 = Cameras[30]
            DescriptionCam4 = Cameras[31]
            #
            Camera1 = [Cam1, IdCam1, HardwareNameCam1, CameraUseCam1, IpCameraAddressCam1, SnapshotUrlCam1, VideoUrlCam1, DescriptionCam1]
            Camera2 = [Cam2, IdCam2, HardwareNameCam2, CameraUseCam2, IpCameraAddressCam2, SnapshotUrlCam2, VideoUrlCam2, DescriptionCam2]
            Camera3 = [Cam3, IdCam3, HardwareNameCam3, CameraUseCam3, IpCameraAddressCam3, SnapshotUrlCam3, VideoUrlCam3, DescriptionCam3]
            Camera4 = [Cam4, IdCam4, HardwareNameCam4, CameraUseCam4, IpCameraAddressCam4, SnapshotUrlCam4, VideoUrlCam4, DescriptionCam4]
            # 
            CamerasList = [Camera1, Camera2, Camera3, Camera4]  

    return CamerasList


#/////////////////////////////////////////////////////////
#CamerasList = GetCameraList(PollingCamera)
#print (len(CamerasList))
#input ()





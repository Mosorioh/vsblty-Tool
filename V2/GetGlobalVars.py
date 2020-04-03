import json
import os, sys
from io import open

#///////////////////////////////////////////
# GET-Endpoint-Setting
# Funcion para obtener la Configuracion del Endpoint, desde el archivo de Globalvars.json
#//////////////////////////////////////////
def Getvaribles():
    #Iniciamos Lista que contendra toda la configuracion del Endpoint
    EndpointSetting = []
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

        EdgeDetection = str(decoded["List"][92]["Value"])
        FaceAnalysisOptimization = str(decoded["List"][93]["Value"])
        TimeBetweenPictures = str(decoded["List"][108]["Value"])
        ReocurringVisitor = str(decoded["List"][105]["Value"])
        ObjectDetection = str(decoded["List"][82]["Value"])
        NatsServer =  str(decoded["List"][74]["Value"])
        NatsServerUrl =  str(decoded["List"][75]["Value"])
        NatsSubscriber =  str(decoded["List"][73]["Value"])
        NatsSubscriberEndpoint = str(decoded["List"][72]["Value"])
        LiveEndpointData = str(decoded["List"][71]["Value"])
        Identity = str(decoded["List"][69]["Value"])
        EnticeOnly = str(decoded["List"][68]["Value"])
        SAD = str(decoded["List"][66]["Value"])
        BodyDetection = str(decoded["List"][65]["Value"])
        EmailPublisherThreshold = str(decoded["List"][56]["Value"])
        EmailPublisherExpiration = str(decoded["List"][54]["Value"])
        DemograhicDataExpiration = str(decoded["List"][53]["Value"])
        DemographicRulesTimer = str(decoded["List"][52]["Value"])
        PollingCamera = str(decoded["List"][27]["Value"])
        ContentSwappedInterval = str(decoded["List"][10]["Value"])



        #///////////////////////
        # Asignamos configuracion a la Lista
        #///////////////////////
        #EndpointSetting = [ContentSwappedInterval,CameraHardwareName, IPAddress, IsPollingCamera, PollingCameraInterval, CollectAnalytics, DemograhicDataExpirationTime, EmailPublisherBioRecordExpiration, EmailPublisherIdentificationTriggerThreshold, EnableUseVizsafe, IsBodyDetectionTurnedOn, Sad, IsIdentitySearchTurnedOn, LiveEndpointData, NotificationEmailIdentifiacion, ObjectDetection, FaceDetectionAggressiveness, OpenVinoFace, FaceDetectionModel, PersonDetectionType, ReocurringVisitor]
        EndpointSetting = [EdgeDetection, FaceAnalysisOptimization, 
        TimeBetweenPictures, ReocurringVisitor, ObjectDetection,
        NatsServer, NatsServerUrl, NatsSubscriber, NatsSubscriberEndpoint, LiveEndpointData,
        Identity, EnticeOnly, SAD, BodyDetection, EmailPublisherThreshold,
        EmailPublisherExpiration, DemograhicDataExpiration, DemographicRulesTimer, PollingCamera, ContentSwappedInterval]
    return EndpointSetting


#/////////////////////////////////////////////////////////
EndpointSetting = Getvaribles()

EdgeDetection = EndpointSetting[0]
FaceAnalysisOptimization = EndpointSetting[1]
TimeBetweenPictures = EndpointSetting[2]
ReocurringVisitor = EndpointSetting[3]
ObjectDetection =EndpointSetting[4]
NatsServer = EndpointSetting[5]
NatsServerUrl = EndpointSetting[6]
NatsSubscriber = EndpointSetting[7]
NatsSubscriberEndpoint = EndpointSetting[8]
LiveEndpointData = EndpointSetting[9]
Identity = EndpointSetting[10]
EnticeOnly = EndpointSetting[11]
SAD = EndpointSetting[12]
BodyDetection = EndpointSetting[13]
EmailPublisherThreshold = EndpointSetting[14]
EmailPublisherExpiration = EndpointSetting[15]
DemograhicDataExpiration = EndpointSetting[16]
DemographicRulesTimer  = EndpointSetting[17]
PollingCamera  = EndpointSetting[18]
ContentSwappedInterval  = EndpointSetting[19]

"""
print (EdgeDetection)
print (FaceAnalysisOptimization)
print (TimeBetweenPictures)
print (ReocurringVisitor)
print (ObjectDetection)
print (NatsServer)
print (NatsServerUrl)
print (NatsSubscriber)
print (NatsSubscriberEndpoint)
print (LiveEndpointData)
print (Identity)
print (EnticeOnly)
print (SAD)
print (BodyDetection)
print (EmailPublisherThreshold)
print (EmailPublisherExpiration)
print (DemograhicDataExpiration)
print (DemographicRulesTimer)
print (PollingCamera)
print (ContentSwappedInterval)
input()
"""

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


def Busquedacloudiden (GuidTest, parametro, ClientLine, today, TestID, CountTest, item, archivo, Hostname):
    #print ("Parametro Cloud: ", (parametro)) 
    if parametro in ClientLine: 
        print ("Linea: ", ClientLine)
                
        Timeline = ClientLine[0:19]
        PosicionNamePerson = ClientLine.find("Person") + 8
        CorteNamePerso = ClientLine.find("PersonId") 

        PosicionPersonId =ClientLine.find("PersonId") + 10
        CortePersonId = ClientLine.find("DetectedFaceId") 


        


        #CortePersonId = PosicionPersonId + 10
        #CorteGroupId = PosicionGroupId + 9 
        

        #PosicionGroupId  = ClientLine.find("GroupId") 
        #PosicionMatchProbability = ClientLine.find("MatchProbability") 
        #PosicionLocalPersistedFaceId = ClientLine.find("LocalPersistedFaceId")      
        #CorteMatchProbability = PosicionMatchProbability + 18
        #CorteLocalPersistedFaceId = ClientLine.find("LocalPersistedFaceId") + 22
        #Matchsincoma = CorteLocalPersistedFaceId - 25

        # ///////////////////////////////////////////////////////////
        """
        print ("PosicionNamePerson ", PosicionNamePerson)
        print ("PosicionPersonId ", PosicionPersonId)
        print ("PosicionGroupId ", PosicionGroupId)
        print ("PosicionMatchProbability ", PosicionMatchProbability)
        print ("PosicionLocalPersistedFaceId ", PosicionLocalPersistedFaceId)
        """

        NamePerson = ClientLine[PosicionNamePerson:CorteNamePerso]
        PersonId = ClientLine[PosicionPersonId:CortePersonId]

        GroupId = -1
        MatchProbability = -1
        LocalPersistedFaceId = -1

        """
        print (Timeline)
        print (NamePerson)
        print (PersonId)
        input()

        
        GroupId = ClientLine[CorteGroupId:PosicionMatchProbability]
        MatchProbability = ClientLine[CorteMatchProbability:Matchsincoma]
        LocalPersistedFaceId = ClientLine[CorteLocalPersistedFaceId:-39]
        """
        
        item +=1 

        print ("")
        print ("//////////////////////////////////////////////")
        # Datos Test
        print ("Date Test:         ", today)
        print ("Test Numero:       ", TestID)
        print ("Test GUID:         ", GuidTest)
        print ("Ciclo Test:        ", CountTest)
        print ("Item:              ", item)
        print ("Hostname:          ", Hostname)
        print ("File:              ", archivo)
        # Resultados
        print ("Timeline:          ", Timeline)    
        print ("Name person:       ", NamePerson)
        print ("Id person  :       ", PersonId)
        print ("GroupId    :       ", GroupId)
        print ("Match      :       ", MatchProbability)
        print ("LocalPer   :       ", LocalPersistedFaceId)

        from AddLogLine import AddLogLine
        AddLogLine (item, archivo, Timeline, NamePerson, PersonId, MatchProbability, GroupId, LocalPersistedFaceId, TestID, CountTest, Hostname, GuidTest)
        
    return item

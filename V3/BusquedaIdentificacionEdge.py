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

def BusquedaEdgeiden (TestID, GuidTest, CicloActual, parametro, ClientLine, item, file):
    #print ("Parametro Edge: ", (parametro)) 
    if parametro in ClientLine: 
        print ("Linea: ", ClientLine)
                
        Timeline = ClientLine[0:19]
        PosicionNamePerson = ClientLine.find("Name") + 6
        PosicionPersonId = ClientLine.find("PersonId")
        PosicionGroupId  = ClientLine.find("GroupId") 
        PosicionMatchProbability = ClientLine.find("MatchProbability") 
        #PosicionLocalPersistedFaceId = ClientLine.find("LocalPersistedFaceId")

        CortePersonId = PosicionPersonId + 10
        CorteGroupId = PosicionGroupId + 9 
        CorteMatchProbability = PosicionMatchProbability + 18
        CorteLocalPersistedFaceId = ClientLine.find("LocalPersistedFaceId") + 22
        Matchsincoma = CorteLocalPersistedFaceId - 25

        # ///////////////////////////////////////////////////////////
        """
        print ("PosicionNamePerson ", PosicionNamePerson)
        print ("PosicionPersonId ", PosicionPersonId)
        print ("PosicionGroupId ", PosicionGroupId)
        print ("PosicionMatchProbability ", PosicionMatchProbability)
        print ("PosicionLocalPersistedFaceId ", PosicionLocalPersistedFaceId)
        """

        NamePerson = ClientLine[PosicionNamePerson:PosicionPersonId]
        PersonId = ClientLine[CortePersonId:PosicionGroupId]
        GroupId = ClientLine[CorteGroupId:PosicionMatchProbability]
        MatchProbability = ClientLine[CorteMatchProbability:Matchsincoma]
        LocalPersistedFaceId = ClientLine[CorteLocalPersistedFaceId:-39]
        
        item +=1 

        print ("")
        print ("//////////////////////////////////////////////")
        # Datos Test
        
        print ("Test Numero:       ", TestID)
        print ("Test GUID:         ", GuidTest)
        print ("Ciclo Test:        ", CicloActual)
        print ("Item:              ", item)
        print ("File:              ", file)
        # Resultados
        print ("Timeline:          ", Timeline)    
        print ("Name person:       ", NamePerson)
        print ("Id person  :       ", PersonId)
        print ("GroupId    :       ", GroupId)
        print ("Match      :       ", MatchProbability)
        print ("LocalPer   :       ", LocalPersistedFaceId)

        from AddLogLine import AddLogLine
        AddLogLine (item, file, Timeline, NamePerson, PersonId, MatchProbability, GroupId, LocalPersistedFaceId, TestID, CicloActual, GuidTest)

    return item
    


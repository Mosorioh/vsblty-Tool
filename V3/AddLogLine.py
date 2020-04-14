# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddLogLine (item, file, Timeline, NamePerson, PersonId, MatchProbability, GroupId, LocalPersistedFaceId, TestID, CicloActual, GuidTest):
    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Create a new record
                         
            sql = "INSERT INTO `LogIdentification` (`Item`, `File`, `Timeline`, `Name`, `PersonId`, `MatchProbability`, `GroupId`, `LocalPersistedId`, `TestID`, `Ciclo`, `GuidTest`) VALUES (  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (item, file, Timeline, NamePerson, PersonId, MatchProbability, GroupId, LocalPersistedFaceId, TestID, CicloActual, GuidTest))
                        
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro test Insertado corectamente")

    finally:
        connection.close()
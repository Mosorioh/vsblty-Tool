# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddLogEmail (TestID, GuidTest, CountTest, Time, LineLogEmail, PersonName, PersonId):
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
                         
            sql = "INSERT INTO `Emails` (`IdTest`, `Guidtest`, `Ciclo`, `Time`, `LineLogEmail`,  `PersonName`, `PersonId`) VALUES ( %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, Time, LineLogEmail, PersonName, PersonId))
                        
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro del Email Fue Insertado corectamente")

    finally:
        connection.close() 
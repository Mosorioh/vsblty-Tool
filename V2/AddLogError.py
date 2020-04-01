# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddLogError (TestID, GuidTest, CountTest, Hostname, Version, file, Timeline, LineaLog, InfoLogerror):
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
                         
            sql = "INSERT INTO `ErrorSummary` (`IdTest`, `Guid`, `Ciclo`, `Hostname`, `Version`,  `File`, `TimeLine`, `LineLogError`, `InfoLog`) VALUES ( %s, %s,%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, Hostname, Version, file, Timeline, LineaLog, InfoLogerror))
                        
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro del Error Fue Insertado corectamente")

    finally:
        connection.close()
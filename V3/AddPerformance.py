# DB
import pymysql
import datetime 

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddPerformance (TestID, GuidTest, CountTest, PID, Cpu, Ram):
    if (Cpu > 100):
        Cpu = 100
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
                         
            sql = "INSERT INTO `Performance` (`TestId`, `GuidTest`, `Ciclo`, `PID`, `Cpu`, `Ram`) VALUES ( %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, PID, Cpu, Ram))
                        
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            print ("Performance Data Taken in: ", datetime.datetime.now(), " - Ram: ",Ram, "MB")


    finally:
        connection.close()


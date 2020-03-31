# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddFrameSummary (TestID, GuidTest, CountTest, Folder, Cam1, Cam2, Cam3, Cam4, CountFrame ):
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
                         
            sql = "INSERT INTO `FrameSummary` (`Idtest`, `GuidTest`, `Ciclo`, `Folder`, `Cam1`, `Cam2`, `Cam3`, `Cam4`,`CountFrame`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, Folder, Cam1, Cam2, Cam3, Cam4, CountFrame))
                        
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro test Insertado corectamente")

    finally:
        connection.close()
# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddLogFuntionTook (TestID, GuidTest, CicloActual, Timeline, InfoLog, TookTime):
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
                         
            sql = "INSERT INTO `FaceAnalysisTook` (`TestId`, `GuidTest`, `Ciclo`, `Timeline`, `InfoLog`,  `TookTime`) VALUES ( %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CicloActual, Timeline, InfoLog, TookTime))
                        
            connection.commit()
            
            print ("Registro de Face Analysis Function Took Fue Insertado corectamente")

    finally:
        connection.close()
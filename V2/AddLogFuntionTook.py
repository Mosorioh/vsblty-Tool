# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddLogFuntionTook (TestID, GuidTest, CountTest, Timeline, InfoLog, TookTime):
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
                         
            sql = "INSERT INTO `FaceAnalysisTook` (`IdTest`, `Guid`, `Ciclo`, `Timeline`, `InfoLog`,  `TookTime`) VALUES ( %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, Timeline, InfoLog, TookTime))
                        
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro de Face Analysis Function Tokk Fue Insertado corectamente")

    finally:
        connection.close()
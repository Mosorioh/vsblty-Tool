# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion

TestId = 126

def AveragePerformance (TestID):

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
                         
            sql = "SELECT AVG(Cpu) AS Cpu FROM `Performance` WHERE `Idtest` = %s"
            cursor.execute(sql, (TestID))
            CpuResultAve = cursor.fetchone()
            CpuAve = int(CpuResultAve.get('Cpu'))
            #print (CpuAve)

            sql2 = "SELECT AVG(Ram) AS Ram FROM `Performance` WHERE `Idtest` = %s"
            cursor.execute(sql2, (TestID))
            RamResultAve = cursor.fetchone()
            RamAve = int(RamResultAve.get('Ram'))
            #print (RamAve)
            

            AvePerformance = [CpuAve, RamAve]
                        
    finally:
            connection.close()

    return AvePerformance

AveragePerformance (TestId)
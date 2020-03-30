# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def GetTestId (GuidTest):
    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `Id` FROM `Test` WHERE `GUID` = %s"
                cursor.execute(sql, (GuidTest)) 
                result = cursor.fetchone()
                print ("Resultado:", result)
                TestID = int(result.get('Id'))
                print ("Id", TestID)
                #input ()
                
    finally:
        connection.close()

    return TestID
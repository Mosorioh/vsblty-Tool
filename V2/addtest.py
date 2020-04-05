# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def addtest (today, GuidTest, Hostname, NumerodeCiclos, DuracionTest, Descripcion, Version, IdentificationService, BetweenPictures, CameraMode, TotalCameraSetting, VersionService, FaceAnalysisOptimization):
    if (IdentificationService == 1):
        iServices = "Edge"
    if (IdentificationService == 0):
        iServices = "Cloud"
    
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
                         
            sql = "INSERT INTO `Test` ( `GUID`, `Hostname`, `TotalCiclos`, `Duracion`, `Descripcion`,  `VersionClient`,  `IdentificationService`,  `BetweenPictures`,  `CameraMode`, `TotalCamera`, `VersionServices`, `FaceAnalysisOptimization`, `iServices`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, ( GuidTest, Hostname, NumerodeCiclos, DuracionTest, Descripcion, Version, IdentificationService, BetweenPictures, CameraMode, TotalCameraSetting, VersionService, FaceAnalysisOptimization, iServices))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro test Insertado corectamente")

    finally:
        connection.close()
# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def addtest (GuidTest, Hostname, VersionClient, VersionService, CameraMode, TotalCameraSetting, IdentificationService, Optimized, ServicesType, BetweenPictures, Ciclos, DuracionCiclo, Descripcion):
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
                         
            sql = "INSERT INTO `Test` ( `GuidTest`, `Hostname`, `VersionClient`, `VersionService`, `CameraMode`,  `TotalCameras`,  `IdentificationService`,  `FaceAnalysisOptimization`,  `ServicesType`, `BetweenPictures`, `Ciclos`, `DuracionCiclos`, `DescriptionTest`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (GuidTest, Hostname, VersionClient, VersionService, CameraMode, TotalCameraSetting, iServices, Optimized, ServicesType, BetweenPictures, Ciclos, DuracionCiclo, Descripcion))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("")
            print ("*******************************************************************")
            print ("///////////////////////////////////////////////////////////////////")
            print ("   --  Registro del Nuevo Test se ha Insertado corectamente")
            print ("*******************************************************************")
            print ("///////////////////////////////////////////////////////////////////")
            

    finally:
        connection.close()
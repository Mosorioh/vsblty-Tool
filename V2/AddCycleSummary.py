# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def addCycleSummary (TestID, GuidTest, CountTest, TotalFaceIdentificacion, TotalFrameReceived, TotalBeforeProcessing, TotalError, TotalFrameLocalPhotos, TotalFrameAfterIdentification, CpuAve, RamAve, TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements):
    faceapi = -1
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
                         
            sql = "INSERT INTO `CycleSummary` (`IdTest`, `GuidTest`, `Ciclo`, `TotalIdentificacion`, `TotalFrameReceived`, `TotalBeforeProcessing`,  `TotalFaceAPIResults`, `TotalError`, `LocalPhotos`, `AfterIdentification`, `CpuAve`, `RamAve`, `TotalFileMetrics`, `TotalFileMetricsIdentification`, `TotalFIleSinPersonEngagements` ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, TotalFaceIdentificacion, TotalFrameReceived, TotalBeforeProcessing, faceapi, TotalError, TotalFrameLocalPhotos, TotalFrameAfterIdentification, CpuAve, RamAve, TotalFilesGenerados, TotalFileMetricsIdentification, TotalFIleSinPersonEngagements))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro test Insertado corectamente")

    finally:
        connection.close()


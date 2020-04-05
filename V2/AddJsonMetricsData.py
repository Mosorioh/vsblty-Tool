# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def addJsonMetricsData (TestID, GuidTest, CountTest, machine, file, GuidFile, timestamp, assetName, engagementType, contentType, Face, localPersistedFaceId, age, Genero, name, bioRecordId, identificationConfidence, camera, cameraDescription):

    if (engagementType == 1):
        engagementType = "Entice"
    if (engagementType == 2):
        engagementType = "Engage"
    if (engagementType == 3):
        engagementType = "Interactive"

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
                         
            sql = "INSERT INTO `JsonMetrics` (`IdTest`, `GuidTest`, `Ciclo`, `machine`, `File`, `GuidFile`,  `timestamp`, `assetName`, `engagementType`, `contentType`, `faceId`, `localPersistedFaceId`, `age`, `Genero`,  `IdentityName`, `bioRecordId`, `identificationConfidence`, `camera`, `cameraDescription` ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, machine, file, GuidFile, timestamp, assetName, engagementType, contentType, Face, localPersistedFaceId, age, Genero, name, bioRecordId, identificationConfidence, camera, cameraDescription))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro Json- Metrics- Data Insertado corectamente")

    finally:
        connection.close()


# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddJsonSummary (JsonSummary): 

    TestId = JsonSummary[0]
    GuidTest = JsonSummary[1]
    CountTest = JsonSummary[2]
    GuidFile = JsonSummary[3]
    file = JsonSummary[4]
    Time = JsonSummary[5]
    DetectedFaces = JsonSummary[6]
    identifications = JsonSummary[7]
    Bodycount = JsonSummary[8]
    BodyTracking = JsonSummary[9]
    CameraId = JsonSummary[10]
    CameraDescrption = JsonSummary[11]

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
                         
            sql = "INSERT INTO `JsonSummary` (`TestId`, `GuidTest`, `Ciclo`, `GuidFile`, `File`,  `Time`, `DetectedFaces`, `identifications`, `Bodycount`, `BodyTracking`, `CameraId`, `CameraDescrption`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestId, GuidTest, CountTest, GuidFile, file,  Time, DetectedFaces, identifications, Bodycount, BodyTracking, CameraId, CameraDescrption))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro Json- Metrics- Data Insertado corectamente")

    finally:
        connection.close()


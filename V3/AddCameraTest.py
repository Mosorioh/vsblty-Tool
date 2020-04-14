# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


# def AddCameraTest (TestID, GuidTest, Cam, IdCam, HardwareName, IpCameraAddress, SnapshotUrl, VideoUrl, Description):
def AddCameraTest (TestID, GuidTest, Camera1):
    OrderCamera = Camera1[0]
    IdCamera = Camera1[1]
    HardwareName = Camera1[2]
    CameraUse = Camera1[3]
    IpCameraAddress = Camera1[4]
    SnapshotUrl = Camera1[5]
    VideoUrl = Camera1[6]
    Description = Camera1[7]

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
                         
            sql = "INSERT INTO `CameraTest` (`TestId`, `GuidTest`, `OrderCamera`, `IdCamera`, `HardwareName`, `CameraUse`, `IpCameraAddress`,  `SnapshotUrl`,  `VideoUrl`,  `Description`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, OrderCamera, IdCamera, HardwareName, CameraUse, IpCameraAddress, SnapshotUrl, VideoUrl, Description))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("       -- Registro de la Camara: ", CameraUse, "-",  IdCamera, " Insertado corectamente")

    finally:
        connection.close()
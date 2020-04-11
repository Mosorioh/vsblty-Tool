# DB
import pymysql

# //////////////////////////////////////
# Conexion
# //////////////////////////////////////
from Conexion import Conexion


def AddJsonTest (TestID, GuidTest, CountTest, JsonGenerados, FileMainR, FileMultiple, FaceIdDetectados, FaceConDemographics,FileSindemographics, TotalIdentificaciones, PersonasNoIdentificadas, FacesEstimadas, IdentificacionEstimada, EfectividadFacesdetected, Efectividadidentidicaciones, OVServicesType, FaceAnalysisOptimization):
    EfectividadFacesdetected = float(EfectividadFacesdetected)
    print (EfectividadFacesdetected)
    if ( EfectividadFacesdetected > 100):
        EfectividadFacesdetected = 100
    
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
                         
            sql = "INSERT INTO `JsonTest` (`TestId`, `GuidTest`, `Ciclo`, `ArchivosGenerados`, `ArchivosMain`,  `ArchivosMultiple`, `FacesDetectadas`, `FacesConDemografica`, `FacesSinDemografica`, `personasIdentificadas`, `PersonasNoIdentificadas`, `DeteccionesEstimadas`,`IdentificacionesEstimadas`,`EraDeteccion`,`EraIdentificacion`, `OpenVinoServicesType`, `Faceanalysisoptmization`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (TestID, GuidTest, CountTest, JsonGenerados, FileMainR, FileMultiple, FaceIdDetectados, FaceConDemographics,FileSindemographics, TotalIdentificaciones, PersonasNoIdentificadas, FacesEstimadas, IdentificacionEstimada, EfectividadFacesdetected, Efectividadidentidicaciones, OVServicesType, FaceAnalysisOptimization))
                        
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("Registro del Error Fue Insertado corectamente")

    finally:
        connection.close()
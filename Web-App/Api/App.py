from flask import Flask, request
from flask import render_template
from flask import jsonify
import uuid 
# BD
import time
import datetime 
from datetime import date
from datetime import datetime
import pymysql
# Cors
from flask_cors import CORS

app=Flask(__name__,template_folder='templates')
cors = CORS(app)

@app.route('/')
def home():
    return 'Api rest '


#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/Test')
def select():
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `Id`, `GUID`, `VersionClient`, `CameraMode`, `iServices`, `BetweenPictures`, `Descripcion` FROM `Test` ORDER BY `Id` DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/ciclo/<idtest>')
def ciclo(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `CicloTest` FROM `Identificacion` WHERE `TestID` =%s GROUP BY `CicloTest`"
            cursor.execute(sql, idtest)
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()



#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/Resultado/<idtest>/<idCiclo>')
def Resultado(idtest, idCiclo):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `PersonId`, `Name`, COUNT(*) AS Total, MIN(`MatchProbability`) AS Minimo, MAX(`MatchProbability`) AS Maximo, AVG(`MatchProbability`) AS Average  FROM `Identificacion` WHERE `TestID` =%s AND `CicloTest` =%s GROUP BY `PersonId`,`Name`"

            cursor.execute(sql, (idtest, idCiclo))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/Testnumero/<idtest>/<idCiclo>')
def Testnumero(idtest, idCiclo):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `PersonId`, `Name`, COUNT(*) AS Total, MIN(`MatchProbability`) AS Minimo, MAX(`MatchProbability`) AS Maximo, AVG(`MatchProbability`) AS Average  FROM `Identificacion` WHERE `TestID` =%s AND `CicloTest` =%s GROUP BY `PersonId`,`Name`"
            cursor.execute(sql, (idtest, idCiclo))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/DetailTest/<idtest>')
def DetailTest(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Test` WHERE `Id` =%s "
            cursor.execute(sql, idtest)
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()


#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/ResumenCiclo/<idtest>')
def ResumenCiclo(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `CycleSummary` WHERE `IdTest` =%s "
            cursor.execute(sql, idtest)
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()



#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/ResumenCiclo/<idtest>/1')
def ResumenCiclo1(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `CycleSummary` WHERE `IdTest` =%s AND `Ciclo` =%s "
            cursor.execute(sql, (idtest, 1))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/FrameSummary/<idtest>/<idciclo>')
def FrameSummary(idtest, idciclo):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `FrameSummary` WHERE `IdTest` =%s AND `Ciclo` =%s "
            cursor.execute(sql, (idtest, idciclo))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()


#//////////////////////////////////////////
# Api Pais
#//////////////////////////////////////////
@app.route('/selectcomparation/<Idmode>')
def selectcomparation(Idmode):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `Id`, `GUID`, `Version`, `CameraMode`, `IdentificationService`, `BetweenPictures`, `Hostname`, `Descripcion` FROM `Test` WHERE `CameraMode` =%s "
            cursor.execute(sql, Idmode)
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()


#//////////////////////////////////////////
# Api CAmera
#//////////////////////////////////////////
@app.route('/CameraSummary/<idtest>')
def CameraSummary(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `CameraSummary` WHERE `TestID` =%s"
            cursor.execute(sql, (idtest))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api CAmera
#//////////////////////////////////////////
@app.route('/Emails/<idtest>')
def Emails(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Emails` WHERE `IdTest` =%s ORDER BY `Time`"
            cursor.execute(sql, (idtest))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()


#//////////////////////////////////////////
# Api Error
#//////////////////////////////////////////
@app.route('/Error/<idtest>')
def Error(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `ErrorSummary` WHERE `IdTest` =%s"
            cursor.execute(sql, (idtest))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api Error
#//////////////////////////////////////////
@app.route('/JsonMetrics/<idtest>')
def JsonMetrics(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `JsonMetrics` WHERE `IdTest` =%s"
            cursor.execute(sql, (idtest))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()


#//////////////////////////////////////////
# Api Error
#//////////////////////////////////////////
@app.route('/JsonSummary/<idtest>')
def JsonSummary(idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `JsonSummary` WHERE `TestId` =%s ORDER BY `Time`"
            cursor.execute(sql, (idtest))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()



#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#
# GRAFICO MAIN Index
# Chart - Grafico Main Pais 
#
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////

@app.route('/Indice/<Idtest>')
def MainpaisIndice(Idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #///////////////////////////////
            
            sql2 = "SELECT `PID` AS PID, `DateMuestra` AS Time, `Ram` As Ram, `Cpu` AS Cpu FROM `Performance` WHERE `Idtest`=%s "
            cursor.execute(sql2, (Idtest))
            resultMensajes_Actual = cursor.fetchall()
            Mensajes_Actual = resultMensajes_Actual
            print("Mensaje: ", Mensajes_Actual)
            #print(resultMale)
            
            #///////////////////////////////
         

        return jsonify(Mensajes_Actual)

    finally:
        connection.close()


#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#
# GRAFICO MAIN Index
# Chart - Grafico Main Pais 
#
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////

@app.route('/FaceAnalysisTook/<Idtest>')
def FaceAnalysisTookTable(Idtest):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #///////////////////////////////
            
            sql2 = "SELECT `Ciclo`, `InfoLog` FROM `FaceAnalysisTook` WHERE `IdTest`=%s ORDER BY `Timeline`"
            cursor.execute(sql2, (Idtest))
            resultMensajes_Actual = cursor.fetchall()
            Mensajes_Actual = resultMensajes_Actual
            print("Mensaje: ", Mensajes_Actual)
            #print(resultMale)
            
            #///////////////////////////////
         

        return jsonify(Mensajes_Actual)

    finally:
        connection.close()

#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#
# Face analysis took
#
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////

@app.route('/FaceAnalysisTook/<idtest>/<idciclo>')
def FaceAnalysisTook(idtest, idciclo):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='Log-identificacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #///////////////////////////////
            
            sql = "SELECT AVG(TookTime) as Average from  `FaceAnalysisTook`  WHERE `IdTest` =%s AND `Ciclo` =%s  ORDER BY `Id`"
            cursor.execute(sql, (idtest, idciclo))
            Average = cursor.fetchone()
            print(Average)
            #AVG = str(Average)
            Avg = str(Average.get('Average'))

            """
            # Minimo
            sql2 = "SELECT MIN(TookTime) as Minimo from  `FaceAnalysisTook`  WHERE `IdTest` =%s AND `Ciclo` =%s  ORDER BY `Id`"
            cursor.execute(sql2, (idtest, idciclo))
            Minimo = cursor.fetchall()
            print(Minimo)

            """
            # Maximo
            sql3 = "SELECT  MAX(TookTime) as Maximo from  `FaceAnalysisTook`  WHERE `IdTest` =%s AND `Ciclo` =%s  ORDER BY `Id`"
            cursor.execute(sql3, (idtest, idciclo))
            Maximo = cursor.fetchone()
            print(Maximo)
            Max = str(Maximo.get('Maximo'))
            
            # Count
            sql4 = "SELECT  COUNT(ID) as Count from  `FaceAnalysisTook`  WHERE `IdTest` =%s AND `Ciclo` =%s  ORDER BY `Id`"
            cursor.execute(sql4, (idtest, idciclo))
            Count = cursor.fetchone()
            print(Count)
            CountR = str(Count.get('Count'))
            #Count
            
            # Suma
            sql5 = "SELECT  SUM(TookTime) as Suma from  `FaceAnalysisTook`  WHERE `IdTest` =%s AND `Ciclo` =%s  ORDER BY `Id`"
            cursor.execute(sql5, (idtest, idciclo))
            Suma = cursor.fetchone()
            print(Suma)
            SumaR = str(Suma.get('Suma'))
            #Count
            #///////////////////////////
         

        return jsonify({"Average": Avg, "Maximo": Max, "Count": CountR, "Sum": SumaR})



    finally:
        connection.close()


if __name__ == '__main__':
    #app.run(host='192.168.100.233', port=5080, debug=True)
    app.run(host='192.168.100.51', port=5080, debug=True)
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



if __name__ == '__main__':
    #app.run(host='192.168.100.233', port=5080, debug=True)
    app.run(host='192.168.100.51', port=5080, debug=True)
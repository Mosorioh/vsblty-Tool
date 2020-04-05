from flask import Flask, request
from flask import render_template
from flask import jsonify
import uuid 
# BD
import time
import datetime 
from datetime import date
from datetime import datetime, timedelta
import pymysql
from flask_cors import CORS

app=Flask(__name__,template_folder='templates')
cors = CORS(app)

@app.route('/')
def home():
    return 'Api rest Graficos'


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
# GRAFICO MAIN
# Chart - Grafico Main Pais 
#
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////

@app.route('/Grafico/<idpais>')
def Mainpais(idpais):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='COVID19',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #///////////////////////////////
            
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data` WHERE `Id_Pais`=%s ORDER BY `Id` DESC LIMIT 100 "
            cursor.execute(sql2, (idpais))
            resultMensajes_Actual = cursor.fetchall()
            Mensajes_Actual = resultMensajes_Actual
            print("Mensaje: ", Mensajes_Actual)
            #print(resultMale)
            
            #///////////////////////////////
         

        return jsonify(Mensajes_Actual)

    finally:
        connection.close()

if __name__ == '__main__':
    #app.run( )
    app.run(host='192.168.100.233', port=5070, debug=True)

'''Crear base de datos local con sqlite
info en: https://likegeeks.com/es/tutorial-de-python-sqlite3/'''

#importar el módulo sqlite3
import sqlite3
from sqlite3 import Error
#crear un objeto de conexión (con) para conectarse con la db
def sql_connection():
    try:
        con = sqlite3.connect('dbtemp.db')
        return con
    except Error:
        print(Error)

#para ejecutar sentencias de sqlite en python se necesita de un cursor
#se crea un cursor utilizando el objeto de conexión
cursor_obj = con.cursor()

#ahora es posible usar el objeto cursor para llamar al método execute() para ejecutar cualquier consulta SQL.


'''#####CREAR BASE DE DATOS########
#Cuando se crea una conexión con SQLite, se crea a la vez un archivo base de datos, si es que no existe
#tambien es posible crear una base de datos en la RAM usando :memory: con la función de conexión ("base de datos en memoria"):
#con = sqlite3.connect(':memory:')

###CREAR TABLA###
#Se utiliza el método execute() con los siguientes pasos:
#1. se crea el objeto de conexión
#2. se crea el objeto cursor con el objeto de conexión
#3. se ejecuta el método execute con el cursor, bajo la consulta CREATE TABLE como parámetro'''


#define función que crea el objeto cursor y crea tabla
def sql_table(con):
    #se establece conexión con el cursor
    cursor_obj = con.cursor()
    #el cursor ejecuta crear la tabla
    cursor_obj.execute("CREATE TABLE grants(id integer PRIMARY KEY, StartYear integer, identif integer, Title text, Leader text, Grantee text, GrantAmount real, FundingArea text, Region text, Featured text)")
#se guardan los resultados con el commit
    con.commit()

#ejecuto la funcion sql_connection que crea el objeto de conexión, luego ejecuto la función sql_table que utiliza el objeto de conexión para crear la tabla y el objeto cursor
con = sql_connection()
sql_table(con)




'''ejemplo para subir csv'''
import csv

campanas_verdes = open("campanas-verdes.csv", "r", encoding="utf-8")
campanas_verdes_r = csv.reader(campanas_verdes, delimiter= ",")

#conecto con base de datos con objeto de conexión
con = sqlite3.connect('campanas_verdes.db')
#creo un cursor 
cursor_obj = con.cursor()
#creo la tabla
cursor_obj.execute(CREATE TABLE campanas_verdes (id integer PRIMARY KEY, longitud integer, latitud integer, calle text, altura integer, modelo text, barrio text, comuna integer, cp integer, cparg integer)

next(campanas_verdes_r)
for line in campanas_verdes_r:
    longitud = line[0]
    latitud = line[1]
    calle = line[2]
    altura = line[3]
    modelo = line[4]
    barrio = line[5]
    comuna = line[6]
    cp = line[7]
    cparg = line[8]

    sql = "INSERT INTO campanas_verdes (longitud, latitud, calle, altura, modelo, barrio, comuna, cp, cparg) VALUES ('"+longitud+"', '"+latitud+"', '"+calle+"', '"+altura+"', '"+modelo+"', '"+barrio+"', '"+comuna+"', '"+cp+"', '"+cparg+"')"

#ejecuto el query con el cursor
cursor_obj.execute(sql)
con.commit()
cursor_obj.close()
con.close()


'''ejemplo para subir json'''

import json

with open("grants.json", "r", encoding="utf8") as f:
    grants_dict = json.load(f)

i = 0
for grant in grants_dict:
    cursor_obj.execute("INSERT INTO grants (id, StartYear, identif, Title, Leader, Grantee, GrantAmount, FundingArea, Region, Featured) VALUES(?,?,?,?,?,?,?,?,?,?)", (i,grant['Start Year'],grant['ID'],grant['Title'],grant['Project Leader(s)'],grant['Grantee(s)'],grant['Grant Amount'],grant['Funding Area'],grant['Region'],grant['Featured']))
    i= i+1

con.commit()
cursor_obj.close()
con.close()
'''método nativo para abrir archivos en python:
open() carga archivos en un buffer de datos. Sintaxis: "archivo = open("nombre_archivo.extension")"
archivo.write() permite modificar el archivo
archivo.close() cierra el archivo
info útil sobre esto en https://overiq.com/python-101/file-handling-in-python/'''

#abrir archivo existente
mi_archivo = open("nombre.csv", mode= "r", encoding="")

#abrir archivo nuevo
mi_archivo_2 = open("nombre.csv", mode="w", encoding="")

'''manipular strings de mi_archivo.csv:
con un for puedo recorrer las líneas y aplicar cualquiera de los métodos para strings.

metodos para los strings:
    #capitalize()
    #count() --> busca cantidad de apariciones de la palabra
    #find() --> te dice si está o no está (true/false)
    #rfind()
    #replace() --> reemplaza caracteres por otros
    #split()
    #index()
    #startwith()
    #encode()
    #low()
    #zfill()
    #partition()'''

#ejemplo: manipulación de columnas del csv
for linea in mi_archivo:
    #reemplazar saltos de línea por nada
    linea = linea.replace("\n", "")
    #generar lista al dividir por ',' 
    lista = linea.split(",")
    #crear variables para cada columna del csv
    variable = lista[index]
    otra_variable = lista[index_2]
    #crear lineas que combinan elementos
    nueva_linea = variable + "," + otra_variable + "\n"
    #escribo todo en un nuevo archivo
    mi_archivo_2.write(nueva_linea)

#cerrar archivos
mi_archivo.close()
mi_archivo2.close()


#libreria csv: tiene varias funciones para trabajar con csvs.
import csv
mi_archivo = open("nombre.csv", encoding="")

#reader transforma un csv en otro que reconoce las comas como separadores de columnas.
mi_archivo2 = csv.reader(mi_archivo, delimiter=",")

#el método strip elimina directamente un caracter
for line in mi_archivo2:
    line = line.strip("\n")
#split lo divide con el separador deseado y lo transforma en una lista
    lista = line.split(",")







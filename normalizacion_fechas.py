''''normalizar datos = todos los datos son transformados para estar en el mismo formato
involucra individualización (donde empieza y donde termina cada elemento) y clasificación (qué tipo de dato es)
1. requiero estrategia de ajuste: llevar datos a un modelo normal y extraerlos en un mismo formato. hay objetos de python específicos

NORMALIZACIÓN DE FECHAS
#objeto datetime tiene dos métodos importantes:
#strptime (fecha_input, patron) --> indica el modelo que sigue la fecha input
#strftime (objeto_date, patron) --> transforma el input en un nuevo modelo de fecha
#POSIX = parametros que permiten identificar tipos de datos esperados.'''

#importar la libreria datetime del modulo datetime
from datetime import datetime

#EJ: Quiero transformar 13/12/2019 en 13-12-2019
# el input es fecha
fecha = "13/12/2019"

#obj_date es el objeto fecha input formateado en un modelo de fecha 
obj_date = datetime.strptime(fecha, '%d/%m/%Y')

#fecha_output es la transformación de la fecha input obj_date en un modelo de fecha indicado
fecha_output = datetime.strftime(obj_date, '%d-%m-%Y')
#print(fecha, "--->", obj_date, "--->", fecha_output)


#funcion normalizador permite ingresar fechas en un formato y las arroja en otro formato fijo
#ej: normalizador("2019-13-02 14:23:33", "%Y-%d-%m %H:%M:%S"), normalizador("13 days after February 2019", "%d days after %B %Y")
def normalizador(fc_input, formato):
    obj_date = datetime.strptime(fc_input, formato)
    fecha_output = datetime.strftime(obj_date, '%d-%m-%Y')
    print(fc_input, "--->", obj_date, "--->", fecha_output)

#funcion normalizadorUniversal permite ingresar fechas en un formato y arroja fechas en otro formato
#ej: normalizador(02/2019, %m/%y, %M-%Y)
def normalizadorUniversal(fc_input, formato_in, formato_out):
    obj_date = datetime.strptime(fc_input, formato_in)
    fecha_output = datetime.strftime(obj_date, formato_out)
    print(fc_input, "--->", obj_date, "--->", fecha_output)

#manejo con meses escritos con letras
#Ej.
fecha = "13/Febrero/2019"
#Crea lista de los elementos de la fecha
lista = fecha.split("/")
#toma el mes y lo pone en mayusculas
mes_normalizado =lista[1].upper()
#crea lista con todos los meses
meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
#busca el indice del mes de la fecha ingresada y le suma 1 para tener el número del mes
nro_mes = meses.index(mes_normalizado)+1
#usa normalizador 
normalizador(lista[0] + str(nro_mes) + lista[2], '%d%m%Y')

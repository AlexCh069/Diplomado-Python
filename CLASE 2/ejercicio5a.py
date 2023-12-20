#   Ejemplo con lectura de for
archivo = open('diavelitas.txt','r')
for linea in archivo:
 print (linea)
archivo.close()
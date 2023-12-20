#  LECTURA DE ARCHIVOS DE TEXTO 
archivo = open('diavelitas.txt','r')
contenido=archivo.read()
print(contenido)
archivo.close()
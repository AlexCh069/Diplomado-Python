#Caracteres para definir expresiones regulares
"""
Inicio y fin de línea: ^, $
Los símbolos de acento circunflejo (^) y dólar ($) 
indican que nuestro patrón de búsqueda debe contener 
respectivamente el inicio o fin de una línea en una 
cadena de texto. 
"""
import re
frase = "Python no sólo es un lenguaje de programación, Python es mi lenguaje de programacón favorito."
patron = '^Python'
#print(re.findall(patron, frase))
frase = "Me gusta aprender Python y programar en Python"
patron = 'Python$'
print(re.findall(patron, frase))
"""
 Coincidencia de caracteres: ., \s, \S
 Los símbolos ., \s y \S indican respectivamente cualquier carácter, 
 espacio en blanco y cualquier carácter a excepción del espacio en blanco.
"""
import re
frase = "Cython no es ningún lenguaje de programación y Nython tampoco pero Python sí"
patron = '^.ython'
palabras = re.findall(patron, frase)
print(palabras)
patron = '\\s.ython'
palabras = re.findall(patron, frase)
print(palabras)
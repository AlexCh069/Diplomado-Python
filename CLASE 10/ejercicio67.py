"""
Rangos de caracteres: [a-z]
Dentro de los conjuntos de caracteres también podemos especificar 
rangos añadiendo un guión a la secuencia. Algunos ejemplos de uso son los siguientes:

[a-z]+ : indica una secuencia de letras minúsculas.
[A-Z]+ : se usa para encontrar secuencias de letras mayúsculas.
[a-zA-Z]+ : es para secuencias de letras mayúsculas o minúsculas.
[A-Z][a-z]+ : secuencias de una letra mayúscula seguida de una o más letras mayúsculas.
[0-9]+ : para secuencias de números de uno o más dígitos.   
"""
import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[a-z]+'
print(re.findall(patron, frase))
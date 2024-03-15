""" 
El acento circunflejo (^) al principio de la secuencia entre corchetes se utiliza 
para indicar negación. Es decir la no coincidencia con los caracteres especificados. 
Un ejemplo de uso puede ser la separación de las palabras de una frase
 excluyendo sus signos de puntuación. 
"""
import re
frase = "¡Esto es una frase! Además contiene signos de puntuación. ¿Los eliminamos?"
patron = '[^¡!.¿? ]+'
print(re.findall(patron, frase))
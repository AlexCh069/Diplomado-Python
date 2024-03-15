"""
 Caracteres de repetición: *, +, ?
 Estos tres caracteres tienen el siguiente significado:

* : indica la repetición de un carácter cero o más veces.
+ : indica la repetición de un carácter una o más veces.
? : Es el carácter reluctant o cuantificador reacio. Añadido a cualquiera 
    de los anteriores se contará con la ocurrencia más corta posible.
"""
import re
frase = "Ramon y Roman programan en Pymhon"
patron = '.+R'
#print(re.findall(patron, frase))
patron = '.+?a'
print(re.findall(patron, frase))
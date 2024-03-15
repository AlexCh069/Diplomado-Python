"""Conjunto de caracteres: [], [^]
Encerrando un conjunto de caracteres entre corchetes ([]) indica cualquiera de 
los caracteres especificados. Así, el patrón [abc] coincidiría con las secuencias ‘a’, ‘b’ o ‘c’. 
El siguiente ejemplo ilustra el uso de los corchetes. En él podemos ver 
que patrón ‘[CN]ython’ no encuentra coincidencia con la secuencia ‘Python’ 
de la frase, ya que ‘P’ no está dentro de los corchetes.
"""
import re
frase = "Cython no es ningún lenguaje de programación y Nython tampoco pero Python sí"
patron = '[CN]ython'
print(re.findall(patron, frase))
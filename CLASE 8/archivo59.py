#EXPRESIONES REGULARES
import re
#re.search(patrón, cadena) es la sintaxis del search
print(re.search("Python", "Programa en Python"))
#re.findall(patrón, cadena) es la sintaxis
print(re.findall("Python", "Programa en Python es mi blog favorito de Python, y gracias a él me estoy convirtiendo en todo un Pythonista."))
#re.split(separador, cadena) #sintaxis
print(re.split("@","nombre.apellido@ejemplo.tld"))

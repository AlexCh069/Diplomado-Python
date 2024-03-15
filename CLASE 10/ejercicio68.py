""" 
Inicio y fin de la extracción: ()
Los paréntesis ( ) no forman parte del patrón a comprobar, pero indican respectivamente 
dónde empieza y termina la extracción del texto. Un caso de uso es la extracción de dominios 
en direcciones de correo electrónico. Esta operación la podemos realizar 
mediante el patrón: ‘@([^ ]*)’ En este caso sabemos que el dominio viene 
después de un símbolo de arroba (@) que indicamos en nuestra expresión regular, 
seguido de una condición cerrada entre paréntesis ya que no queremos que el resultado contenga arrobas. 
"""
import re
frase = "Tengo dos correos electrónicos que son nombre.apellido@dominio.tld y nombre@dominio.com"
patron = '@([^ ]*)'
print(re.findall(patron, frase))
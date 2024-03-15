#Estructura de un decorador
""" 
  Un decorador se compone de las tres ideas que acabamos de ver. 
  Es decir, acepta una función como argumento y define una función interior
  la cual retorna. Además, dentro de la función interior ejecuta la 
  función que se le ha pasado como argumento. 
"""

def mi_decorador(funcion_original):#def mi_decorador(funcion_necesita_decorador())
    def funcion_envolvente():
        print("Código antes de la funcion_original()")
        funcion_original()# funcion_necesita_decorador()
        print("Código después de la funcion_original()")
    return funcion_envolvente
@mi_decorador
def funcion_necesita_decorador():
    print("¡Quiero que me decoren!")
#programa principal
#funcion_decorada = mi_decorador(funcion_necesita_decorador) #funcion_decorada=funcion_envolvente()
#funcion_decorada()  # EJECUTA funcion_envolvente()
funcion_necesita_decorador()  
print("fin de programa")        
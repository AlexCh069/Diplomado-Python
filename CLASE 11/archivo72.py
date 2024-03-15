#Funciones como argumentos
def una_funcion():
    return "Código de una_funcion()"
def otra_funcion(alguna_funcion): #def otra_funcion(una_funcion)
    print("Código de otra_funcion()")
    print(alguna_funcion())# print(una_funcion())
#programa principal
otra_funcion(una_funcion) 
print("FIN DEL PROGRAMA")   
#Retornando funciones
def funcion_externa():
    print("Código de la funcion_externa()")
    def funcion_interna():
        print("Código de la funcion_interna()")
    return funcion_interna
#programa principal
mi_funcion = funcion_externa() # mi_funcion=funcion_interna() asi queda despues del llamado de la funcion_externa()
mi_funcion()# funcion_interna()
print("fin de programa")
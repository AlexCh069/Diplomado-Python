"""  
 un decorador es como un interruptor. Un interruptor que podemos encender 
 o apagar para añadir funcionalidad extra a una función sin necesidad de 
 añadir más código al cuerpo de dicha función. 
 En la práctica un decorador se indica con el signo@ y se pone encima de 
 la función que decora.
 @un_decorador
def mi_funcion():
    # realizar alguna tarea
    return algo

El funcionamiento de los decoradores se basa en tres ideas que vamos a desarrollar
 a continuación y que son las siguientes:
-Dentro de una función se pueden crear más funciones
-Las funciones pueden retornar funciones
-Las funciones se pueden pasar como argumentos a otras funciones    
"""
# FUNCIONES DENTRO DE OTRA FUNCION
def funcion_externa():
    print("Código de la funcion_externa()")
    def funcion_interna():
        print("Código de la funcion_interna()")
    funcion_interna()
#programa principal
#funcion_interna()  no se puede llamar en el pp   
funcion_externa()  
print("fin de programa") 
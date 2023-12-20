class Coche(): # creacion de la clase :class nombre_clase():
    ruedas=4 # atributo asocian con datos
    def desplazamiento(self): # metodos asocian con funciones. self( Almacena el objeto de la clase)
        print("El coche se esta desplazando sobre 4 ruedas")
#PROGRAMA PRINCIPAL        
miVehiculo=Coche() # nombre_objeto=nombre_clase(). Creacion del objeto
print("Mi coche tiene ", miVehiculo.ruedas, " ruedas") #nombre_objeto.nombre_atributo
miVehiculo.desplazamiento() # nombre_objeto.nombre_metodo()
print("FIN DEL PROGRAMA")
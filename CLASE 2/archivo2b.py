#EJEMPLO DE HERENCIA
class Padre():
      caballo="negro"
      ojos="azules"
      def conducir_coche(self):
        print ("La persona sabe conducir coches")
class Hijo(Padre): # class nombre_clase_hija(nombre_clase_padre): Asi se define la herencia en python
      def conducir_moto(self):
        print ("La persona sabe conducir moto")
#PROGRAMA PRINCIPAL        
persona=Hijo() # objeto e la clase hijo
print(persona.caballo) #usando herencia
print(persona.ojos)
persona.conducir_coche()
persona.conducir_moto() 
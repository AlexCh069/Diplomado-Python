#EJEMPLO DE CONSTRUCTOR
class Cachorro():
    def __init__(self, color, raza): #CONSTRUCTOR: Inicializa los aributos de la clase cuando se crea el objeto
        self.color = color
        self.raza = raza
#PROGRAMA PRINCIPAL        
perrito = Cachorro("Marrón claro", "Golden retriever") #CREANDO UN OBJETO
#print("Este es un cachorro de la raza {} y es de color {}".format(perrito.raza, perrito.color))
print(f"este es un cachorro de la raza {perrito.raza} y es de color {perrito.color}")
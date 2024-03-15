import bd
from model import Producto
def run():
    pass
    arroz = Producto('Arroz', 1.25)
    bd.session.add(arroz)
    print(arroz.id)
    agua = Producto('Agua', 0.3)
    bd.session.add(agua)
    bd.session.commit()
    print(arroz.id) #""" #Base.metadata.create_all(bd.engine)
    
#PROGRAMA PRINCIPAL
bd.Base.metadata.create_all(bd.engine)
run()
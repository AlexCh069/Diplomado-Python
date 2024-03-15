import bd
from model import Producto
def run():
   pass
   """ 
    arroz = Producto('Arroz', 1.25)
    bd.session.add(arroz)
    print(arroz.id)
    agua = Producto('Agua', 0.3)
    bd.session.add(agua)
    bd.session.commit()
    print(arroz.id)
"""
   #num_productos = bd.session.query(Producto).count()
   #print("num_productos:",num_productos)
   """ 
   resultados = bd.session.query(Producto).all()
   for producto in resultados:
          print(producto.id,end=" ")
          print(producto.nombre,end=" ")
          print(producto.precio,end=" ")
          print()
   """   
   
   primer_producto = bd.session.query(Producto).first()

# Verificar si se encontró un producto
   """
   if primer_producto:
        print(f"ID: {primer_producto.id}, Nombre: {primer_producto.nombre}, Precio: {primer_producto.precio}")
   else:
        print("No se encontraron productos.")"""
   #agua = bd.session.query(Producto).filter_by(nombre='Agua').first()
   #print(f"ID: {agua.id}, Nombre: {agua.nombre}, Precio: {agua.precio}") 
   #producto_a_actualizar = bd.session.query(Producto).filter_by(id=2).first()

# Verificar si se encontró el producto
   
   """ 
     if producto_a_actualizar:
    # Actualizar el precio del producto
    producto_a_actualizar.precio = 8888
    
    # Confirmar los cambios en la sesión
    bd.session.commit()
   else:
    print("El producto con el ID especificado no fue encontrado.")
   """ 
      
   producto_a_borrar = bd.session.query(Producto).filter_by(id=2).first()

# Verificar si se encontró el producto
  
   if producto_a_borrar:
    # Borrar el producto
    bd.session.delete(producto_a_borrar)
    
    # Confirmar los cambios en la sesión
    bd.session.commit()
    print("El producto ha sido borrado correctamente.")
   else:
        print("El producto con el ID especificado no fue encontrado.")
#PROGRAMA PRINCIPAL
bd.Base.metadata.create_all(bd.engine)
run()
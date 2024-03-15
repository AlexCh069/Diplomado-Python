import base_datos as bd
from cancion import Cancion

def run():
    # luna = Cancion(id = 1,
    #                titulo = 'luna',
    #                minutos = 3,
    #                segundos = 23,
    #                compositor = 'Alexander Ch',
    #                albumes = 'Distopias',
    #                interpretes = 'Lola, Vico C')

    luna = Cancion( 8,'luna roja', 3, 23, 'Alexander Ch')
    
    bd.session.add(luna)
    bd.session.commit()

    print(luna)

bd.Base.metadata.create_all(bd.engine)
run()
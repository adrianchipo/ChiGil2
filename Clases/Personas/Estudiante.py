from PersonaBase import PersonaClaseBase

class Estudiante(PersonaClaseBase):
    def __init__(self, Usuario=None, LimiteLibros=3, LimiteRenovacion=3):
        PersonaClaseBase.__init__(self, LimiteLibros, LimiteRenovacion)
    
    def BuscarLibro(self):
        print('buscar libro')
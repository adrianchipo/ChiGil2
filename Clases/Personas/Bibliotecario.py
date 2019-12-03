from PersonaBase import PersonaClaseBase

class Bibliotecario(PersonaClaseBase):
    def __init__(self, Usuario=None, Contrasena=None):
        PersonaClaseBase.__init__(self, Usuario, Contrasena)
    
    def BuscarLibro(self):
        print('buscar libro')

    def PrestarLibro(self):
        print('PrestarLibro')
    
    def RegresarLibro(self):
        print('RegresarLibro')
    
    def RegistrarEstudiante(self):
        print('RegistrarEstudiante')
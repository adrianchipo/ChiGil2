from abc import ABCMeta, abstractmethod

class PersonaClaseBase(metaclass=ABCMeta):
    def __init__(self, Usuario, Contrasena, LimiteLibros, LimiteRenovacion):
        self.Usuario = Usuario
        self.Contrasena = Contrasena
        self.LimiteLibros = LimiteLibros
        self.LimiteRenovacion = LimiteRenovacion
    
    @abstractmethod
    def BuscarLibro(self):
        pass

    @abstractmethod
    def PrestarLibro(self):
        pass

    @abstractmethod
    def RegresarLibro(self):
        pass

    @abstractmethod
    def RegistrarEstudiante(self):
        pass
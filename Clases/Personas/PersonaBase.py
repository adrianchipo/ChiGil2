import abc

ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()}) 

class PersonaClaseBase(ABC):
    def __init__(self, Usuario, Contrasena, LimiteLibros, LimiteRenovacion):
        self.Usuario = Usuario
        self.Contrasena = Contrasena
        self.LimiteLibros = LimiteLibros
        self.LimiteRenovacion = LimiteRenovacion
    
    @abc.abstractmethod
    def BuscarLibro(self):
        pass

    @abc.abstractmethod
    def PrestarLibro(self):
        pass

    @abc.abstractmethod
    def RegresarLibro(self):
        pass

    @abc.abstractmethod
    def RegistrarEstudiante(self):
        pass
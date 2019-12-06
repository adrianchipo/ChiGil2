from Clases import Libro
from PersonaBase import PersonaClaseBase

class Bibliotecario(PersonaClaseBase):
    def __init__(self, Usuario=None, Contrasena=None):
        PersonaClaseBase.__init__(self, Usuario, Contrasena)
    
    def BuscarLibro(id):
        query="SELECT * FROM `libros` where id_libro = %s"
        cur = self.conn.cursor()
        cur.execute(query, id)

        for row in cur.fetchall():
            print (row[0])
        

    def PrestarLibro(Libro):
        Libro.Prestado = True
        Libro.CalcularFechaEntrega
    
    def RegresarLibro(self):
        Libro.Prestado = False
    
    def RegistrarEstudiante(self):
        print('RegistrarEstudiante')
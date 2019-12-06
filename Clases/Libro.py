import time
import datetime

class Libro:
    def __init__ (self, Titulo, Autor, FechaPrestamo, FechaEntrega, Renovado, Atrasado, Prestado):
        self.Titulo = Titulo
        self.Autor = Autor
        self.FechaPrestamo = FechaPrestamo
        self.FechaEntrega = FechaEntrega
        self.Renovado = Renovado
        self.Atrasado = Atrasado
        self.Prestado = Prestado

    def CalcularFechaEntrega(self):
        self.FechaEntrega = self.FechaPrestamo + datetime.timedelta(days=7)

libro1 = Libro("abc", "juan", datetime.date(2018,1,1), datetime.date(2018,1,1), False, False, False)
libro1.CalcularFechaEntrega()
print(libro1.FechaEntrega)


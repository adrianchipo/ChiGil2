Clase: Libro\
    Método: CalcularFechaEntrega()\
        Argumentos: Libro.FechaPrestamo\
        Requerimentos: Calcula la fecha en la que se debe regresar el libro.\
        Valores de retorno: Libro.FechaEntrega\
        Efecto: Suma siete días a Libro.FechaEntrega\

Clase: Estudiante\
    Método: BuscarLibro()\
        Argumentos: Libro.Titulo\
        Requerimentos: Buscar un libro por título.\
        Valores de retorno: Objeto de clase Libro\
        Efecto: \

Clase: Bibliotecario\
    Método: BuscarLibro()\
        Argumentos: Libro.Titulo\
        Requerimentos: Buscar un libro por título\
        Valores de retorno: Objeto clase libro\
        Efecto:\
    Método: PrestarLibro()\
        Argumentos: Libro.Titulo\
        Requerimentos: Cambia el estado del libro y calcula la fecha de entrega.\
        Valores de retorno: Libro.Prestamo, Libro.FechaEntrega\
        Efecto:\
    Método: RegresarLibro()\
        Argumentos: Libro.Titulo\
        Requerimentos: Cambia el estado del libro a disponible\
        Valores de retorno: Libro.FechaPrestamo, Libro.FechaEntrega\
        Efecto:\
    Método: RegistrarEstudiante()\
        Argumentos: Estudiante.Matricula\
        Requerimentos: Registra al estudiante para no pasar el límite de préstamos\
        Valores de retorno:\
        Efecto:\
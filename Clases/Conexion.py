import MySQLdb

def conexion():
    class program:
        def main():
            print("bienvenidos")
            conn = MySQLdb.connect(*datos)

class conexBD:
    DB_HOST = 'localhost' 
    DB_USER = 'root' 
    DB_PASS = '' 
    DB_NAME = 'prueba' 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
    conn = MySQLdb.connect(*datos)
    try:
        print("conexion exitosa")
    except:
            print("Error al conectar")
    conn.close()     
    print("conexion terminada")
    def query():
        showquery="SELECT * FROM `libros`"
        result = run_query(showquery)
        print result
        while(result):
            print("nombre_libro")
        
    
    def FindBookById(id):
        parametro= raw_input("@id_libro_param")
        query="SELECT * FROM `libros` where id_libro = '%s'", parametro
        result = run_query(query)
        print result
        while(result):
            print("El libro se registro el día:")
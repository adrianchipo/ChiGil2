import MySQLdb
class conexBD:
    def __init__():
        self.DB_HOST = 'localhost' 
        self.DB_USER = 'root' 
        self.DB_PASS = '' 
        self.DB_NAME = 'prueba' 
    
        try:
            # si da error de identado ponlo en una linea xd
            self.conn = MySQLdb.connect(host=self.DB_HOST, 
                                        user=self.DB_USER, 
                                        passwd=self.DB_PASS,
                                        db=self.DB_NAME)
            print("conexion exitosa")
        except:
            print("Error")
    
    
    def query():
        showquery="SELECT * FROM `libros`"
        #result = run_query(showquery)
        cur=self.conn.cursor()
        cur.execute(showquery)
        for row in cur.fetchall():
            print (row[0])
        
    
    def FindBookById(id):
        query="SELECT * FROM `libros` where id_libro = %s"
        cur = self.conn.cursor()
        cur.execute(query, id)

        for row in cur.fetchall():
            print (row[0])

class program:
    def main():
        print("bienvenidos")
        Database = conexBD() # llamar al constructor inicia el metodo __init__()
        Database.query() # llamar al método query.
        Database.FindBookById(1) # encuentra libro con el id = 1
        return

if __name__ == '__main__':
    programa = program()

    programa.main()
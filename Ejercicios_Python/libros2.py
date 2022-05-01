# CREA UN PROGRAMA CON LAS SIGUIENTES FUNCIONALIDADES
"""
- INSERTAR UN NUEO LIBRO PIDIENDO DATOS POR TECLADO
- LISTAR TODOS LOS LIBROS
- Borrar libro pidiendo por teclado el id_dl_libro
SALIR

"""
import mysql.connector # Se instala en el CMD con: pip install mysql-connector-python
import time

# Creo la conexión a BBDD
miBBDD = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="libros"
)

miCursor = miBBDD.cursor()



# Menu por teclado

user = 1

while user != 5 :
    print("\n---- Registro de Libro ----")
    print("1: Inserta libro\n2: Listar libros\n3: Borrar libro\n4: Asociar Autor - Libro\n5: Salir")
    user = int(input("\nSelecciona una opcion:\n"))
    if user == 1:
        miCursor = miBBDD.cursor()
        nombre = input("\nEscribe el nombre del libro: \n")
        isbn = int(input("Escribe el ISBN del libro: \n"))
        year = int(input("Escribe al año de pubicacion del libro: \n"))

        sqlString = "INSERT INTO libro (NOMBRE, ISBN, ANIO_PUBLICACION) VALUES (%s, %s, %s)"
        datos = (nombre, isbn, year)
    
        miCursor.execute(sqlString, datos)
    
        miBBDD.commit()

        print(miCursor.rowcount, "filas insertadas.")

    
    elif user == 2:
        # Ejecuto la sentencia SELECT
        miCursor.execute("SELECT * FROM libro")

        # Recupero los datos resultado de la consulta
        misLibros = miCursor.fetchall()

    # Imprimo los resultados
        for libro in misLibros:
          print(libro)

        miBBDD.commit()

    elif user == 3:
        # Ejecuto la sentencia SELECT
        miCursor.execute("SELECT * FROM libro")

        # Recupero los datos resultado de la consulta
        misLibros = miCursor.fetchall()
        

        id = input("Inserte el ID del libro")


        identificador = "DELETE FROM libro WHERE ID = %s"
        miCursor.execute(identificador, [id])

        miBBDD.commit()



    elif user == 4:

        id_libro = input("Inserte el ID del libro")

        misAutores = []

        while (len(misAutores) == 0):
            id_autor = input("Inserte el ID del autor")
            sqlstring = "SELECT * FROM autor WHERE ID = %s"
            miCursor.execute(sqlstring, [id_autor])
            misAutores = miCursor.fetchall()



        identificador = "UPDATE libro SET ID_AUTOR = %s WHERE ID = %s"
        
        miCursor.execute(identificador, [id_autor, id_libro])

        miBBDD.commit()


    elif user > 5 or user <1:
        print("Opcion no válida\nVuelve a elegir")


miCursor.close()    
miBBDD.close()

time.sleep(5)







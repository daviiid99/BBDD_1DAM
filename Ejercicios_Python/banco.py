import mysql.connector # Se instala en el CMD con: pip install mysql-connector-python
import time

# Creo la conexión a BBDD
miBBDD = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="BANCO"
)

miCursor = miBBDD.cursor()


"""
Funciones

"""


def listarPersonas(numero):
    usuarios = "SELECT * FROM TITULAR LIMIT %s, 5"
    miCursor.execute(usuarios, [numero])
    misClientes = miCursor.fetchall()
    return misClientes


def imprimirLista(lista):
    for item in lista:
        print(item)

"""
Main

"""


# Menu por teclado

user = 0

    

while user != 2 :
    print("\n---- Datos de Banco ----")
    print("1: Listar Usuarios\n2: Salir")

    user = int(input("\nSelecciona una opcion:\n"))

    # Listamos todos los usuarios del banco
    if user == 1:
        contador = 0



        while contador < 20 :
            misPersonas = listarPersonas(contador)
            imprimirLista(misPersonas)

            print("\nEscribe 'N' para siguiente pagina:\nEscribe 'B' para siguiente pagina")

            avanzar = input(" : ")

            if avanzar.upper() == "N":
                contador +=5

            elif avanzar.upper() == "B":
                contador -=5

                if contador < 0:
                    contador = 0
            

        
miCursor.close()    
miBBDD.close()

time.sleep(3)







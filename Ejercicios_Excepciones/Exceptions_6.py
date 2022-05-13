import mysql.connector
def main():
    try:
        cnx = mysql.connector.connect(
            user = str(input("Ingresar usuario: ")),
            password = str(input("Ingresar contraseña: ")),
            host = str(input("Ingresar host: "))
        )
        cursor = cnx.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("La version de MySQL es: {}".format(data[0]))
    except mysql.connector.Error as err:
        print("Error al conectar a MySQL: ", err)

main()

        
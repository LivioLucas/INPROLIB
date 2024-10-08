import mariadb


def get_db_connection():
        conn_params = {
        "user":"root",
        "password" : "123",
        "host" : "localhost",
        "database":"aula16.05_schema"
        }

        connection = mariadb.connect(**conn_params)
        cursor =  connection.cursor()
        cursor.execute("SELECT * FROM usuarios;")
        
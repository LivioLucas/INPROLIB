import mariadb

conn_params= {
"user" : "root",
"password" : "root",
"host" : "localhost",
"database" : "epe_schema"
}

def get_db_connection():
    return mariadb.connect(**conn_params)
    
    
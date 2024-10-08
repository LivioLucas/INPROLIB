from flask import Flask, render_template, request
from db_config import get_db_connection
import mariadb


app = Flask(__name__)

#aqui temos módulos para renderizar página, para navegação.
@app.route("/")
def index(): #este método faz com que a página inicial do projeto seja o "login.html"
    return render_template ("index.html")


#daqui pra frente temos módulos de operação, consulta (login), inserção (cadastros), e relatórios (estoque).
#rota abaixo é para login no sistema, pegando diretamente do form de login na pagina login.html
@app.route("/login", methods = ['POST'])
def checkar_login():
    login = request.form.get('login')
    print(login)
    password = request.form.get('password')
    print(password)
#aqui faremos a conexão com o banco de dados para fazermos a consulta na tabela e só então liberar o login    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT nome, senha FROM usuario WHERE nome = %s AND senha = %s"
        print(query)
        cursor.execute(query,(login, password))
        result = cursor.fetchone()
        print(result)
        cursor.close()
        conn.close()

        if result:
            print("login funcionou")
            return render_template('index.html')
        else:
            print("login não funcionou, mas mesmo assim conectou no BD")
            return render_template('index.html')

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)    
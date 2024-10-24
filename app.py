from flask import Flask, render_template, request
from db_config import get_db_connection
from flask_mail import Mail, Message
import mariadb



app = Flask(__name__)
#CONFIGURAÇÀO PARA FUNÇÃO DE ENVIO DE EMAIL NO BOTÃO ESQUECI MINHA SENHA
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'inprolibfacinpro@gmail.com' 
app.config['MAIL_PASSWORD'] = 'chew suix ehhy sayn'#Facinproprojetointegrador3
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
#aqui temos módulos para renderizar página, para navegação.
@app.route("/")
def index(): #este método faz com que a página inicial do projeto seja o "login.html"
    return render_template ("index.html")

@app.route("/repositorios")
def repositorios():
    return render_template ("repositorios.html")

@app.route("/cadInterno")
def cadInterno():
    return render_template ("cadInterno.html")


@app.route("/cadastro")
def cadastro():
    return render_template ("cadastro.html")

@app.route("/cadcurso")
def cadcurso():
    return render_template ("cadcurso.html")

@app.route("/formularioMandaSenha")
def formularioSenha():
    return render_template ("esqueciasenha.html")

#daqui pra frente temos módulos de operação, consulta (login), inserção (cadastros), e relatórios (estoque).
#rota abaixo é para login no sistema, pegando diretamente do form de login na pagina login.html
@app.route("/login", methods = ['POST'])
def checkar_login():
    login = request.form.get('login')
    password = request.form.get('password')
#aqui faremos a conexão com o banco de dados para fazermos a consulta na tabela e só então liberar o login    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT email, senha FROM usuario WHERE email = %s AND senha = %s"
        cursor.execute(query,(login, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            print("login funcionou")
            return render_template('repositorios.html')
        else:
            print("login não funcionou, mas mesmo assim conectou no BD")
            return render_template('index.html')

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('index.html')
    


@app.route("/cadastrarUsuario", methods=['POST'])
def cadastrarUsuario():
    nomeUser = request.form.get('nome')
    cpfUser = request.form.get('cpf')
    emailUser = request.form.get('email')
    senhaUser = request.form.get('senha')
    confirmaSenhaUser = request.form.get('confirmarSenha')
    print(nomeUser,cpfUser,emailUser, senhaUser, confirmaSenhaUser)
    if senhaUser == confirmaSenhaUser:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            insert_query = """
                INSERT INTO usuario (nome, email, senha, cpf)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (nomeUser, emailUser, senhaUser, cpfUser))
            conn.commit()
            cursor.close()
            conn.close()
            print("usuario cadastrado!")
            return render_template("index.html")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return render_template('index.html')
    else:
        print("senhas não conferem")
        return render_template("cadastro.html")



@app.route('/esquecisenha', methods = ['GET','POST'])
def recuperaSenha():
    emailParaRecuperar = request.form.get('emailRecoverySenha')
    mensagem = Message("TESTE", sender = 'noreply@demo.com', recipients = [emailParaRecuperar])
    mensagem.body = "Ô BURRO, A PORRA DA SENHA É 123456"
    mail.send(mensagem)
    print("enviou o email")
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)    


#este é um exemplo de acesso a uma rota python pelo javascript

#const url = '/minha-rota';  // O endpoint Flask que você deseja chamar
#const dados = { chave: 'valor' };  // Os dados a serem enviados

#fetch(url, {
#method: 'POST',  // Método de requisição (GET, POST, etc.)
#headers: {
#  'Content-Type': 'application/json',  // Tipo de conteúdo a ser enviado
#  },
#  body: JSON.stringify(dados),  // Dados convertidos em JSON
#})
#.then(response => response.json())  // Converte a resposta em JSON
#.then(data => {
#  console.log('Resposta do servidor:', data);
#})
#.catch(error => {
# console.error('Erro:', error);
#});

from flask import Flask, render_template, request, jsonify
from db_config import get_db_connection
from flask_mail import Mail, Message
from datetime import datetime
import mariadb
import os

#IMPORTANTE DENTRO DESSE REPOSITÓRIO TEM O ARQUIVO SQL DO BANCO DE DADOS DO PROJETO, IMPORTE ELE QUANDO FOR USAR

#AQUI DEFINIMOS O CAMINHO DO ARQUIVO QUE SERÁ SALVO
#SERÁ NECESSARIO AJUSTAR CASO SEJA FEITO EM OUTRA MAQUINA
DIRETORIO_upload = "C:\\Users\\livio\\Documents\\GitHub\\INPROLIB\\arquivos\\upload"
DIRETORIO_fotoPerfil = "C:\\Users\\livio\\Documents\\GitHub\\INPROLIB\\static\\img"
diretorio_base = r"C:\Users\livio\Documents\GitHub\INPROLIB"





app = Flask(__name__)
#CONFIGURAÇÀO PARA FUNÇÃO DE ENVIO DE EMAIL NO BOTÃO ESQUECI MINHA SENHA
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'inprolibfacinpro@gmail.com' 
app.config['MAIL_PASSWORD'] = 'chew suix ehhy sayn'#Facinproprojetointegrador3
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def carregarInfoLogin():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        pegar_autor= "SELECT nome_usuario FROM audit_login"
        cursor.execute(pegar_autor)
        usuario_logado = cursor.fetchone()[0]  
        cursor = conn.cursor()
        pegar_cursos = "SELECT imagem_usuario FROM audit_login"
        cursor.execute(pegar_cursos)
        imagem_perfil = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return {
        "usuario_logado": usuario_logado,
        "imagem_perfil": imagem_perfil
        }
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('home.html')   

#aqui temos módulos para renderizar página, para navegação.
@app.route("/")
def index(): 
#este método faz com que a página inicial do projeto seja o "login.html"
    return render_template ("index.html")

@app.route("/repositorios")
def repositorios():
    dados_usuario_logado = carregarInfoLogin()
# rota para renderização da pagina de repositórios "repositorios.html"
    return render_template ("repositorios.html", dados_usuario_logado=dados_usuario_logado)

@app.route("/cadInterno")
def cadInterno():
    dados_usuario_logado = carregarInfoLogin()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        pegar_autor= "SELECT nome FROM usuario"
        cursor.execute(pegar_autor)
        users = cursor.fetchall()  
        cursor = conn.cursor()
        pegar_cursos = "SELECT nome_curso FROM curso"
        cursor.execute(pegar_cursos)
        cursos = cursor.fetchall()
        return render_template("cadInterno.html", cursos=cursos, users=users,dados_usuario_logado=dados_usuario_logado) 
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('home.html')   
# rota para a renderização da pagina de cadastro interno de usuários "cadInterno.html"
    


@app.route("/cadastro")
def cadastro():
    dados_usuario_logado = carregarInfoLogin()
# rota para a renderização da pagina de cadastro externo de usuários para que possam fazer login "cadastro.html"
    return render_template ("cadastro.html", dados_usuario_logado=dados_usuario_logado)

@app.route("/cadcurso")
def cadcurso():
    dados_usuario_logado = carregarInfoLogin()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        pegar_autor= "SELECT nome FROM usuario WHERE tipo = 'Professor'"
        cursor.execute(pegar_autor)
        users = cursor.fetchall()  
        return render_template("cadcurso.html", users=users, dados_usuario_logado=dados_usuario_logado) 
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('index.html') 
# rota para a renderização da pagina de cadastro de cursos "cadcurso.html"
    

@app.route("/formularioMandaSenha")
def formularioSenha():
# rota para a renderização da pagina de inserção de email para solicitar recuperação de senha "formularioMandaSenha.html"
    return render_template ("esqueciasenha.html")

@app.route("/publicacao_conteudo")
def publicacao_conteudo():
    dados_usuario_logado = carregarInfoLogin()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        pegar_autor= "SELECT nome FROM usuario"
        cursor.execute(pegar_autor)
        autores = cursor.fetchall()  
        cursor = conn.cursor()
        pegar_cursos = "SELECT nome_curso FROM curso"
        cursor.execute(pegar_cursos)
        cursos = cursor.fetchall()    
        return render_template("publicacao.html", cursos=cursos, autores=autores, dados_usuario_logado=dados_usuario_logado) 
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('home.html')    

  

#daqui pra frente temos módulos de operação, consulta (login), inserção (cadastros), e relatórios (estoque).
#rota abaixo é para login no sistema, pegando diretamente do form de login na pagina login.html
@app.route("/login", methods=['POST'])
def checkar_login():
    # Obtém o valor do campo 'login' do formulário enviado via POST.
    login = request.form.get('login')
    # Obtém o valor do campo 'password' do formulário enviado via POST.
    password = request.form.get('password')

    # Tentativa de conectar ao banco de dados e realizar a verificação do login.
    try:
        # Chama a função 'get_db_connection' para estabelecer uma conexão com o banco de dados.
        conn = get_db_connection()
        # Cria um cursor para executar comandos SQL no banco de dados.
        cursor = conn.cursor()
        # Define a consulta SQL para buscar o email e senha do usuário na tabela 'usuario'.
        query = "SELECT email, senha FROM usuario WHERE email = %s AND senha = %s"
        # Executa a consulta SQL passando o login e a senha como parâmetros.
        cursor.execute(query, (login, password))
        # Obtém o primeiro resultado da consulta (se houver).
        result = cursor.fetchone()
        query2 = "SELECT foto_perfil FROM usuario WHERE email = %s"
        cursor.execute(query2, (login,))
        imagem = cursor.fetchone()[0]
        query3 = "SELECT nome FROM usuario WHERE email = %s"
        cursor.execute(query3, (login,))
        nome = cursor.fetchone()[0]   
        print(nome) 
        query_audit = "INSERT INTO audit_login (nome_usuario, imagem_usuario, ultimo_login) VALUES (%s, %s, %s)"
        data_login = datetime.now()
        cursor.execute(query_audit, (nome, imagem, data_login))   
        conn.commit() 
        # Fecha o cursor para liberar recursos.
        cursor.close()
        # Fecha a conexão com o banco de dados.
        conn.close()

        # Verifica se a consulta retornou algum resultado (login bem-sucedido).
        if result:
            print("login funcionou")  # Mensagem de sucesso no console.
            # Renderiza a página 'repositorios.html' em caso de login bem-sucedido.
            return render_template('repositorios.html',imagem = imagem, nome = nome)
        else:
            print("login não funcionou, mas mesmo assim conectou no BD")  # Mensagem de falha no login.
            # Renderiza a página 'index.html' em caso de falha no login.
            return render_template('index.html')


    except mariadb.Error as e:
        # Captura e imprime qualquer erro que ocorra ao tentar conectar ao banco de dados.
        print(f"Error connecting to MariaDB Platform: {e}")
        # Renderiza a página 'index.html' em caso de erro.
        return render_template('index.html')



#MÉTODO PARA CADASTRO DE CURSOS (PRIMITIVO) FEITO POR LÍVIO    
@app.route("/cadastrarCurso", methods=['POST'])
def cadastrarCurso():
    # Obtém o valor do campo 'nomeCurso' do formulário enviado via POST.
    nomeCurso = request.form.get('nomeCurso')
    # Obtém o valor do campo 'descricaoCurso' do formulário enviado via POST.
    descricaoCurso = request.form.get('descricaoCurso')
    # Obtém o valor do campo 'codigoCurso' do formulário enviado via POST.
    codigoCurso = request.form.get('codigoCurso')
    nomeCoordenador = request.form.get('coordenadorCurso')
    credCurso = request.form.get('credCurso')
    
    # Impressão dos dados obtidos do formulário para verificação.
    print(nomeCurso, descricaoCurso, codigoCurso)
    
    # Tentativa de conectar ao banco de dados para inserir os dados do curso.
    try:
        # Chama a função 'get_db_connection' para estabelecer uma conexão com o banco de dados.
        conn = get_db_connection()
        # Cria um cursor para executar comandos SQL no banco de dados.
        cursor = conn.cursor()
        cursor.execute('SELECT id_usuario FROM usuario WHERE nome = %s', (nomeCoordenador,))
        id_coordenador = cursor.fetchone()[0] 
        
        
        # Define a consulta SQL para inserir um novo curso na tabela 'curso'.
        insert_query = """
        INSERT INTO curso (nome_curso, descricao_curso, codigo_curso, id_coordenador, autorizacao)
        VALUES (%s, %s, %s, %s, %s)
        """  # Query para inserção de dados na tabela 'curso'.
        
        # Executa a consulta SQL passando os dados do curso como parâmetros.
        cursor.execute(insert_query, (nomeCurso, descricaoCurso, codigoCurso, id_coordenador, credCurso))
        
        # Confirma as alterações no banco de dados.
        conn.commit()
        # Fecha o cursor para liberar recursos.
        cursor.close()
        # Fecha a conexão com o banco de dados.
        conn.close()
        
        # Mensagem de sucesso no console após o cadastro do curso.
        print("curso cadastrado!")
        # Renderiza a página 'repositorios.html' após o cadastro bem-sucedido.
        return render_template("repositorios.html")
    
    except mariadb.Error as e:
        # Captura e imprime qualquer erro que ocorra ao tentar conectar ao banco de dados.
        print(f"Error connecting to MariaDB Platform: {e}")
        # Renderiza a página 'cadcurso.html' em caso de erro no cadastro.
        return render_template('cadcurso.html')
      

#MÉTODO PARA CADASTRO DE USUÁRIOS POR FORA DO SISTEMA, FEITO POR LÍVIO
@app.route("/cadastrarUsuario", methods=['POST'])
def cadastrarUsuario():
    # Obtém o valor do campo 'nome' do formulário enviado via POST.
    nomeUser = request.form.get('nome')
    # Obtém o valor do campo 'cpf' do formulário enviado via POST.
    cpfUser = request.form.get('cpf')
    # Obtém o valor do campo 'email' do formulário enviado via POST.
    emailUser = request.form.get('email')
    # Obtém o valor do campo 'senha' do formulário enviado via POST.
    senhaUser = request.form.get('senha')
    # Obtém o valor do campo 'confirmarSenha' do formulário enviado via POST.
    confirmaSenhaUser = request.form.get('confirmarSenha')
    fotoPerfil = request.files['fotoPerfil']
    nome_fotoPerfil = fotoPerfil.filename
    fotoPerfil.save(os.path.join(DIRETORIO_fotoPerfil, nome_fotoPerfil))
    caminho_fotoPerfil = os.path.join(DIRETORIO_fotoPerfil, nome_fotoPerfil)
    caminho_relativo = os.path.relpath(caminho_fotoPerfil, start=diretorio_base)
    caminho_salvar = "..\\" + caminho_relativo.replace("/", "\\")

    # Impressão dos dados obtidos do formulário para verificação.
    print(nomeUser, cpfUser, emailUser, senhaUser, confirmaSenhaUser)
    
    # Verifica se a senha e a confirmação de senha são iguais.
    if senhaUser == confirmaSenhaUser:
        # Tentativa de conectar ao banco de dados para inserir os dados do usuário.
        try:
            # Chama a função 'get_db_connection' para estabelecer uma conexão com o banco de dados.
            conn = get_db_connection()
            # Cria um cursor para executar comandos SQL no banco de dados.
            cursor = conn.cursor()
            
            # Define a consulta SQL para inserir um novo usuário na tabela 'usuario'.
            insert_query = """
                INSERT INTO usuario (nome, email, senha, cpf, foto_perfil)
                VALUES (%s, %s, %s, %s, %s)
            """
            
            # Executa a consulta SQL passando os dados do usuário como parâmetros.
            cursor.execute(insert_query, (nomeUser, emailUser, senhaUser, cpfUser, caminho_salvar))
            # Confirma as alterações no banco de dados.
            conn.commit()
            # Fecha o cursor para liberar recursos.
            cursor.close()
            # Fecha a conexão com o banco de dados.
            conn.close()
            
            # Mensagem de sucesso no console após o cadastro do usuário.
            print("usuario cadastrado!")
            # Renderiza a página 'index.html' após o cadastro bem-sucedido.
            return render_template("index.html")
        
        except mariadb.Error as e:
            # Captura e imprime qualquer erro que ocorra ao tentar conectar ao banco de dados.
            print(f"Error connecting to MariaDB Platform: {e}")
            # Renderiza a página 'index.html' em caso de erro no cadastro.
            return render_template('index.html')
    else:
        # Mensagem de erro no console se as senhas não conferirem.
        print("senhas não conferem")
        # Renderiza a página 'cadastro.html' para permitir que o usuário tente novamente.
        return render_template("cadastro.html")


#MÉTODO DE RECUPERAÇÃO DE SENHA (PRIMITIVO), FEITO POR LÍVIO
@app.route('/esquecisenha', methods=['GET', 'POST'])
def recuperaSenha():
    # Obtém o valor do campo 'emailRecoverySenha' do formulário enviado via POST.
    emailParaRecuperar = request.form.get('emailRecoverySenha')
    
    # Tentativa de conectar ao banco de dados para recuperar a senha do usuário.
    try:
        # Chama a função 'get_db_connection' para estabelecer uma conexão com o banco de dados.
        conn = get_db_connection()
        # Cria um cursor para executar comandos SQL no banco de dados.
        cursor = conn.cursor()
        
        # Executa a consulta SQL para buscar a senha do usuário com o email fornecido.
        cursor.execute("SELECT senha FROM usuario WHERE email = %s", (emailParaRecuperar,))
        pegar_senha = cursor.fetchone()  # Obtém o resultado da consulta.
        
        # Verifica se a senha foi encontrada.
        if pegar_senha:
            # Acessa o valor da senha, que está na primeira posição do resultado (ex: (123456,)).
            pegar_senha = pegar_senha[0]
        
        # Fecha o cursor para liberar recursos.
        cursor.close()
        # Fecha a conexão com o banco de dados.
        conn.close()
        
        # Impressão da senha recuperada para fins de depuração.
        print(pegar_senha)         
        
        # Cria uma mensagem de email para enviar a senha recuperada ao usuário.
        mensagem = Message("Recuperação de Senha", sender='noreply@demo.com', recipients=[emailParaRecuperar])
        # Define o corpo do email, incluindo a senha recuperada.
        mensagem.body = f"A sua senha é: {pegar_senha} NÃO COMPARTILHE ESSE EMAIL COM NINGUÉM!"
        
        # Envia o email com a senha recuperada.
        mail.send(mensagem)
        # Mensagem de sucesso no console após o envio do email.
        print("Email enviado com sucesso")
        
        # Renderiza a página 'index.html' após o envio do email.
        return render_template('index.html')
    
    except mariadb.Error as e:
        # Captura e imprime qualquer erro que ocorra ao tentar conectar ao banco de dados.
        print(f"Erro ao conectar ao MariaDB: {e}")
        # Renderiza a página 'index.html' em caso de erro.
        return render_template('index.html')

#MÉTODO DE ENVIO DE CONTEÚDO (PRIMITIVO), FEITO POR LÍVIO
@app.route('/upload_conteudo', methods=['POST'])
def upload_conteudo():
    # Obtenha o arquivo enviado pelo formulário
    arquivo = request.files['publicarConteudo']
    # AQUI GUARDAMOS O NOME DO ARQUIVO EM UMA VARIAVEL
    nome_do_conteudo = arquivo.filename
    # AQUI É O MÉTODO PARA SALVAR O ARQUIVO NA PASTA DESEJADA
    arquivo.save(os.path.join(DIRETORIO_upload, nome_do_conteudo))
    # AQUI SALVAMOS O CAMINHO COMPLETO DO ARQUIVO NUMA VARIAVEL
    caminho_do_conteudo = os.path.join(DIRETORIO_upload, nome_do_conteudo)
    # OBTENDO A DATA E HORA ATUAL PARA SALVAR NO BANCO DE DADOS
    timestamp_atual = datetime.now()
    # Obtendo o valor do campo 'nomeAutor' do formulário enviado via POST.
    nomeAutor = request.form.get('nomeAutor')
    # Obtendo o valor do campo 'nomeCursoAutor' do formulário enviado via POST.
    nomeCurso = request.form.get('nomeCursoAutor')
    tipoArquivo = request.form.get('tipoArquivo')
    nome_arquivo = request.form.get('nomeAquivo')
    print(nome_arquivo)
    assunto_publicacao = request.form.get('assuntoPublicacao')
    ano_autoria = request.form.get('ano_autoria')
    print(timestamp_atual)
    print(caminho_do_conteudo)
    try:
        # Chama a função 'get_db_connection' para estabelecer uma conexão com o banco de dados.
        conn = get_db_connection()
        # Cria um cursor para executar comandos SQL no banco de dados.
        cursor = conn.cursor()

        # Busca o id_usuario com base no nome do autor
        cursor.execute('SELECT id_usuario FROM usuario WHERE nome = %s', (nomeAutor,))
        id_usuario = cursor.fetchone()[0]  # Pega apenas o valor do ID

        # Busca o id_curso com base no nome do curso
        cursor.execute('SELECT id_curso FROM curso WHERE nome_curso = %s', (nomeCurso,))
        id_curso = cursor.fetchone()[0]  # Pega apenas o valor do ID

        # Insere os dados na tabela publicacao
        cursor.execute(
           "INSERT INTO publicacao (titulo, arquivo, data_publicacao, id_autor, id_curso, tipo, nome_arquivo, assuntos_relacionados, data_autoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
           (nome_do_conteudo, caminho_do_conteudo, timestamp_atual, id_usuario, id_curso, tipoArquivo, nome_arquivo, assunto_publicacao, ano_autoria)
        )

        # Comita as alterações e fecha a conexão
        conn.commit()
        cursor.close()
        conn.close()

        print("Funcionou")

        

        return render_template('repositorios.html')
    
    except mariadb.Error as e:
        # Captura e imprime qualquer erro que ocorra ao tentar conectar ao banco de dados.
        print(f"Erro ao conectar ao MariaDB: {e}")
        # Renderiza a página 'index.html' em caso de erro.
        return render_template('repositorios.html')
    


@app.route('/alterar_funcao', methods=['POST','GET'])
def alterarfuncao():
    usuario_professor = request.form.get('usuarioFuncProf')
    curso_professor = request.form.get('cursoFuncProf')
    try:
        # Chama a função 'get_db_connection' para estabelecer uma conexão com o banco de dados.
        conn = get_db_connection()
        # Cria um cursor para executar comandos SQL no banco de dados.
        cursor = conn.cursor()
        # Define a consulta SQL para inserir um novo curso na tabela 'curso'.
        update_query = "UPDATE usuario SET tipo = 'Professor' , curso_usuario= %s WHERE nome = %s;"  # Query para inserção de dados na tabela 'curso'.
        
        # Executa a consulta SQL passando os dados do curso como parâmetros.
        cursor.execute(update_query, ( curso_professor, usuario_professor))
        
        # Confirma as alterações no banco de dados.
        conn.commit()
        # Fecha o cursor para liberar recursos.
        cursor.close()
        # Fecha a conexão com o banco de dados.
        conn.close()
        
        # Mensagem de sucesso no console após o cadastro do curso.
        print("funcionou!")
        # Renderiza a página 'repositorios.html' após o cadastro bem-sucedido.
        return render_template("cadInterno.html")
    
    except mariadb.Error as e:
        # Captura e imprime qualquer erro que ocorra ao tentar conectar ao banco de dados.
        print(f"Error connecting to MariaDB Platform: {e}")
        # Renderiza a página 'cadcurso.html' em caso de erro no cadastro.
        return render_template('cadcurso.html')
    
@app.route('/alterar_funcao_aluno', methods=['POST','GET'])
def alterarfuncaoaluno():
    usuario_aluno = request.form.get('usuarioFuncaluno')
    curso_aluno = request.form.get('cursoFuncaluno')
    try:
        # Chama a função 'get_db_connection' para estabelecer uma conexão com o banco de dados.
        conn = get_db_connection()
        # Cria um cursor para executar comandos SQL no banco de dados.
        cursor = conn.cursor()
        # Define a consulta SQL para inserir um novo curso na tabela 'curso'.
        update_query = "UPDATE usuario SET tipo = 'Aluno' , curso_usuario= %s WHERE nome = %s;"  # Query para inserção de dados na tabela 'curso'.
        
        # Executa a consulta SQL passando os dados do curso como parâmetros.
        cursor.execute(update_query, ( curso_aluno, usuario_aluno))
        
        # Confirma as alterações no banco de dados.
        conn.commit()
        # Fecha o cursor para liberar recursos.
        cursor.close()
        # Fecha a conexão com o banco de dados.
        conn.close()
        
        # Mensagem de sucesso no console após o cadastro do curso.
        print("funcionou!")
        # Renderiza a página 'repositorios.html' após o cadastro bem-sucedido.
        return render_template("cadInterno.html")
    
    except mariadb.Error as e:
        # Captura e imprime qualquer erro que ocorra ao tentar conectar ao banco de dados.
        print(f"Error connecting to MariaDB Platform: {e}")
        # Renderiza a página 'cadcurso.html' em caso de erro no cadastro.
        return render_template('cadcurso.html')




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

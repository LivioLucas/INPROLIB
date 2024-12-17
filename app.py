from flask import Flask, render_template, request
from db_config import get_db_connection
import mariadb
<<<<<<< Updated upstream
=======
import os

#IMPORTANTE DENTRO DESSE REPOSITÓRIO TEM O ARQUIVO SQL DO BANCO DE DADOS DO PROJETO, IMPORTE ELE QUANDO FOR USAR

#AQUI DEFINIMOS O CAMINHO DO ARQUIVO QUE SERÁ SALVO
#SERÁ NECESSARIO AJUSTAR CASO SEJA FEITO EM OUTRA MAQUINA
DIRETORIO_upload = "C:\\Users\\Victor Hugo\\Documents\\GitHub\\INPROLIB\\arquivos\\upload"
DIRETORIO_fotoPerfil = "C:\\Users\\Victor Hugo\\Documents\\GitHub\\INPROLIB\\static\\img"
diretorio_base = r"C:\Users\Victor Hugo\Documents\GitHub\INPROLIB"


>>>>>>> Stashed changes


app = Flask(__name__)

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
        query = "SELECT nome, senha FROM usuario WHERE nome = %s AND senha = %s"
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

<<<<<<< Updated upstream
=======

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

@app.route("/relatorios")
def relatorios():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        pegar_autor= "SELECT nome, id_usuario FROM usuario"
        cursor.execute(pegar_autor)
        users = cursor.fetchall()  
        cursor = conn.cursor()
        pegar_cursos = "SELECT nome_curso, id_curso FROM curso"
        cursor.execute(pegar_cursos)
        cursos = cursor.fetchall()
        pegar_tipos = "SELECT nome_tipo, id FROM tipos_de_publicacao"
        cursor.execute(pegar_tipos)
        tipos = cursor.fetchall()
        print(cursos)
        return render_template("relatorios.html", cursos=cursos, users=users, tipos=tipos) 
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('home.html')   
    
@app.route('/filtrar', methods=['POST'])
def filtrar():
    print("entrou")
    filtros = request.json  # Recebe os filtros como JSON
    curso = filtros.get('curso')
    autor = filtros.get('autor')
    tipo = filtros.get('tipo')
    data_inicial = filtros.get('data_inicial')
    data_final = filtros.get('data_final')
    print(curso,autor,tipo,data_inicial,data_final)
    
    
    query = """
    SELECT 
        p.id_publicacao,
        p.titulo,
        a.nome AS nome_autor,
        p.tipo AS nome_tipo,
        c.nome_curso AS nome_curso,
        p.data_publicacao
    FROM 
        publicacao p
    LEFT JOIN usuario a ON p.id_autor = a.id_usuario
    LEFT JOIN tipos_de_publicacao t ON p.tipo = t.id
    LEFT JOIN curso c ON p.id_curso = c.id_curso
    WHERE 1=1

    """
    params = []

    if curso:
        query += " AND p.id_curso = %s"
        params.append(curso)

    if autor:
        query += " AND p.id_autor = %s"
        params.append(autor)

    if tipo:
        query += " AND p.tipo = %s"
        params.append(tipo)

    if data_inicial:
        query += " AND p.data_publicacao >= %s"
        params.append(data_inicial)

    if data_final:
        query += " AND p.data_publicacao <= %s"
        params.append(data_final)


    print(query)
    print(params)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        
        print(resultados)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


>>>>>>> Stashed changes
if __name__ == "__main__":
    app.run(debug=True)    
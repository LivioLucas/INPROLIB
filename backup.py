#rota abaixo para a página cadastros de pessoas
@app.route('/cad_pessoas_pagina')
def abrir_cad_pessoas():
    return render_template("cad_pessoas.html")

#rota abaixo para a página de emissão de ordens de produção
@app.route('/lan_emissao')
def lan_emissão():
    return render_template("lan_emissao.html")

#rota abaixo para a página de lançamentos
@app.route('/lan_produto')
def lan_produto():
  #conexão com o banco da dados para mostrar nomes de fornecedores e entradas no banco de dados  
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        pegar_entrada = "SELECT nome_entrada FROM entrada"
        cursor.execute(pegar_entrada)
        entradas = cursor.fetchall()  
        print(entradas) 
        cursor = conn.cursor()
        pegar_fornecedores = "SELECT empresa_forn FROM fornecedor"
        cursor.execute(pegar_fornecedores)
        fornecedores = cursor.fetchall()    
        return render_template("lan_produto.html", fornecedores=fornecedores, entradas=entradas)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('home.html')
    
    
def pegar_estoque_entrada():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT cod_entrada, lan_entrada, lan_fornecedor, lote_entrada, lan_tipo_entrada, data_fab, quantidade, und_medida FROM estoque_entrada')
    dados = cursor.fetchall()
    conn.close()
    return dados

#rota abaixo para a página de estoque 
@app.route('/estoque')
def estoque():
        estoque_entrada= pegar_estoque_entrada()
        return render_template("estoque.html",estoque_entrada = estoque_entrada)

    

#rota abaixo para a página de baixa de estoque
@app.route('/baixa_estoque')
def baixa_estoque():
    return render_template("baixa_estoque.html")

#rota abaixo para a página home
@app.route('/home')
def home():
   return render_template("home.html")
    
#rota abaixo para a página cadastros de produção
@app.route('/cad_producao_pagina')
def abrir_cad_producao():
#essa conexão busca o nome de todos os nossos fornecedores para que possamos cadastrar as entradas
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        pegar_fornecedores = "SELECT empresa_forn FROM fornecedor"
        cursor.execute(pegar_fornecedores)
        fornecedores = cursor.fetchall()        
        return render_template("cad_producao.html", fornecedores=fornecedores)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('home.html')

#daqui pra frente temos módulos de operação, consulta (login), inserção (cadastros), e relatórios (estoque).
#rota abaixo é para login no sistema, pegando diretamente do form de login na pagina login.html
@app.route("/login", methods = ['POST'])
def checkar_login():
    cpf = request.form.get('cpf')
    senha = request.form.get('senha')
#aqui faremos a conexão com o banco de dados para fazermos a consulta na tabela e só então liberar o login    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT cpf, senha FROM usuario WHERE cpf = %s AND senha = %s"
        cursor.execute(query, (cpf, senha))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            return render_template('home.html')
        else:
            print("login não funcionou")
            return render_template('login.html')

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return render_template('login.html')
    
        
#rota abaixo é para cadastro de usuários, pegando diretamente do form de usuários na pagina cad_pessoas.html
@app.route("/cad_user", methods =['POST'])
def cad_user():
    nome = request.form.get('nome')
    cpf_user = request.form.get('cpf')
    senha_user = request.form.get('senha')
    email_user = request.form.get('email')
    funcao_user = request.form.get('funcao')
    confirm_senha_user = request.form.get('confirma_senha')
    print(nome,cpf_user, email_user, funcao_user,senha_user, confirm_senha_user)
    #aqui faremos a conexão com o BD para inserir os dados na tabela usuarios
    if senha_user == confirm_senha_user:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            insert_query = """
                INSERT INTO usuario (nome, email, senha, cpf, funcao)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (nome, email_user, senha_user, cpf_user, funcao_user))
            conn.commit()
            cursor.close()
            conn.close()
            return render_template("home.html")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return render_template('cad_pessoas.html')
    else:
        print("senhas não conferem")
        return render_template('cad_pessoas.html')
    
#rota abaixo é para cadastro de fornecedores, pegando diretamente do form na página cad_pessoas.html
@app.route('/cad_fornecedor', methods = ['POST'])
def cad_fornecedor():
    empresa_forn = request.form.get('nome_fornecedor')
    cnpj_forn = request.form.get('cnpj_fornecedor')
    cep_forn = request.form.get('cep_fornecedor')
    endereco_forn = request.form.get('endereco_fornecedor')
    bairro_forn = request.form.get('bairro_fornecedor')
    uf_forn = request.form.get('uf_fornecedor')
    gestor_forn = request.form.get('gestor_fornecedor')
    email_forn = request.form.get('email_fornecedor')
    cidade_forn = request.form.get('cidade_fornecedor')
    telefone_forn = request.form.get('telefone_fornecedor')
    #aqui faremos a conexão com o banco de dados para gravar o fornecedor no nosso BD
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_query = """
                INSERT INTO fornecedor (empresa_forn, cnpj_forn, cep_forn, endereco_forn, bairro_forn, uf_forn, gestor_forn, email_forn, cidade_forn, telefone_forn)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        cursor.execute(insert_query, (empresa_forn, cnpj_forn, cep_forn, endereco_forn, bairro_forn, uf_forn, gestor_forn, email_forn, cidade_forn, telefone_forn ))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template("home.html")
    except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return render_template('cad_pessoas.html')
    

#rota abaixo é para cadastro de entradas, pegando diretamente do form na página cad_producao.html
@app.route('/cad_entradas', methods = ['POST'])
def cad_entradas():
    cod_entrada = request.form.get('cod_entrada')
    unid_medida_entrada = request.form.get('unid_medida_entrada')
    nome_entrada = request.form.get('nome_entrada')
    validade_entrada = request.form.get('validade_entrada')
    tipo_entrada = request.form.get('tipo_entrada')
    est_min_entrada = request.form.get('est_min_entrada')
    fornecedor_id = request.form.get('fornecedor')    
    data_cad_entrada = request.form.get('data_cad_entrada')
    print(cod_entrada, unid_medida_entrada, nome_entrada, validade_entrada, tipo_entrada, est_min_entrada, fornecedor_id, data_cad_entrada )
    #aqui iremos realizar a conexão com o banco de dados para trazer os dados de fornecedor e gravar os dados inseridos
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_query = """
                INSERT INTO entrada (cod_entrada, unid_medida_entrada, nome_entrada, validade_entrada, tipo_entrada, est_min_entrada, fornecedor_id, data_cad_entrada)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """       
        cursor.execute(insert_query, (cod_entrada, unid_medida_entrada, nome_entrada, validade_entrada, tipo_entrada, est_min_entrada, fornecedor_id, data_cad_entrada ))
        conn.commit()
        cursor.close()
        conn.close()        
        return render_template ('home.html')
    except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return render_template('cad_pessoas.html')
        
@app.route('/lancamentos', methods=['POST'])
def lancamentos():
    cod_entrada = request.form.get('cod_entrada')
    lan_entrada = request.form.get('lan_entrada')
    lan_fornecedor = request.form.get('lan_fornecedor')
    lote_entrada = request.form.get('lote_entrada')
    lan_tipo_entrada = request.form.get('lan_tipo_entrada')
    data_fab = request.form.get('data_fab')
    quantidade = request.form.get('quantidade')
    und_medida = request.form.get('und_medida')
    print(cod_entrada,lan_entrada,lan_fornecedor,lote_entrada,lan_tipo_entrada,data_fab,quantidade, und_medida)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO estoque_entrada (cod_entrada, lan_entrada, lan_fornecedor, lote_entrada, lan_tipo_entrada, data_fab, quantidade, und_medida)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """       
        cursor.execute(insert_query, (cod_entrada,lan_entrada,lan_fornecedor,lote_entrada,lan_tipo_entrada,data_fab,quantidade, und_medida))
        conn.commit()
        cursor.close()
        conn.close()        
        return render_template ('home.html')
    except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return render_template('cad_pessoas.html')

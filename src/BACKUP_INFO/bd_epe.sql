-- tabela de usuário
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(60),
    senha VARCHAR(20),
    cpf VARCHAR(30)
    funcao VARCHAR(15)
);
-- tabela de fornecedor 
CREATE TABLE fornecedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    empresa_forn VARCHAR (60),
    cnpj_forn VARCHAR UNIQUE (20),
    cep_forn VARCHAR (20),
    endereco_forn VARCHAR (100),
    bairro_forn  VARCHAR (50),
    uf_forn VARCHAR (40),
    gestor_forn VARCHAR (60),
    email_forn VARCHAR (60),
    cidade_forn VARCHAR (60),
    telefone_forn VARCHAR (30),
);
-- tabela de entrada
CREATE TABLE entrada (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod_entrada VARCHAR (60),
    unid_medida_entrada VARCHAR (20),
    nome_entrada VARCHAR (20),
    validade_entrada VARCHAR (100),
    tipo_entrada  VARCHAR (50),
    est_min_entrada VARCHAR (40),
    fornecedor VARCHAR (60),
    data_cad_entrada VARCHAR (60)
);
CREATE TABLE estoque_entrada (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod_entrada VARCHAR (60),
    lan_entrada VARCHAR (20),
    lan_fornecedor VARCHAR (20),
    lote_entrada VARCHAR (100),
    lan_tipo_entrada  VARCHAR (50),
    data_fab VARCHAR (40),
    quantidade VARCHAR (60)
);
-- inserção de usuário master
INSERT INTO usuario (nome, email, senha, cpf, funcao)
VALUES ("Lívio Lucas","liviool23@gmail.com", "123456", "702.121.941-51", "master");

-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           11.5.2-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para inprolib_schema
CREATE DATABASE IF NOT EXISTS `inprolib_schema` /*!40100 DEFAULT CHARACTER SET armscii8 COLLATE armscii8_bin */;
USE `inprolib_schema`;

-- Copiando estrutura para tabela inprolib_schema.audit_login
CREATE TABLE IF NOT EXISTS `audit_login` (
  `id_audit` int(11) NOT NULL AUTO_INCREMENT,
  `nome_usuario` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `imagem_usuario` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ultimo_login` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_audit`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Copiando dados para a tabela inprolib_schema.audit_login: ~29 rows (aproximadamente)
INSERT INTO `audit_login` (`id_audit`, `nome_usuario`, `imagem_usuario`, `ultimo_login`) VALUES
	(2, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 16:33:18'),
	(3, 'Leonardo Santos Henrique Melo', 'C:\\Users\\livio\\Documents\\GitHub\\INPROLIB\\fotoperfil\\Screenshot_1.png', '2024-12-04 16:34:26'),
	(4, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 21:46:28'),
	(5, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 22:12:47'),
	(6, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 22:19:17'),
	(7, 'teste', '..\\static\\img\\pentagono.png', '2024-12-04 22:23:02'),
	(8, 'teste', '..\\static\\img\\pentagono.png', '2024-12-04 22:23:33'),
	(9, 'teste', '..\\static\\img\\pentagono.png', '2024-12-04 22:26:53'),
	(10, 'TCHÊRERE', '..\\static\\img\\tcherere.png', '2024-12-04 22:35:09'),
	(11, 'TCHÊRERE', '..\\static\\img\\tcherere.png', '2024-12-04 22:35:39'),
	(12, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 22:35:48'),
	(13, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 22:38:56'),
	(14, 'TCHÊRERE', '..\\static\\img\\tcherere.png', '2024-12-04 22:39:04'),
	(15, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 22:42:02'),
	(16, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 22:46:08'),
	(17, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-04 22:53:08'),
	(18, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-10 15:49:46'),
	(19, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-10 15:50:15'),
	(20, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-16 16:22:09'),
	(21, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-16 16:22:26'),
	(22, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-16 23:42:56'),
	(23, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 00:32:10'),
	(24, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 00:32:27'),
	(25, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 00:34:37'),
	(26, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 00:37:01'),
	(27, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 00:54:12'),
	(28, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 00:56:11'),
	(29, 'Gustavo Henrique Suriane', '..\\static\\img\\wppLIVIO.jpg', '2024-12-17 01:00:01'),
	(30, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 01:07:53'),
	(31, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 16:01:50'),
	(32, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 16:18:14'),
	(33, 'Lívio Lucas', '..\\static\\img\\fotoLivio.png', '2024-12-17 16:51:00'),
	(34, 'Lucas Rodrigues Vargas', '..\\static\\img\\wppLIVIO.jpg', '2024-12-17 16:52:09');

-- Copiando estrutura para tabela inprolib_schema.curso
CREATE TABLE IF NOT EXISTS `curso` (
  `id_curso` int(11) NOT NULL AUTO_INCREMENT,
  `nome_curso` varchar(255) NOT NULL,
  `id_coordenador` int(11) DEFAULT NULL,
  `descricao_curso` varchar(50) DEFAULT NULL,
  `codigo_curso` varchar(50) DEFAULT NULL,
  `autorizacao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_curso`),
  KEY `id_coordenador` (`id_coordenador`),
  CONSTRAINT `curso_ibfk_1` FOREIGN KEY (`id_coordenador`) REFERENCES `usuario` (`id_usuario`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.curso: ~5 rows (aproximadamente)
INSERT INTO `curso` (`id_curso`, `nome_curso`, `id_coordenador`, `descricao_curso`, `codigo_curso`, `autorizacao`) VALUES
	(4, 'Psicologia', NULL, 'Curso de Bacharelado em Psicologia', 'PSI2024/2', 'teste do livio'),
	(5, 'Administração', 13, 'Curso de Administração', 'ADM 2024.2', 'teste do livio'),
	(6, 'Enfermagem', 15, 'Curso de Enfermagem 2024.2', 'ENF 2024.2', 'TESTE TCHERERE'),
	(7, 'teste', 13, 'teste', 'teste', 'TESTE TCHERERE'),
	(8, 'Curso de Acupuntura', 13, 'Pós Graduação em Acupuntura', 'ACUP2024.2', '1095'),
	(9, 'Curso de Logística', 11, 'Graduação em Logistica', 'LOG.2024-2', '6474/24');

-- Copiando estrutura para tabela inprolib_schema.esqueci_senha
CREATE TABLE IF NOT EXISTS `esqueci_senha` (
  `id_solicitacao` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `data_solicitacao` datetime NOT NULL,
  `status` enum('Ativo','Expirado') NOT NULL,
  PRIMARY KEY (`id_solicitacao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.esqueci_senha: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela inprolib_schema.funcao
CREATE TABLE IF NOT EXISTS `funcao` (
  `id_funcao` int(11) NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  PRIMARY KEY (`id_funcao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.funcao: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela inprolib_schema.logs
CREATE TABLE IF NOT EXISTS `logs` (
  `id_log` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) DEFAULT NULL,
  `atividade` varchar(255) NOT NULL,
  `data_hora` datetime NOT NULL,
  PRIMARY KEY (`id_log`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `logs_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.logs: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela inprolib_schema.publicacao
CREATE TABLE IF NOT EXISTS `publicacao` (
  `id_publicacao` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `data_publicacao` timestamp NOT NULL,
  `id_autor` int(11) DEFAULT NULL,
  `id_curso` int(11) DEFAULT NULL,
  `tipo` varchar(255) NOT NULL DEFAULT '',
  `status` enum('Publicado','Desativado') NOT NULL,
  `arquivo` varchar(255) DEFAULT NULL,
  `nome_arquivo` varchar(255) DEFAULT NULL,
  `assuntos_relacionados` varchar(255) DEFAULT NULL,
  `data_autoria` date DEFAULT NULL,
  PRIMARY KEY (`id_publicacao`),
  KEY `id_autor` (`id_autor`),
  KEY `id_curso` (`id_curso`),
  CONSTRAINT `publicacao_ibfk_1` FOREIGN KEY (`id_autor`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `publicacao_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`id_curso`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.publicacao: ~3 rows (aproximadamente)
INSERT INTO `publicacao` (`id_publicacao`, `titulo`, `data_publicacao`, `id_autor`, `id_curso`, `tipo`, `status`, `arquivo`, `nome_arquivo`, `assuntos_relacionados`, `data_autoria`) VALUES
	(14, '1732719355852.pdf', '2024-11-27 17:28:36', 15, 5, 'Tese', 'Publicado', 'C:\\Users\\livio\\Documents\\GitHub\\INPROLIB\\arquivos\\upload\\1732719355852.pdf', 'Testando commit', 'teste', '2024-11-12'),
	(15, '1734379903304.pdf', '2024-12-17 00:58:17', 11, 8, 'Dissertações', 'Publicado', 'C:\\Users\\livio\\Documents\\GitHub\\INPROLIB\\arquivos\\upload\\1734379903304.pdf', 'Acupuntura e os benefícios da Saúde ', 'Saúde', '2024-12-16'),
	(16, '24100757.58_-_José_Guilherme_Paciléo_Zanardo_-_17122024112354208.pdf', '2024-12-17 16:54:00', 17, 9, 'Monografia', 'Publicado', 'C:\\Users\\livio\\Documents\\GitHub\\INPROLIB\\arquivos\\upload\\24100757.58_-_José_Guilherme_Paciléo_Zanardo_-_17122024112354208.pdf', 'Cargas Orgânicas ', 'Logistica', '2024-12-17');

-- Copiando estrutura para tabela inprolib_schema.relatorio
CREATE TABLE IF NOT EXISTS `relatorio` (
  `id_relatorio` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` enum('Por Curso','Por Data','Por Pessoa') NOT NULL,
  `data_geracao` date NOT NULL,
  PRIMARY KEY (`id_relatorio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.relatorio: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela inprolib_schema.tipos_de_publicacao
CREATE TABLE IF NOT EXISTS `tipos_de_publicacao` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome_tipo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin;

-- Copiando dados para a tabela inprolib_schema.tipos_de_publicacao: ~4 rows (aproximadamente)
INSERT INTO `tipos_de_publicacao` (`id`, `nome_tipo`) VALUES
	(1, 'TCC'),
	(2, 'Dissertação'),
	(3, 'Monografia'),
	(4, 'Tese');

-- Copiando estrutura para tabela inprolib_schema.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `cpf` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `tipo` enum('Funcionário','Professor','Coordenador','Secretaria','Bibliotecaria','Aluno') NOT NULL,
  `foto_perfil` varchar(255) DEFAULT NULL,
  `curso_usuario` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.usuario: ~5 rows (aproximadamente)
INSERT INTO `usuario` (`id_usuario`, `nome`, `email`, `cpf`, `senha`, `tipo`, `foto_perfil`, `curso_usuario`) VALUES
	(11, 'Lívio Lucas', 'liviool123@gmail.com', '702.121.941-51', '486575', 'Professor', '..\\static\\img\\fotoLivio.png', 'Curso de Acupuntura'),
	(13, 'Leonardo Santos Henrique Melo', 'leoshmello@gmail.com', '810.301.940-25', '794613', 'Professor', 'C:\\Users\\livio\\Documents\\GitHub\\INPROLIB\\fotoperfil\\Screenshot_1.png', 'Psicologia'),
	(14, 'teste', 'teste@gmail.com', '686.013.600-68', '123', 'Aluno', '..\\static\\img\\pentagono.png', 'Administração'),
	(15, 'TCHÊRERE', 'gustavoteste@gmail.com', '113.233.720-83', '123123', 'Professor', '..\\static\\img\\tcherere.png', 'Administração'),
	(16, 'Gustavo Henrique Suriane', 'gusSuriane@gmail.com', '984.864.811-21', '159159', 'Funcionário', '..\\static\\img\\wppLIVIO.jpg', NULL),
	(17, 'Lucas Rodrigues Vargas', 'Lucas@gmail.com', '662.181.111-23', '321321', 'Aluno', '..\\static\\img\\wppLIVIO.jpg', 'Curso de Logística');

-- Copiando estrutura para tabela inprolib_schema.usuario_curso
CREATE TABLE IF NOT EXISTS `usuario_curso` (
  `id_usuario` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  PRIMARY KEY (`id_usuario`,`id_curso`),
  KEY `id_curso` (`id_curso`),
  CONSTRAINT `usuario_curso_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `usuario_curso_ibfk_2` FOREIGN KEY (`id_curso`) REFERENCES `curso` (`id_curso`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.usuario_curso: ~0 rows (aproximadamente)

-- Copiando estrutura para tabela inprolib_schema.usuario_funcao
CREATE TABLE IF NOT EXISTS `usuario_funcao` (
  `id_usuario` int(11) NOT NULL,
  `id_funcao` int(11) NOT NULL,
  PRIMARY KEY (`id_usuario`,`id_funcao`),
  KEY `id_funcao` (`id_funcao`),
  CONSTRAINT `usuario_funcao_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `usuario_funcao_ibfk_2` FOREIGN KEY (`id_funcao`) REFERENCES `funcao` (`id_funcao`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela inprolib_schema.usuario_funcao: ~0 rows (aproximadamente)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

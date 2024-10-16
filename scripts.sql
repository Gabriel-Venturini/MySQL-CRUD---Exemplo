-- Cria o banco de dados
CREATE DATABASE IF NOT EXISTS empresa;

-- Apaga o banco de dados
DROP SCHEMA `empresa`;

-- Usa o banco de dados criado
USE empresa;

-- Cria a tabela 'funcionarios'
CREATE TABLE IF NOT EXISTS funcionarios (
    id INT not null AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    cargo VARCHAR(50),
    salario DECIMAL(10,2)
);

-- Deleta todos os dados dos funcionarios
DELETE FROM funcionarios;

-- Deleta funcionario especifico
delete from funcionarios where id = 2;

-- Inserir dados ficticios no BD
INSERT INTO funcionarios (nome, email, cargo, salario) VALUES 
('João Silva', 'joao.silva@email.com', 'Desenvolvedor', 4500.50),
('Maria Oliveira', 'maria.oliveira@email.com', 'Gerente', 7500.00),
('Carlos Souza', 'carlos.souza@email.com', 'Analista', 3800.25),
('Ana Lima', 'ana.lima@email.com', 'Designer', 3200.40),
('Pedro Fernandes', 'pedro.fernandes@email.com', 'Consultor', 5000.00),
('Fernanda Costa', 'fernanda.costa@email.com', 'Especialista', 6200.75),
('Roberto Dias', 'roberto.dias@email.com', 'Coordenador', 5500.60),
('Camila Nunes', 'camila.nunes@email.com', 'Secretária', 2500.00),
('Lucas Martins', 'lucas.martins@email.com', 'Estagiário', 1500.00),
('Paula Ribeiro', 'paula.ribeiro@email.com', 'Engenheira', 8000.90);

-- Visualiza tabela completa
SELECT * FROM funcionarios;

-- Atualiza dados de funcionario especifico
UPDATE empresa.funcionarios
SET nome='Paula Ribeiro', email='paula.ribeiro@email.com', cargo='Engenheira', salario=8000.90
WHERE id=63;
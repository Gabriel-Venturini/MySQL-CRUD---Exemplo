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
DELETE FROM empresa.funcionarios
WHERE id;
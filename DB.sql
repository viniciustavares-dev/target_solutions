-- Tabela de Usuários
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL, 
    role VARCHAR(255) NOT NULL DEFAULT 'usuario' 
);

-- Tabela de Projetos
CREATE TABLE projetos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    gerente_id INTEGER REFERENCES usuarios(id)
);

-- Tabela de Tarefas
CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    status VARCHAR(255) NOT NULL DEFAULT 'pendente', 
    projeto_id INTEGER REFERENCES projetos(id), 
    responsavel_id INTEGER REFERENCES usuarios(id)
);
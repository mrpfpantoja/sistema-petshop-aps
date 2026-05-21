import sqlite3

DATABASE_NAME = "clinica_veterinaria.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute("PRAGMA foreign_keys = ON;") # Ativa chaves estrangeiras
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Criação das tabelas usando estritamente INT e VARCHAR do seu colega
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INT PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(30) NOT NULL,
            email VARCHAR(30) NOT NULL UNIQUE,
            senha VARCHAR(15) NOT NULL,
            telefone VARCHAR(20),
            tipo_usuario VARCHAR(20) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
            id_cliente INT PRIMARY KEY AUTOINCREMENT,
            id_usuario INT NOT NULL,
            cpf VARCHAR(30) NOT NULL UNIQUE,
            residencia VARCHAR(50), 
            dataNascimento VARCHAR(10) NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Funcionarios (
            id_funcionario INT PRIMARY KEY AUTOINCREMENT,
            id_usuario INT NOT NULL,
            cargo VARCHAR(50) NOT NULL,
            salarios FLOAT NOT NULL, 
            crmv VARCHAR(50),
            dataNascimento VARCHAR(10),                               
            FOREIGN KEY (id_usuario) REFERENCES Usuarios(id) ON DELETE CASCADE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Pets (
            id_pet INT PRIMARY KEY AUTOINCREMENT,
            id_cliente INT NOT NULL,
            nome VARCHAR(50) NOT NULL,
            idade INT,
            especie VARCHAR(25) NOT NULL,
            raca VARCHAR(25),                                
            observacoes VARCHAR(100) NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) ON DELETE CASCADE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Servicos (
            id_servico INT PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL UNIQUE,
            tipo VARCHAR(50),
            preco_base FLOAT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Agendamentos (
            id_agendamento INT PRIMARY KEY AUTOINCREMENT,
            id_cliente INT NOT NULL,
            id_pet INT NOT NULL,
            id_funcionario INT,
            data VARCHAR(10) NOT NULL,     
            hora VARCHAR(8) NOT NULL,     
            status VARCHAR(100) NOT NULL DEFAULT 'Agendado',
            valor_total FLOAT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
            FOREIGN KEY (id_pet) REFERENCES Pets(id_pet),
            FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ItensServico (
            id_item INT PRIMARY KEY AUTOINCREMENT,
            id_agendamento INT NOT NULL,
            id_servico INT NOT NULL,
            preco FLOAT NOT NULL,
            FOREIGN KEY (id_agendamento) REFERENCES Agendamentos(id_agendamento) ON DELETE CASCADE,
            FOREIGN KEY (id_servico) REFERENCES Servicos(id_servico)
        )
    """)
    conn.commit()
    conn.close()
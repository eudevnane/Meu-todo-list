import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

# Adicionar a coluna 'concluida' se ela ainda não existir
try:
    cursor.execute("ALTER TABLE tarefas ADD COLUMN concluida BOOLEAN DEFAULT 0;")
    print("Coluna 'concluida' adicionada com sucesso!")
except sqlite3.OperationalError:
    print("A coluna 'concluida' já existe no banco de dados.")

# Salvar e fechar
conexao.commit()
conexao.close()

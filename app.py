from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco e criar a tabela se não existir
def conectar_bd():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conteudo TEXT NOT NULL,
            concluida INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Rota principal: exibe a lista de tarefas
@app.route('/')
def index():
    conectar_bd()  # Garante que a tabela existe
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return render_template("index.html", tarefas=tarefas)

# Rota para adicionar tarefas
@app.route('/adicionar', methods=['POST'])
def adicionar():
    conteudo = request.form.get("conteudo")
    if conteudo:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (conteudo) VALUES (?)", (conteudo,))
        conn.commit()
        conn.close()
    return redirect('/')

# Rota para marcar como concluído
@app.route('/concluir/<int:id>')
def concluir(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = NOT concluida WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Iniciar a aplicação
if __name__ == "__main__":
    app.run(debug=True)

import sqlite3
import random
import time
import datetime

# Criando uma conexão
conn = sqlite3.connect('dsa.db')

# Criando um cursor
c = conn.cursor()


# Função para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, ' \
              'prod_name TEXT, valor REAL)')


# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES(002, '02-05-2020', 'teclado', 130 )")
    conn.commit()
    c.close()
    conn.close()


# Usando variáveis para inserir dados
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'monitor'
    new_valor = random.randrange(50, 100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?, ?)",
              (new_date, new_prod_name, new_valor))
    conn.commit()


# Leitura de dados
def leitura_todos_dados():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)


# Leitura de registros específicos
def leitura_registros():
    c.execute("SELECT * FROM PRODUTOS WHERE valor > 60.0")
    for linha in c.fetchall():
        print(linha)

    # Leitura de colunas específicos


def leitura_colunas():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha[3])

# Select nos dados
leitura_todos_dados()
print('\n\n')
# Leitura de registros específicos
leitura_registros()
print('\n\n')
# Leitura de colunas específicas
leitura_colunas()

# Encerrando a conexão
c.close()
conn.close()
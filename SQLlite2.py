# Reemove o arquivo com o banco de dados SQLite (caso exista)

import os
import random
import time
import datetime

os.remove("dsa.db") if os.path.exists("dsa.db") else None

import sqlite3

# Abrindo conexão
conn = sqlite3.connect('dsa.db')

# Criando o cursor
c = conn.cursor()

# Função para criar uma tabela
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS produtos'\
              '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prodName TEXT, valor REAL)')

# Função para inserir uma linha
def dataInsert():
    c.execute("INSERT INTO produtos VALUES(10, '2022-20-01 19:21:00', 'Teclado', 90)")
    conn.commit()
    c.close()
    conn.close()

# Função para inserir dados usando variáveis
def dataInsertVar():
    newData = datetime.datetime.now()
    newProdName = 'Monitor'
    newValor = random.randrange(50,100)
    c.execute("INSERT INTO produtos (date,prodName, valor) VALUES (?, ?, ?)",(newData, newProdName, newValor))
    conn.commit()

# Criando a tabela
createTable()

# Inserindo os dados
#dataInsert()

for i in range(10):
    dataInsertVar()
    time.sleep(0.05)

# Seleciona todos os registros
c.execute('select * from produtos')

# Recupera os resultados
recset = c.fetchall()

# Mostra
for rec in recset:
    print ('Produto Id: %d, Date: %s, Nome: %s, Valor: %s \n' % rec)

c.close()
conn.close()
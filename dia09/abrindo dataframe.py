# %%
import pandas as pd
import sqlalchemy
import sqlite3

# %%
import sqlite3

# Conectar ao banco
conn = sqlite3.connect("../data/olist.db")
cursor = conn.cursor()

# Listar todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Exibir os nomes das tabelas
for tabela in tabelas:
    print(tabela[0])

conn.close()

import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect("../data/olist.db")  # ajuste o caminho se necessário

# Carregar a tabela tb_order_items
df_items = pd.read_sql_query("SELECT * FROM tb_order_items", conn)

# Visualizar as primeiras linhas
print(df_items.head())

# Fechar a conexão
conn.close()

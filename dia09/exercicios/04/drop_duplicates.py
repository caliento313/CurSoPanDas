# %%

# Obtenha a última linha de transacao de cada cliente
# Obtenha a primeira

import pandas as pd
#MOSTRA A PLANILHA INTEIRA
#pd.set_option('display.max_columns', None)

df = pd.read_csv("../../data/transacoes.csv",sep=';')

print(df)

# %%

#COLOCA EM ORDEM DECRECENTE E MOSTRA A ULTIMA TRANSACAO DO CLIENTE
ultima_transacao = (df.sort_values(by="DtCriacao")
                      .drop_duplicates(subset=['IdCliente'], keep='last'))
#print(ultima_transacao.sort_values(by='DtCriacao'))#239861  5f8fcbe0-6014-43f8-8b83-38cf2f4887b3  2024-01-27 11:53:23.774
print(ultima_transacao)
# %%
#COLOCA EM ORDEM DECRESCENTE E MOSTRA A PRIMEIRA TRANSACAO DO CLIENTE
primeira_transacao = (df.sort_values(by="DtCriacao")
                        .drop_duplicates(subset=['IdCliente'], keep='first'))
print(primeira_transacao)
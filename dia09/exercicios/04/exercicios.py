# %%
import pandas as pd

# %%
# 04.01 - Quantos clientes tem vínculo com a Twitch?

clientes = pd.read_csv("../../../data/clientes.csv")
clientes.head()

filtro = clientes["flTwitch"] == 1
qtde_twitch = clientes[filtro].shape[0]

print(f"Temos {qtde_twitch} usuários com twitch")

# %%
# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

clientes.head()

filtro = clientes["qtdePontos"] > 1000
qtde_1000 = clientes[filtro].shape[0]
print(f"Temos {qtde_1000} clientes com mais de 1000 pontos")

# %%
# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

transacoes = pd.read_csv("../../../data/transacoes.csv")
transacoes.head()
filtro = (transacoes['dtCriacao'] >= '2025-02-01') & (transacoes['dtCriacao'] < '2025-02-02')
qtde_dia_2025_02_01 = transacoes[filtro].shape[0]
print(f"No dia 2025-02-01 tivemos {qtde_dia_2025_02_01} transacoes")

# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

series_idades = pd.Series(idades)
series_idades
print(series_idades)

# %%
idades[0]
series_idades[0]

# %%
#series_idades[-1]

# %%
series_idades = series_idades.sort_values()
series_idades
print(series_idades)

# %%
series_idades[0]

# %%

print(series_idades.iloc[0])

# %%
series_idades.iloc[-1]

# %%

series_idades.iloc[:3]
print(series_idades.iloc[:3])#mostra o elemento da serie na posiçao do indice 3
# %%

print(series_idades.iloc[::-1])
print(series_idades.iloc[:-1])

# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

indexs = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]

series_idades = pd.Series(idades, index=indexs)
series_idades
print(series_idades)

# %%
series_idades.iloc[-1]
print(series_idades.iloc[-1])#- significa "index location", ou seja, acesso por posição.
#-1 é o índice negativo que representa o último item.

print(series_idades.iloc[::-1])#- [::-1] é uma fatiamento invertido.
#Isso retorna a Series de trás pra frente, ou seja, em ordem reversa.

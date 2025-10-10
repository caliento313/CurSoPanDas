# %%
# 06.01 - Qual a quantidade média de redes sociais dos usuários?
# E a Variância? E o máximo?

import pandas as pd

clientes = pd.read_csv("../../../data/clientes.csv")
clientes

# %%

clientes["totalRedes"] = (clientes['flEmail'] + 
                          clientes['flTwitch'] + 
                          clientes['flYouTube'] + 
                          clientes['flBlueSky'] +
                          clientes['flInstagram'])

media = clientes["totalRedes"].mean()
variancia = clientes["totalRedes"].var()
maximo = clientes["totalRedes"].max()

print("media:",media)
print("variancia:",variancia)
print("maximo:",maximo)

# %%

redes = [
    "flEmail",
    "flTwitch",
    "flYouTube",
    "flBlueSky",
    "flInstagram",
]

clientes[redes].sum(axis=1).describe()
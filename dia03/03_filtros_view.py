# %%

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=';')
print(clientes.head())

# %%

filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0["flag_1"] = 1
print(clientes_0)

# %%

A = [1,2]
B = A.copy()
#print("A:", A)
#print("B:", B)

#B.append("fodase")
#print("A:", A)
#print("B:", B)

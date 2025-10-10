# %%

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=';')
#MOSTRA A LINHA COM O MAIOR NUMEROS DE PONTOS
max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
#print(clientes[filtro])
#print(max_ponto)
#print(clientes['qtdePontos'].sort_values())
# %%

#MOSTRA OS idS COM MAIOR PONTOS
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
                      .head(5)["idCliente"] )
print(top_5)
#top5 = clientes.sort_values(by="qtdePontos", ascending=False).head(5)
print(type(top_5))

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    })

#print(brinquedo)

# %%
# ORDENA AS LINHAS POR PRIORIDADES COMO NA SEUQNCIA A ABAIXO
ordenado = brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
#print(ordenado)


# %%
# 06.04 - Quem teve mais transações de Streakproduto?

import pandas as pd
#Abri os 3 dataframes necessarios para a açao
transacoes = pd.read_csv("../data/transacoes.csv",sep=';')
#foi preciso alterar o nome das colunas pois estavam salvos diferentes no arquivo
transacoes=transacoes.rename(columns = {
    "IdTransacao":"idTransacao"})
transacoes=transacoes.rename(columns = {
    'IdCliente':'idCliente'})
#print(transacoes.head())
print(transacoes.dtypes)

# %%
transacao_produto = pd.read_csv("../data/transacao_produto.csv",sep=';')
#idProduto             object
#foi preciso alterar o nome das colunas pois estavam salvos diferentes no arquivo
transacao_produto=transacao_produto.rename(columns={
    'IdTransacao':'idTransacao','IdProduto':'idProduto'})
#foi preciso filtrar pois avia erros na tabela
transacao_produto['idProduto'] = pd.to_numeric(transacao_produto['idProduto'], errors='coerce')
#foi preciso retirar as linhas com NaN
transacao_produto = transacao_produto.dropna(subset=['idProduto'])
#foi preciso transformar colunas que eram object para int
transacao_produto['idProduto'] = transacao_produto['idProduto'].astype(int)

print(transacao_produto.head())
print(transacao_produto.dtypes)

# %%
produtos = pd.read_csv("../data/produtos.csv",sep=';')
produtos = produtos.rename(columns={
    'IdProduto':'idProduto'})
print(produtos.head())
print(produtos.dtypes)

cliente_transacao_produto = (transacoes.merge
               (transacao_produto,
                on="idTransacao",
                how="left"))
print(cliente_transacao_produto[['idTransacao', "idCliente", "idProduto"]])
df_full = (cliente_transacao_produto.merge
           (produtos,
            on=['idProduto'],
            how='left',))

#print(df_full)
#print(df_full.dtypes)
#df_full = df_full[df_full["DescNomeProduto"]=="Presença Streak"]
#df_full.groupby(by=["idCliente"]["idTransacao"]
   #    .count()
    #    .sort_values(ascending=False)
     #   .head(1))
#print(df_full)



# Filtra os produtos desejados resume a tabela em um unico produto
produtos = produtos[produtos["DescNomeProduto"]=="Presença Streak"]

# Realiza os merges e conta as transações por cliente
top_cliente = (transacoes
               .merge(transacao_produto, on="idTransacao", how="left")
               .merge(produtos, on="idProduto", how="inner")
               .groupby("idCliente")["idTransacao"]
               .count()
               .sort_values(ascending=False)
               .head(10))

# Exibe o resultado
print(top_cliente)

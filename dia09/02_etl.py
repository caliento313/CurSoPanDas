# %%
import pandas as pd
import sqlalchemy
import sqltool
from sklearn import cluster

# %%
with open("etl.sql") as open_file:
    query = open_file.read()

print(query)
import sqlite3
import pandas as pd
#Abre uma data frame atraves da query
conn = sqlite3.connect("../data/olist.db")

query = "SELECT * FROM tb_order_items"
df = pd.read_sql_query(query, conn)

print(df.head())
#cria uma nova coluna somando duas ja existentes

df["preco_total"] = df["price"] + df["freight_value"]
print(df)
#Para salvar a tabela modificada no dataframe original
df.to_sql( "tb_order_items",con=conn,index=False,if_exists='replace')#quando a tabela é add
# dados novos ele substituim
conn.close()

# %%
#engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")
#df = pd.read_sql_query(query, con=engine)
#print(df)

# %%
## Treina modelo de cluster
#kmean = cluster.KMeans(n_clusters=4)
#kmean.fit(df[['totalRevenue','qtSalles']])

#df["cluster"] =  kmean.labels_
#print(df)

# %%
#df.to_sql( "sellers_cluster",con=conn,index=False,if_exists="replace",)

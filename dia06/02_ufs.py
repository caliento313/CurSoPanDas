import pandas as pd
import html5lib
import requests
#IMPORTA UMA TABELA DA INTERNET
url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
headers = {
    "User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
dfs = pd.read_html(response.text)
uf = dfs[1]
print(uf)
print(uf.dtypes)
#FUNCAO PARA TRANSFORMAR DADOS DE STR EM FLOAT E TIRAR ESPAÇOS E SUBSTITUIR , POR . .
def str_to_float(x:str):
    x = (x.replace(" ", "")
         .replace(",", ".")
         .replace("\xa0", "")
            )
    return float(x)
#print(uf)
#APLICAÇAO DA FUNÇAO NOS DADOS DA TABNELA
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

#print(uf["População (Censo 2022)"])
#print(uf)
#FUNÇAO PARA RETITRAR STR ANOS DA COLUNA DE EXPECTATIVA DE VIDA
def exp_to_anos(exp:str):
    return float(exp.replace(",", ".")
                    .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)
#print(uf)
# FUNÇAO PARA CRIAR UMA NOVA COLUNA CHAMADA REGIAO E RELACIONAR DADOS JA EXISTENTES
def uf_to_regiao(uf):

     if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
         return "Centro-Oeste"
     elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
         return "Nordeste"
     elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
         return "Norte"
     elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
         return "Sudeste"
     elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
         return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
#print(uf)
#PADRONIZANDO A MORTALIDADE RETIRANDO O CARACTER ESPECIAL ‰ E MUDANDO O NOME DA COLUNA
def mortalidade_to_float(x:str):
    x = float(x.replace("‰", "")
              .replace(",", "."))
    return x
uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
#print(uf)

#FUNÇAO QUE FAZ A COMPARAÇAO DE LINHA POR LINHA DAS COLUNAS EM TRUE OR FALSE
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and
            linha["IDH (2010)"] > 700)
uf2 = uf.apply(classifica_bom, axis=1)
print(uf)
print(uf.dtypes)
#print(uf2)
uf.to_csv("tabela_1.csv", index=False, encoding="utf-8")

#uf.apply(lambda x: x["PIB per capita (R$) (2015)"], axis=1)
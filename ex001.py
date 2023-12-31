import pandas as pd
from twilio.rest import Client
from decouple import config

account_sid = config("account_sid")
auth_token = config("auth_token")

client = Client(account_sid, auth_token)


# Passo a passo de solucão
#Abrir os 6 arquivos em excel.
lista_meses =['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    #print (mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0] 
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0] 
        print (f'no mes {mes} encontou alguem com mais de 55000: {vendedor}, vendas: {vendas}')
        message = client.messages.create(
            to= config("to"),
            from_= "+18782010411",
            body=f"no mes {mes} encontou alguem com mais de 55000: {vendedor}, vendas: {vendas}")
        print(message.sid)



# Para cada arqruivo:
# verifcar se algum valor na coluna daquele arquivo e maior que 55.000;
# se for maior do que 55.000 -> enviar SMS com nome, mes e as vendas do vededor;
# caso  contrário faz nada;
    


import pandas as pd

#Dados de exemplo
data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'Idade': [25, 30, 22, 28],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']}

# Criando um DataFrame
df = pd.DataFrame(data)

# Exibindo o DataFrame
print(df)
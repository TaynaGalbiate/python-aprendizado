import pandas as pd

df= pd.read_csv('carros.csv')
print("\nTABELA:\n", df.head())              #Mostrando as 5 primeiras

proporcao = df ['População do Estado']/df['Carros por habitante']
print ("\nPROPORÇÃO:\n",proporcao)           #Mostrando a proporção da populçao do Estado e os 

verificar = df.sort_values('Quant Carros', ascending=False) 
print ("\nMAIOR QUANT. DE CARROS: \n",verificar)         #Mostrando a maior quantidade de carros

df_estado_hab = df[['Estado','Carros por habitante']]
print ("\nESTADO E CARROS POR HABITANTES:\n",df_estado_hab)         #Tabela com duas colunas dos estados e carros por habitantes
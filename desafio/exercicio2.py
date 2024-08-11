#Exercício 2:

#Qual é a média, a moda e a mediana de horas de sono para cada uma das profissões? [‘mean’, np.median, pd.Series.mod]


#Importando a biblioteca e abrindo o arquivo
import pandas as pd 
import numpy as np                                
df=pd.read_csv("saude-do-sono.csv") 


#Agrupando por profissão
grouped = df.groupby('Ocupação')['Duração do sono']

# Calculando a média
media = grouped.mean()         

# Calculando a mediana
mediana = grouped.median()

# Calculando a moda
moda = grouped.apply(lambda x: x.mode()[0] if not x.mode().empty else np.nan)            #x.mode calcula a moda, if not verifica se não está vazio para chamar o else.

# Exibindo os resultados
print("\nMÉDIA DAS HORAS DE SONO POR PROFISSÃO:\n",media)

print("\nMEDIANA DAS HORAS DE SONO POR PROFISSÃO\n",mediana)

print("\nMODA DAS HORAS DE SONO POR PROFISSÃO:\n",moda)




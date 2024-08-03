import pandas as pd

df_concurso = pd.read_csv('concurso.csv')
print("\n",df_concurso.head())  #Mostando a tabela


grupo = df_concurso[["Estado","Número de Inscrição"]].groupby("Estado").count()
print("\n",grupo)     #Mostrando tabela apenas com o estado e o número de inscrição


df=df_concurso["Deficiência"].value_counts(normalize=True)*100
print("\n",df)       #Mostrando a quantidade de pessoas com deficiência


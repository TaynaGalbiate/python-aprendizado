#Exercício 6:
#Faça um subconjunto com as colunas Identificador, Gênero, Idade, Pressão sanguínea e Frequência cardíaca.


#Importando a biblioteca e abrindo o arquivo
import pandas as pd                              
df=pd.read_csv("saude-do-sono.csv") 

#Criando um subconjunto com as colunas desejadas
colunas = ['ID', 'Gênero', 'Idade', 'Pressão sanguíneaaaa', 'Frequência cardíaca']       #Nome das colunas desejadas
subconjunto_df = df[colunas]                                         #Dentro de subconjunto_df tem o data frame e as colunas desejadas

print("\nSUBCONJUNTO:\n",subconjunto_df)                             #Mostra na tela o subconjunto
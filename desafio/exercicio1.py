#Exercício 1:
#Ao visualizar a base você percebeu que seria melhor alterar o nome de algumas colunas. 
# Mude o ‘ID’ para ‘Identificador’, corrija o nome da coluna que indica a pressão sanguínea, 
# mude a coluna ‘Ocupação’ para ‘Profissão’, a coluna ‘Categoria BMI’ está em parte em inglês, substitua para ‘Categoria IMC’.


#Importando a biblioteca e abrindo o arquivo
import pandas as pd                                 
df=pd.read_csv("saude-do-sono.csv")                  

#Exibindo o DataFrame original
print("\nORIGINAL:\n")
print(df)

#Renomeando as colunas
df.rename(columns={
    'ID': 'Identificador',
    'Pressão sanguíneaaaa': 'Pressão Sanguínea',
    'Ocupação': 'Profissão',
    'Categoria BMI': 'Categoria IMC'
}, inplace=True)                       #inplace=True (as alterações são feitas diretamente no df existente, sem precisar criar uma cópia nova.)

#Exibindo as alterações
print("\nALTERAÇÕES REALIZADAS:\n")
print(df)


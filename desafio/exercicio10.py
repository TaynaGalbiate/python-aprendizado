#Exercício 10:
#Pessoas com frequências cardíacas acima de 70 dão mais passos que pessoas com frequência cardíaca menor ou igual a 70? (Use a média)


#Importando a biblioteca e abrindo o arquivo
import pandas as pd                     
df=pd.read_csv("saude-do-sono.csv") 


#Verifica se as colunas necessárias estão presentes
if 'Frequência cardíaca' in df.columns and 'Passos diários' in df.columns:
    
    #Separa os dados em dois grupos com base na frequência cardíaca
    grupo_70 = df[df['Frequência cardíaca'] > 70]
    grupo_70_menor = df[df['Frequência cardíaca'] <= 70]
    
    #Calcula a média de passos para cada grupo
    passos_70 = grupo_70['Passos diários'].mean()
    passos_70_menor = grupo_70_menor['Passos diários'].mean()
    
    #Compara as médias e imprimi o resultado
    if passos_70 > passos_70_menor:
        print("Pessoas com frequências cardíacas acima de 70, dão mais passos do que pessoas com frequência cardíaca menor/igual a 70.")
    else:
        print("Pessoas com frequências cardíacas acima de 70, não dão mais passos do que pessoas com frequência cardíaca menor/igual a 70.")
else:
    print("Não foi encontrado.")

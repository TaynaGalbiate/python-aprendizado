#Exercício 9:

#É predominante entre os participantes dormir 8 horas por dia (considere usar Moda como medida)?

#Importando a biblioteca e abrindo o arquivo
import pandas as pd                     
df=pd.read_csv("saude-do-sono.csv") 


if 'Duração do sono' in df.columns:                          #Verifica se a coluna 'Duração do sono' está presente no df, se a coluna existir, o bloco de código é executado.
        moda = df['Duração do sono'].mode()                  #Calculando a moda das horas de sono com
       
        if 8 in moda.values:                                  #Verificando se 8 horas está entre as modas, caso não tenha o else fará as próximas observações
            print("É predominante entre os participantes dormir 8 horas por dia.")
        else:
            print("Não é predominante entre os participantes dormir 8 horas por dia.")
else:
        print("Não foi encontrada.")

        

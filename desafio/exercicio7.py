#Exercício 7:

#Descubra qual a profissão menos frequente no conjunto. (Use value_counts)



#Importando a biblioteca e abrindo o arquivo
import pandas as pd                             
df=pd.read_csv("saude-do-sono.csv") 

#Contando a frequência de cada profissão
contagem_profissoes = df['Ocupação'].value_counts()         #.value_counts conta a frequência de valores únicos em uma série

#Encontrando a profissão menos frequente
profissao_menos = contagem_profissoes.idxmin()              #.idxmin() e min() para encontrar a menos frequente
frequencia_menos = contagem_profissoes.min()

#Exibindo o resultado
print(f"\nA profissão menos frequente é: {profissao_menos}, com {frequencia_menos} ocorrência(s).\n")
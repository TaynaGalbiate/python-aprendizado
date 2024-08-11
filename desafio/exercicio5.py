#Exercício 5:

#Entre quem fez enfermagem e quem fez medicina, quem tem menos horas de sono? (Use o método ‘isin’, considere a média)

#Importando a biblioteca e abrindo o arquivo
import pandas as pd                              
df=pd.read_csv("saude-do-sono.csv") 

#Filtrando os dados enfermeiros e médicos
profissoes = ['Enfermeiro(a)', 'Médico(a)']
filtrado_df = df[df['Ocupação'].isin(profissoes)]
print("\nTABELA:\n",filtrado_df)

#Calculando a média de horas de sono
media_sono = filtrado_df.groupby('Ocupação')['Duração do sono'].mean()

#Exibi a média de horas de sono e compara
print("\nMÉDIA DE HORAS DE SONO DOS ENFERMEIROS E MÉDICOS:\n",media_sono)


#Identificando qual profissão tem menos horas de sono
profissao_sono = media_sono.idxmin()                 #.idmin() retorna o menor valor dentro de uma série
menor_media_sono = media_sono.min()                        #.min() encontra o menor valor dentro do conjunto

print("\nPROFISSIONAL COM MENOS HORAS DE SONO:\n",profissao_sono)
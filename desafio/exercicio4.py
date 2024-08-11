#Exercício 4:

#De acordo com os dados, advogar ou ser representante de vendas faz você dormir menos? (Use o método ‘isin’, considere a média)

#Importando a biblioteca e abrindo o arquivo
import pandas as pd                              
df=pd.read_csv("saude-do-sono.csv") 


#Filtrando os dados para 'Advogado' e 'Representante de Vendas'
profissoes = ['Advogado(a)', 'Representante de Vendas']                        
filtrado_df = df[df['Ocupação'].isin(profissoes)]                           #isin filtra apenas as linhas onde a coluna profissão é igual a advogado ou representante de vendas.
print ("\nTABELA:\n" , filtrado_df)


#Calculando a média de horas de sono para as profissões filtradas
media_sono = filtrado_df.groupby('Ocupação')['Duração do sono'].mean()

#Exibi a média de horas de sono para as profissões
print("\nMÉDIA DE SONO:\n",media_sono)

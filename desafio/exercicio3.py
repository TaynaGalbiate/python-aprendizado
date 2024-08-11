#Exercício 3:
#Das pessoas que atuam com engenharia de software qual a porcentagem de obesos?


#Importando a biblioteca e abrindo o arquivo
import pandas as pd                              
df=pd.read_csv("saude-do-sono.csv") 

engenharia_df = df[df['Ocupação'] == 'Eng. de Software']                 #filtrar nas profissões apenas os engenheiros de software

#Selecionando apenas as colunas profissão e categoria bmi
engenharia_qualidade_df = engenharia_df[['Ocupação', 'Categoria BMI']]         
print("\nTABELA:\n",engenharia_qualidade_df)


#Contando o total de pessoas em engenharia de software e o número de pessoas obesas
total_engenharia = engenharia_df.shape[0]                                           #.shape[0] retorna o tato encontrado
total_obesos = engenharia_df[engenharia_df['Categoria BMI'] == 'Obesidade'].shape[0]

#Calcular a porcentagem de obesos
percentual_obesos = (total_obesos / total_engenharia) * 100

#Exibindo o resultado
print(f"\nPORCERTAGEM DE OBESOS ENTRE ENGENHEIROS:\n {percentual_obesos:.2f}%")
#Exercício 8:

#Quem tem maior pressão sanguínea média, homens ou mulheres? (Considere a média)

#Importando a biblioteca e abrindo o arquivo
import pandas as pd                     
df=pd.read_csv("saude-do-sono.csv") 



#Convertendo a string de pressão arterial em valores numéricos
def convert(pressao):
    try:
        sist, dias = pressao.split('/')
        return float(sist), float(dias)          #Convertendo para o tipo float
    except ValueError:
        return None, None                       #Se a conversão falhar retorna None, None

#Aplica a função à coluna e cria duas novas colunas para sistólica e diastólica
df[['Pressão Sistólica', 'Pressão Diastólica']] = df['Pressão sanguíneaaaa'].apply(lambda x: pd.Series(convert(x)))     #Esta é uma função lambda recebe um valor x da coluna 'Pressão sanguíneaaaa', chama convert e passa o resultado para pd.Series, que cria uma nova Series a partir da tupla (sistólica, diastólica).

#Agrupando os dados pelo gênero e calculando a média usando o .mean
media_sistolica = df.groupby('Gênero')['Pressão Sistólica'].mean()            
media_diastolica = df.groupby('Gênero')['Pressão Diastólica'].mean()          

# Calcula a média geral para cada gênero (média das médias sistólica e diastólica)
media_total = pd.DataFrame({
    'Média Sistólica': media_sistolica,
    'Média Diastólica': media_diastolica
})
media_total['Média Geral'] = (media_total['Média Sistólica'] + media_total['Média Diastólica']) / 2         #Cálculo para saber a média geral


#Resultados
print("\nMÉDIA GERAL DE PRESSÃO POR GÊNERO:\n")
print(media_total)

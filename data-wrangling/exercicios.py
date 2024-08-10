import pandas as pd
df=pd.read_csv("collected.csv")
print(df)

df=df.drop(columns=['Unnamed: 0'])
print(df.head())  #Removendo uma coluna desnecessária



novas_cols ={'Endereerço': 'Endereço'}
df.rename(columns=novas_cols, inplace=True)  #Alterando o nome da coluna
print (df.head())


df['Nome']= df['Nome'].str.replace(r'[^a-zA-Z0-9\sà-úÀ-Ú]', '', regex=True)     #Removendo os caracteres dos nomes
print(df.head())


              

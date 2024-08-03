#Criando jogadores

import pandas as pd

jogadores_data ={"Jogador": ["João", "Caio","Bruno"],
                 "Ano": [2022,2023,2024],
                 "Pontuação":[95, 97, 99]}

df = pd.DataFrame(jogadores_data)
print("\nGRUPO DE JOGADORES\n",df)

grupo = df.groupby('Jogador')

for jogador, group in grupo:
 print("\nJOGADOR:")
 print("----- {} -----".format(jogador))
 print(group)
 print("")

pontuacao = df.loc[df.Pontuação > 97]
print("\nPONTUAÇÃO ACIMA DE 96:\n", pontuacao)
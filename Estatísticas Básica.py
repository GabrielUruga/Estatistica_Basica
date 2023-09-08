import os
from numpy import loadtxt, mean, add, sum
import pandas as pd

# abrindo arquivo CSV no projeto
arq = os.path.join('Personal Projects/LinkedIn/Análise Estatística/notas.csv')

# Transformando os valores em um array 1D
arrn1, arrn2 = loadtxt(arq, 
                       delimiter=',', 
                       usecols=(1,2), 
                       skiprows=1,
                       unpack=True)

# calculando Média
media_1b = mean(arrn1)
media_2b = mean(arrn2)

# somando as notas dos arrays
notas_totais = add(arrn1, arrn2)

# calculando média semestral
media_semestre = mean(notas_totais)/2

# Calculando Médias de cada index do array com Notas Totais
medias_notas_totais = (notas_totais/2)

# inserindo os arrays e a média no dataframe 
tabela_notas = pd.DataFrame(data={'N1':arrn1,                           
                                  'N2':arrn2,
                                  ' ':' ',
                                  'MÉDIA':medias_notas_totais,
                                  '  ':'  '
                                  })
'''
Foi usado Dicionário para colocar uma estrutura key:value, em que:
- key = nome da coluna
- value = linha(s) da coluna
'''

# ordenando a coluna Média em crescente
tabela_notas.sort_values(['MÉDIA'],ascending=True, inplace=True, ignore_index=True)

# imprimindo a tabela
print(f'NOTAS:\n\n{tabela_notas}')
print(end='\n')

# Exportando o DataFrame para CSV
tabela_notas.to_csv('Personal Projects/LinkedIn/Análise Estatística/Tabela_Notas.csv', index = False)
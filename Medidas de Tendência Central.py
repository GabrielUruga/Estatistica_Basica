from pandas import read_csv, DataFrame, set_option
from statistics import mode, mean, median, stdev

# lendo CSV
try:
  dados = read_csv('Personal Projects/LinkedIn/Análise Estatística/Tabela_Notas.csv')
except:
  print('Não foi possível encontrar este arquivo')

# criando DataFrame com dados do CSV
notas = DataFrame(dados)

# criando objetos para colunas
n1 = notas['N1']
n2 = notas['N2']
semestre = notas['MÉDIA']

# criando DataFrame com medidas encontradas
tabela = DataFrame(data={ 
                                'MÉDIA':[mean(n1),mean(n2),mean(semestre)],
                                'DESVIO PADRÃO':[stdev(n1), stdev(n2), stdev(semestre)],
                                'MODA':[mode(n1), mode(n2), mode(semestre)],
                                'MEDIANA':[median(n1), median(n2), median(semestre)]
                                  }, 
                                  index  = ['N1', 'N2', 'Semestre'])
# Formatação de Casas Decimais do DataFrame
set_option('float_format', '{:.2f}'.format)

# Imprimindo DataFrame com Medidas de Tendência Central
print(f'Medidas de Tendência Central:\n\n{tabela}\n')
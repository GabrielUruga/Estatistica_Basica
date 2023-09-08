from pandas import read_csv, set_option

try: 
    df = read_csv('Personal Projects/LinkedIn/Análise Estatística/Tabela_Notas.csv')
except:
    print('Não foi possível ler o arquivo')

# Formatação de casas decimais
set_option('float_format', '{:.2f}'.format)

# Resumo Estatístico
print(f'RESUMO ESTATÍSTICO:\n\n{df.describe()}\n')
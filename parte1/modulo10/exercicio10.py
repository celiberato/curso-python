
def log(msg, quebra=False):
  if quebra:
    print('*****************************************************')
  print(msg)

  
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/develop/dataset/credito.csv', na_values='na');
df.head(n=10)

log('---------------- EXPLORAÇÃO DADOS: DESCOBRIR POR QUE UM CLIENTE É INADIMPLENTE (SALÁRIO / ESCOLARIDADE / ETC) -----------------', True)
log('Entender a variável DEFAULT (0=adimplente, 1=inadimplente, ou seja,', True)
log('queremos entender o porque um cliente deixa de honrar com suas dívidas baseado no comportamento de outros atributos,', False)
log('como salário, escolaridade e movimentação financeira', False)

log(df, True)

df.shape

log('DEFAULT: VARIÁVEL RESPOSTA', True)
log('IDADE, SALARIO, ETC: VARIÁVEIS EXPLICATIVAS', False)
df[df['default']==0].shape
df[df['default']==1].shape

qtd_total = df.shape[0];

qtd_adimplentes = df[df['default']==0].shape[0]
qtd_inadimplentes = df[df['default']==1].shape[0]

perc_qtd_adimplentes = round(qtd_adimplentes / qtd_total * 100, 2)
perc_qtd_inadimplentes = round(qtd_inadimplentes / qtd_total * 100, 2)

log(f'total: {qtd_total}', True);
log(f'adimplentes: {qtd_adimplentes}', False);
log(f'inadimplentes: {qtd_inadimplentes}', False);

log(f'(%) adimplentes: {perc_qtd_adimplentes}', False);
log(f'(%) inadimplentes: {perc_qtd_inadimplentes}', False);


log('ATRIBUTOS CATEGORICOS', True)
log(df.select_dtypes('object').describe().transpose(), False)
log('ATRIBUTOS NUMERICOS', True)
log(df.drop('id', axis=1).select_dtypes('number').describe().transpose(), False)

log('DADOS FALTANTES', True)
log(df.head(), False)
log(df.isna().any(), False)


def stats_dados_faltantes(df: pd.DataFrame) -> None:
	stats_dados_faltantes = [];
	for col in df.colunas:
		if df[col].isna().any():
			qtde, _ = df[df['col'].isna()].shape
			total, _ = df.shape
			dict_dados_faltantes = {col: {'quantidade': qtd, 'porcentagem': round(100 * qtd/total, 2)}}
			stats_dados_faltantes.append(dict_dados_faltantes)

	for stat in stats_dados_faltantes:
		log(stat, True)

log('---------------- TRANSFORMAÇÃO E LIMPEZA DE DADOS: CORRIGIR TIPOS DE DADOS / REMOVER DADOS FALTANTES -----------------', True)

df[['limite_credito', 'valor_transacoes_12m']].dtypes
df[['limite_credito', 'valor_transacoes_12m']].head(n=5)

fn =lambda valor: float(valor.replace('.', '').replace(',', '.'))

valores_originais = ['12.691,51', '8.256,96', '3.418,56']
valores_limpos = list(map(fn, valores_originais))

log('VALORES ORIGINAIS', True)
log(valores_originais, False)
log('VALORES LIMPOS', True)
log(valores_limpos, False)

df['valor_transacoes_12m'] =  df['valor_transacoes_12m'].apply(fn)
df['limite_credito'] =  df['limite_credito'].apply(fn)

df.dtypes
df.select_dtypes('object').describe().transpose()

df.drop('id', axis=1).select_dtypes('number').describe().transpose()

df.dropna(inplace=True)

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

qtd_total_novo, _ = df.shape
qtd_adimplentes_novo, _ = df[df['default'] == 0].shape
qtd_inadimplentes_novo, _ = df[df['default'] == 1].shape

perc_qtd_adimplentes_novo = round(qtd_adimplentes_novo / qtd_total_novo * 100, 2)
perc_qtd_inadimplentes_novo = round(qtd_inadimplentes_novo / qtd_total_novo * 100, 2)

log(f'total (NOVO): {qtd_total_novo}', True);
log(f'adimplentes (NOVO): {qtd_adimplentes_novo}', False);
log(f'inadimplentes (NOVO): {qtd_inadimplentes_novo}', False);

log(f'(%) adimplentes (NOVO): {perc_qtd_adimplentes_novo}', False);
log(f'(%) inadimplentes (NOVO): {perc_qtd_inadimplentes_novo}', False);


log('---------------- VISUALIZAÇÃO DE DADOS: ENTENDER QUE FATOR LEVA UM CLIENTE A INADIMPLÊNCIA -----------------', True)

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')

df_adimplente = df[df['default']==0]
df_inadimplente = df[df['default']==1]


log(df.select_dtypes('object').head(n=5))

coluna = 'escolaridade'
titulos = ['Escolaridade dos clientes', 'Escolaridade dos clientes adimplentes', 'Escolaridade dos clientes inadimplentes']

eixo = 0;
max_y = 0;
max = df.select_dtypes('object').describe()[coluna]['freq'] * 1.1;
figura, eixos = plt.subplots(1,3, figsize=(20, 5), sharex=True);

for dataframe in [df, df_adimplente, df_inadimplente]:
	df_to_plot = dataframe[coluna].value_counts().to_frame()
	df_to_plot.rename(columns={coluna: 'frequência absoluta'}, inplace=True)
	df_to_plot[coluna] =  df_to_plot.index
	df_to_plot.sort_values(by=[coluna], inplace=True)
	df_to_plot.sort_values(by=[coluna])

	f = sns.barplot(x=df_to_plot[coluna], y=df_to_plot['frequência absoluta'], ax=eixos[eixo])
	f.set(title=titulos[eixo], xlabel=coluna.capitalize(), ylabel = "frequência absoluta")
	f.set_xticklabels(labels=f.get_xticklabels(), rotation=90)
	_, max_y_f = f.get_ylim()
	max_y = max_y_f if max_y_f>max_y else max_y
	f.set(ylim=(0, max_y))
	eixo+= 1

figura.show()
figura.savefig('grafico.png')
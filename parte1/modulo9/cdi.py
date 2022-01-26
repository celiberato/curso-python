import os
import requests as req
import json
from datetime import datetime;

# criando a variavel data e hora
data_e_hora = datetime.now();
data = datetime.strftime(data_e_hora, '%y/%m/%d')
hora = datetime.strftime(data_e_hora, '%H/%M/%S')


# captando a taxa CDI do site na b3
try:
	response = req.get('https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx');
	response.raise_for_status()
except request.HTTPError as exc:
	print('Dado não encontrado, continuando.');
	cdi = None;
except Exception as exc:
	print('Erro, parando a execução');
	raise exc;
else:
	dados = json.loads(response.text)
	cdi = float(dados['taxa'].replace(',', '.'))

# verificando se o arquivo 'taxa-cdi.csv' existe
if os.path.exists('./taxa-cdi.csv') == False:

	with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
		fp.write('data,hora,taxa\n');

# salvando dados no arquivo 'taxa-cdi.csv'		

with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
	fp.write (f'{data},{hora},{cdi}\n');

print('Sucesso');
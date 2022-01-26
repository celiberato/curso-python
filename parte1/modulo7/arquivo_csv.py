class ArquivoBase(object):
	def __init__(self, arquivo: str, tipo_arquivo: str):
		self.arquivo = arquivo;
		self.tipo_arquivo = tipo_arquivo;
		self.conteudo = self._extrair_conteudo();

	def _extrair_conteudo(self):
		with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
			conteudo = arquivo.readlines();
		return conteudo;

class ArquivoCSV(ArquivoBase):
	def __init__(self, arquivo: str, tipo_arquivo: str):
		super().__init__(arquivo = arquivo, tipo_arquivo = tipo_arquivo);
		self.colunas = self._extrair_nome_colunas();


	def _extrair_nome_colunas(self):
		return self.conteudo[0].strip().split(sep=',');

	def _extrair_coluna(self, indice_coluna: str):
		coluna = list();
		for linha in self.conteudo:
			conteudo_linha =- linha.strip().split(sep=',');
			coluna.append(conbteudo.linha[indice_coluna]);
		coluna.pop(0);
		return coluna;		

class ArquivoTXT(ArquivoBase):
	def __init__(self, arquivo: str, tipo_arquivo: str):
		super().__init__(arquivo = arquivo, tipo_arquivo = tipo_arquivo);

---------------------

from arquivo_csv import ArquivoCSV ;

csv = ArquivoCSV('./banco.csv', 'CSV')

print(csv.conteudo)		
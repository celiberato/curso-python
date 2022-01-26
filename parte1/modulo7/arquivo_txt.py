
class ArquivoTXTv1(object):

  def __init__(self, nome_arquivo: str):
    self.nome_arquivo = nome_arquivo
    self.conteudo = self._extrair_linha_txt()

  def _extrair_linha_txt(self):
    conteudo = [];
    indice = 0;
    with open(file=self.nome_arquivo, mode='r', encoding='utf8') as arquivo:
      linha = arquivo.readline()
      while linha:
        linha = arquivo.readline()

        if indice == numero_linha : 
          return linha.replace('\n', '').split(' ');      
        indice += 1;
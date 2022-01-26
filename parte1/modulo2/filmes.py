filmes = ['Um Sonho de Liberdade', 
			'O Poderoso Chefão 2', 
			'Batman: O Cavaleiro das Trevas', 
			'12 Homens e uma Sentença', 
			'A Lista de Schindler', 
			'O Senhor dos Anéis: O Retorno do Rei',
			'Pulp Fiction: Tempo de Violência', 
			'A Lista de Schindler', 
			'O Senhor dos Anéis: O Retorno do Rei',
			'Pulp Fiction: Tempo de Violência', 
			'Três Homens em Conflito', 
			'O Senhor dos Anéis: A Sociedade do Anel']

print(filmes)

primeiro_filme = filmes[0]
segundo_filme = filmes[1]

filmes.pop(0)
filmes.pop(0)

filmes.insert(0, primeiro_filme)
filmes.insert(0, segundo_filme)

print(filmes)

-----------------------------------

filmes = ['Um Sonho de Liberdade', 
			'O Poderoso Chefão 2', 
			'Batman: O Cavaleiro das Trevas', 
			'12 Homens e uma Sentença', 
			'A Lista de Schindler', 
			'O Senhor dos Anéis: O Retorno do Rei',
			'Pulp Fiction: Tempo de Violência', 
			'A Lista de Schindler', 
			'O Senhor dos Anéis: O Retorno do Rei',
			'Pulp Fiction: Tempo de Violência', 
			'Três Homens em Conflito', 
			'O Senhor dos Anéis: A Sociedade do Anel']

print(filmes)

unicos = list(set(filmes))
print(unicos)

---------------------------------------------------
dic_filme = [{'nome': 'Um Sonho de Liberdade', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'O Poderoso Chefão 2', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'Batman: O Cavaleiro das Trevas', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': '12 Homens e uma Sentença', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'A Lista de Schindler', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'O Senhor dos Anéis: O Retorno do Rei', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'Pulp Fiction: Tempo de Violência', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'A Lista de Schindler', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'Três Homens em Conflito', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'},
{'nome': 'O Senhor dos Anéis: A Sociedade do Anel', 'ano': 1900, 'sinopse': 'xxxxxxxxxxxxx'}
]

print(dic_filme)
print(dic_filme[1]['nome'])
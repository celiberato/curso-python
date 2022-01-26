idade = 30
print(idade)

idade += 5
print(idade)

idade -= 10
print(idade)

print(type(idade))

juros = 0.5
print(juros)

print(type(juros))


nome = 'Fulano'
sobrenome = 'de Tal'
nome_completo = f'Meu nome é {nome} {sobrenome}'

print(nome_completo)
print(type(nome_completo))

posicao_fulano = nome_completo.find("Fulano")
posicao_de_tal = nome_completo.find("de Tal")
print(nome_completo[posicao_fulano: posicao_de_tal])
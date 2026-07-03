import os
'''
Exercícios
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.

3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

**************************************************************************
Resolução
**************************************************************************

1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.

pessoa = {'nome' : 'Guilherme', 'idade' : 28, 'cidade' : 'Brasília'}

pessoa['profissao'] = 'Engenheiro de Software'
pessoa['idade'] = 31
del pessoa['cidade']

print(pessoa)
os.system('cls')
print(pessoa)

3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

items() → Retorna pares chave-valor
clear() → Limpa o dicionário
update() → Atualiza ou mescla com outro dicionário
pop() → Remove e retorna o valor de uma chave específica
popitem() → Remove o último par inserido
copy() → Cria uma cópia superficial do dicionário
get() → Retorna o valor de uma chave sem gerar erro, podendo definir valor padrão


square_numbers = {x: x**2 for x in range(1,6)}
print(square_numbers)
os.system('cls')
print(square_numbers)

4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
'''
frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

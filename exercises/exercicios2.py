"""
print('1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.')

numero = int(input('Insira um número:'))

if numero % 2 == 0:
    print('Par')
else :
    print('Ímpar')


print('''2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:
Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.\n
''')


idade = int(input('Qual sua idade? '))

if 0<= idade <=12:
    print('Crianca')
elif 13<= idade <=18:
    print('Adolescente')
elif  idade > 18:
    print('Adulto')
else:
    print('Valor inválido!')


print('3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.')

usuario_correto = 'dida'
senha_correta = '123'

usuario = input('Qual o seu usuário?')
senha = input('Qual a sua senha?')

if usuario_correto == usuario and senha_correta == senha:
    print('Usuárioe e senha válidas.')
else :
    print('Usuário ou senha inválida')

"""

print("""

4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.

""")

x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if x > 0 and y > 0 :
    print('Primeiro Quadrante')
elif x < 0 and y > 0 :
    print('Segundo Quadrante')
elif x < 0 and y < 0 :
    print('Terceiro Quadrante')
elif x > 0 and y < 0 :
    print('Quarto Quadrante')
else:
    print('O ponto está localizado no eixo ou origem.')

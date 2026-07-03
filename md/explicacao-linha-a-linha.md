# Explicação Linha a Linha — `app.py`

Documentação detalhada do sistema de cadastro de restaurantes (CLI), explicando o que cada linha/trecho do código faz.

---

## Importações e dados iniciais

```python
import os
```
Importa o módulo `os`, usado mais adiante para limpar a tela do terminal (`os.system('cls')`).

```python
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]
```
Cria a variável global `restaurantes`, uma **lista de dicionários**. Cada dicionário representa um restaurante com três chaves: `nome` (string), `categoria` (string) e `ativo` (booleano, indicando se o restaurante está ativado ou não). Essa lista já vem populada com 3 restaurantes de exemplo e será usada (lida e modificada) por todas as outras funções do programa.

---

## `exibir_nome_do_programa()`

```python
def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""...""")
```
Define uma função sem parâmetros. A docstring (texto entre `'''`) documenta o propósito da função. Dentro dela, um único `print()` com uma string multi-linha (delimitada por `"""`) exibe o logo em ASCII art "CADASTRO DE RESTAURANTES". Por ser uma string literal, o texto é exibido exatamente como escrito, preservando quebras de linha.

---

## `exibir_opcoes()`

```python
def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')
```
Mostra o menu de opções numeradas. Cada `print` imprime uma linha. O `\n` no final da última linha adiciona uma linha em branco extra após o menu, separando visualmente o menu do próximo `input()`.

---

## `finalizar_app()`

```python
def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizar app')
```
Chama `exibir_subtitulo()` passando o texto `'Finalizar app'`. Isso limpa a tela e mostra um cabeçalho estilizado avisando que o programa está sendo encerrado. **Observação:** essa função não chama `voltar_ao_menu_principal()` nem encerra o processo (não há `exit()` ou `return` explícito de saída) — na prática, ao terminar, o programa simplesmente chega ao fim da execução da função e o script encerra naturalmente, pois nada mais é chamado depois dela.

---

## `voltar_ao_menu_principal()`

```python
def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal

    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()
```
- `input('\nDigite uma tecla para voltar ao menu ')`: pausa a execução esperando o usuário digitar algo e pressionar Enter. O valor digitado não é armazenado (não há `variavel =` antes do `input`), serve só para "segurar" a tela.
- `main()`: chama novamente a função principal, reiniciando o fluxo do programa (limpa tela, mostra logo, menu e pede nova opção). Isso cria um laço de repetição por **recursão** (a função chama a si mesma indiretamente através do fluxo do programa).

---

## `opcao_invalida()`

```python
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal

    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
```
Imprime uma mensagem de erro e, em seguida, chama `voltar_ao_menu_principal()` para reiniciar o ciclo do menu.

---

## `exibir_subtitulo(texto)`

```python
def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela

    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
```
- `def exibir_subtitulo(texto):` — função que recebe um parâmetro `texto` (string).
- `os.system('cls')` — executa o comando de sistema `cls`, que limpa o terminal no **Windows**. (Em Linux/Mac o comando equivalente seria `clear`; por isso essa linha só funciona como esperado em Windows.)
- `linha = '*' * (len(texto))` — cria uma string de asteriscos (`*`) com o mesmo comprimento do texto recebido, usando `len()` para contar os caracteres e o operador `*` para repetir o caractere `'*'` essa quantidade de vezes.
- `print(linha)` — imprime a linha de asteriscos (borda superior).
- `print(texto)` — imprime o texto do subtítulo.
- `print(linha)` — imprime a linha de asteriscos novamente (borda inferior), formando uma "moldura" ao redor do texto.
- `print()` — imprime uma linha em branco para espaçamento.

---

## `cadastrar_novo_restaurante()`

```python
def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    ...
    '''
    '''Essa função é responsavel por cadastrar um novo restaurante
    ...
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()
```
- As duas docstrings seguidas (a primeira logo após `def`, e a segunda logo abaixo) são, na prática, uma **duplicação**: a primeira é a docstring oficial da função (acessível via `.__doc__`); a segunda é apenas uma string "solta" que não tem efeito nenhum no programa (não é atribuída a nada, nem impressa) — é código residual que pode ser removido com segurança.
- `exibir_subtitulo('Cadastro de novos restaurantes')` — limpa a tela e mostra o cabeçalho da seção.
- `nome_do_restaurante = input(...)` — captura o nome digitado pelo usuário e guarda na variável `nome_do_restaurante`.
- `categoria = input(f'...')` — usa uma **f-string** (string formatada) para inserir o nome do restaurante já digitado dentro da pergunta sobre a categoria, tornando a interação mais personalizada.
- `dados_do_restaurante = {...}` — monta um novo dicionário com os dados coletados. O campo `'ativo'` começa sempre como `False` (todo restaurante novo nasce desativado).
- `restaurantes.append(dados_do_restaurante)` — adiciona esse novo dicionário à lista global `restaurantes`, usando o método `.append()` de listas.
- `print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')` — confirma o cadastro ao usuário, novamente usando f-string para interpolar o nome.
- `voltar_ao_menu_principal()` — pausa e retorna ao menu principal.

---

## `listar_restaurantes()`

```python
def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista
    ...
    '''
    exibir_subtitulo('Listando restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()
```
- `exibir_subtitulo('Listando restaurantes')` — mostra o cabeçalho da seção.
- `print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")` — imprime o cabeçalho da "tabela". O método `.ljust(n)` alinha o texto à esquerda preenchendo com espaços até completar `n` caracteres, criando colunas alinhadas visualmente. O `|` funciona como separador de coluna.
- `for restaurante in restaurantes:` — laço que percorre cada dicionário dentro da lista `restaurantes`, um de cada vez, atribuindo-o à variável `restaurante` a cada iteração.
  - `nome_restaurante = restaurante['nome']` — acessa o valor da chave `'nome'` do dicionário atual.
  - `categoria = restaurante['categoria']` — acessa o valor da chave `'categoria'`.
  - `ativo = 'ativado' if restaurante['ativo'] else 'desativado'` — **expressão condicional (ternária)**: se `restaurante['ativo']` for `True`, a variável recebe `'ativado'`; caso contrário, recebe `'desativado'`.
  - `print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')` — imprime a linha da tabela para aquele restaurante, também alinhada com `.ljust()`.
- `voltar_ao_menu_principal()` — ao fim da listagem, pausa e volta ao menu.

---

## `alternar_estado_restaurante()`

```python
def alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante
    ...
    '''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()
```
- `exibir_subtitulo('ALterando estado do restaurante')` — mostra o cabeçalho (note o "L" maiúsculo no meio da palavra "ALterando", um pequeno erro de digitação sem impacto funcional).
- `nome_restaurante = input(...)` — captura o nome do restaurante que o usuário quer alternar.
- `restaurante_encontrado = False` — variável de controle (flag) inicializada como `False`, usada para saber, depois do laço, se algum restaurante correspondente foi encontrado.
- `for restaurante in restaurantes:` — percorre todos os restaurantes cadastrados.
  - `if nome_restaurante == restaurante['nome']:` — compara o nome digitado com o nome do restaurante atual do laço (comparação **sensível a maiúsculas/minúsculas e a espaços**).
    - `restaurante_encontrado = True` — marca que houve correspondência.
    - `restaurante['ativo'] = not restaurante['ativo']` — inverte o valor booleano atual (`True` vira `False` e vice-versa), alternando o estado.
    - `mensagem = f'...' if restaurante['ativo'] else f'...'` — monta a mensagem de sucesso apropriada (ativado ou desativado) conforme o novo estado.
    - `print(mensagem)` — exibe a mensagem.
- `if not restaurante_encontrado:` — depois do laço, se a flag continuar `False` (nenhum restaurante bateu com o nome digitado), informa que não encontrou.
- `voltar_ao_menu_principal()` — pausa e retorna ao menu.

---

## `escolher_opcao()`

```python
def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário
    ...
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
```
- `try:` — inicia um bloco de tratamento de exceções, protegendo o código de erros que travariam o programa.
- `opcao_escolhida = int(input('Escolha uma opção: '))` — pede um número ao usuário e converte o texto digitado para `int`. Se o usuário digitar algo que não seja um número (ex: "abc"), o `int()` lança uma exceção (`ValueError`).
- `# opcao_escolhida = int(opcao_escolhida)` — linha comentada (não executada); parece ser um resquício de uma versão anterior do código, sem efeito algum.
- `if / elif / elif / elif / else` — estrutura condicional em cadeia que decide qual função chamar de acordo com o número escolhido:
  - `1` → `cadastrar_novo_restaurante()`
  - `2` → `listar_restaurantes()`
  - `3` → `alternar_estado_restaurante()`
  - `4` → `finalizar_app()`
  - qualquer outro número → `opcao_invalida()`
- `except:` — captura **qualquer** tipo de exceção (inclusive erros inesperados). Caso ocorra qualquer erro no bloco `try` (por exemplo, entrada não numérica), chama `opcao_invalida()`.

---

## `main()`

```python
def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
```
Função que orquestra o fluxo principal do programa:
1. `os.system('cls')` — limpa a tela.
2. `exibir_nome_do_programa()` — mostra o logo ASCII.
3. `exibir_opcoes()` — mostra o menu numerado.
4. `escolher_opcao()` — pede e processa a escolha do usuário, disparando a função correspondente.

---

## Bloco de execução

```python
if __name__ == '__main__':
    main()
```
Verifica se o arquivo está sendo executado **diretamente** (não importado como módulo por outro arquivo). `__name__` é uma variável especial do Python que vale `'__main__'` quando o script é rodado diretamente. Se verdadeiro, chama `main()`, iniciando o programa.

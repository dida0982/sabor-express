# Conceitos e Comandos Utilizados — `app.py`

Este documento explica, de forma independente do código específico, **cada conceito, comando, estrutura e método de Python** utilizado no projeto. A ideia é servir como material de estudo/referência, e não apenas descrever o que aquela linha faz no contexto do programa.

---

## 1. Módulos e importação

### `import os`
O módulo `os` faz parte da **biblioteca padrão** do Python e permite interagir com o sistema operacional: manipular arquivos, pastas, variáveis de ambiente e executar comandos do terminal. No projeto, ele é usado apenas para `os.system('cls')`.

### `os.system(comando)`
Executa um comando do **terminal/console** como se ele tivesse sido digitado manualmente. `'cls'` é o comando de limpar tela no **Windows** (Prompt de Comando). Em sistemas Unix (Linux/macOS) o comando equivalente é `'clear'`. Por isso, esse trecho do código é dependente de plataforma — se rodar o `app.py` no Linux/Mac, a tela não será limpa.

---

## 2. Estruturas de dados

### Listas (`list`)
Uma lista é uma coleção **ordenada e mutável** de itens, criada com colchetes `[]`. No projeto, `restaurantes` é uma lista que armazena vários dicionários. Métodos usados:
- `.append(item)`: adiciona um item ao final da lista.

### Dicionários (`dict`)
Estrutura de **pares chave-valor**, criada com chaves `{}`. Cada restaurante é representado como `{'nome': ..., 'categoria': ..., 'ativo': ...}`. O acesso a um valor é feito por `dicionario['chave']`, por exemplo `restaurante['nome']`.

### Booleanos (`bool`)
Tipo que representa `True` ou `False`. Usado no campo `'ativo'` para indicar se um restaurante está ativado.

---

## 3. Funções

### `def nome_da_funcao(parametros):`
Define um bloco de código reutilizável. No projeto, quase toda a lógica é organizada em funções (uma responsabilidade por função), o que é uma boa prática chamada de **separação de responsabilidades**.

### Docstrings (`''' texto '''`)
Strings colocadas logo após a definição de uma função (ou classe/módulo), usadas para documentar o que ela faz, seus parâmetros ("Inputs") e o que ela produz ("Outputs"). Podem ser acessadas em tempo de execução via `nome_da_funcao.__doc__`. Diferente de um comentário comum (`#`), a docstring é parte da estrutura da linguagem e ferramentas de documentação automática conseguem lê-la.

### Funções sem `return`
Todas as funções do projeto realizam ações (imprimir na tela, alterar a lista global) mas não retornam valores com `return`. Isso é chamado de função com **efeito colateral** (side effect) — ela existe para *fazer algo*, não para *calcular e devolver um valor*.

### Recursão indireta via `main()`
`voltar_ao_menu_principal()` chama `main()`, que eventualmente pode levar de volta a `voltar_ao_menu_principal()`. Isso cria um ciclo de chamadas de função (uma espécie de "loop" implementado através de chamadas de função em vez de um `while`). É uma alternativa válida a um laço `while True`, mas tem uma limitação técnica: em Python, cada chamada de função consome espaço na **pilha de chamadas** (call stack); um uso muito prolongado desse padrão poderia, em teoria, esbarrar no limite de recursão do Python (ainda que na prática, para um programa interativo como esse, dificilmente isso ocorre, pois cada iteração depende de uma ação manual do usuário).

---

## 4. Entrada e saída de dados

### `input(mensagem)`
Exibe `mensagem` no console e pausa a execução até o usuário digitar algo e pressionar Enter. O valor retornado é **sempre uma string** (texto), mesmo que o usuário digite números.

### `print(...)`
Exibe informações no console. Pode receber várias formas de string, inclusive strings multi-linha (delimitadas por `"""` ou `'''`).

### `int(valor)`
Converte um valor (geralmente uma string vinda de `input()`) para um número inteiro. Se o texto não puder ser convertido (ex: `"abc"`), lança uma exceção `ValueError`.

---

## 5. Strings e formatação

### F-strings (`f'texto {variavel}'`)
Permitem inserir o valor de variáveis diretamente dentro de uma string, colocando-as entre chaves `{}`. É a forma moderna e recomendada de formatar strings em Python (substitui o antigo `.format()` e o operador `%`).

### `str.ljust(largura)`
Método de string que **alinha o texto à esquerda**, completando com espaços em branco à direita até atingir o número de caracteres definido em `largura`. Muito usado para criar colunas alinhadas em saídas de texto no terminal (como uma tabela simples).

### Multiplicação de strings (`'*' * n`)
Em Python, o operador `*` aplicado a uma string e um número inteiro repete a string aquele número de vezes. Ex.: `'*' * 5` resulta em `'*****'`. Usado para criar bordas dinâmicas proporcionais ao tamanho do texto.

### `len(objeto)`
Retorna o número de elementos de um objeto — no caso de uma string, o número de caracteres.

---

## 6. Estruturas de controle

### `if / elif / else`
Estrutura condicional que executa diferentes blocos de código dependendo de uma condição. `elif` é a contração de "else if", permitindo encadear múltiplas condições.

### Expressão condicional (operador ternário)
```python
valor = resultado_se_verdadeiro if condicao else resultado_se_falso
```
Uma forma compacta de escrever um `if/else` que **retorna um valor**, útil para atribuições rápidas (usado tanto em `listar_restaurantes()` quanto em `alternar_estado_restaurante()`).

### `for item in colecao:`
Laço de repetição (**for loop**) que percorre cada elemento de uma coleção (lista, dicionário, string, etc.), executando o bloco de código para cada um deles.

### Operador `not`
Operador lógico que inverte um valor booleano: `not True` resulta em `False` e vice-versa. Usado para alternar o estado `ativo`/`inativo` de um restaurante.

### Operador de igualdade `==`
Compara dois valores e retorna `True` se forem iguais, `False` caso contrário. Diferente do `=`, que é usado para atribuição.

---

## 7. Tratamento de erros

### `try / except`
Estrutura que permite **capturar e tratar exceções** (erros) sem que o programa pare de funcionar abruptamente. O bloco `try` contém o código que pode falhar; o bloco `except` define o que fazer caso um erro ocorra.

⚠️ **Boa prática:** o código usa um `except:` "genérico" (sem especificar o tipo de exceção), o que captura **qualquer** erro, incluindo erros de programação inesperados (ex: `KeyboardInterrupt`, `MemoryError`). O recomendado, em geral, é capturar exceções específicas, como `except ValueError:`, para evitar mascarar bugs não relacionados à validação de entrada.

---

## 8. Variáveis globais

A lista `restaurantes` é definida fora de qualquer função (no escopo do módulo), tornando-a uma **variável global**. Funções como `cadastrar_novo_restaurante()` e `alternar_estado_restaurante()` conseguem **ler e modificar** essa lista diretamente sem precisar declará-la com a palavra-chave `global`, porque estão apenas alterando o conteúdo da lista (`.append()`, alterar um item) e não reatribuindo a variável em si (`restaurantes = outra_coisa`).

---

## 9. Ponto de entrada do programa

### `if __name__ == '__main__':`
Um padrão extremamente comum em scripts Python. `__name__` é uma variável especial que o Python define automaticamente:
- Quando o arquivo é executado diretamente (`python app.py`), `__name__` vale `'__main__'`.
- Quando o arquivo é importado por outro script (`import app`), `__name__` vale `'app'`.

Esse padrão garante que o código dentro do `if` (chamar `main()`) só rode quando o arquivo for executado diretamente, e não quando for importado como módulo em outro projeto.

---

## Resumo dos comandos/conceitos por categoria

| Categoria | Itens usados |
|---|---|
| Módulos | `os`, `os.system()` |
| Estruturas de dados | listas, dicionários, booleanos |
| Funções | `def`, docstrings, ausência de `return` |
| Entrada/Saída | `input()`, `print()`, `int()` |
| Strings | f-strings, `.ljust()`, multiplicação de string, `len()` |
| Controle de fluxo | `if/elif/else`, operador ternário, `for`, `not`, `==` |
| Erros | `try/except` |
| Escopo | variável global |
| Estrutura de script | `if __name__ == '__main__':` |

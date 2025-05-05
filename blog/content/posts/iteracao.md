+++
date = '2025-04-30T23:04:21-03:00'
title = 'Python Nuclear: Iteração'
toc = true
draft = true
+++

> Há 2 problemas difíceis em ciência da computação: invalidar cache, nomear coisas e errar por 1.
<br>---*Leon Bambrick*

Duas variantes de erro-por-1 ao percorrer uma coleção:

* laço termina no penúltimo item, o último é ignorado;
* laço vai além do último item, acessando
memória inválida, ou terminando com
[*segfault*](https://pt.wikipedia.org/wiki/Falha_de_segmenta%C3%A7%C3%A3o)

Esses bugs são raros em Python,
porque quase nunca precisamos lidar com índices
ou ler o comprimento da coleção
para percorrer seus itens.


```python
>>> serie = 'abc'
>>> for letra in serie:
...     print(letra.upper())
...
A
B
C

```

Parte da inteligência está na instrução `for`, outra parte
está no conceito de *iterável*, aquilo que pode ser iterado
(percorrido sequencialmente)--da mesma forma que *comestível*
significa aquilo que pode ser comido.

Python oferece várias estruturas de dados iteráveis prontas para
usar:

* sequências como `str`, `bytes`, `list`, `array`: coleções ordenadas de itens;
* outras coleções como `dict`, `set`, `deque`: nem sempre ordenadas;
* geradores como `map()`, `filter()`, `groupby()`: funções que produzem um item de cada vez, sob demanda.

Por exemplo, o gerador `map()` aplica uma função a cada item de um iterável, produzindo um resuldado por vez.

Invocá-la sozinha produz isso:

```python
>>> serie = 'abc'
>>> map(str.upper, serie)  # doctest: +ELLIPSIS
<map object at 0x...>

```

O `map object` resultante de de invocar `map()` é um *objeto gerador*, que é iterável:

```python
>>> for letra in map(str.upper, serie):
...     print(letra)
...
A
B
C

```

## Desempacotar iteráveis

Python opera com iteráveis em outros contextos além do laço `for`.

Você pode *desempacotar* um iterável em diferentes variáveis
através da atribuição paralela, assim:

```python
>>> x, y, z = map(ord, serie)
>>> x
97
>>> y
98
>>> z
99

```

A atribuição paralela também funciona no laço `for`.
Veja a atribuição a `chave, valor` neste exemplo:

```
>>> d = {'a': 10, 'b': 20, 'c': 30}
>>> d.items()
dict_items([('a', 10), ('b', 20), ('c', 30)])
>>> for chave, valor in d.items():
...     print(chave, '->', valor)
...
a -> 10
b -> 20
c -> 30

```

Outro exemplo de desempacotar iterável é prefixar um argumento
com `*` ao chamar uma função. Isso desempacota o argumento,
passando seus itens como argumentos separados:

```python
>>> def mostrar(a, b, c):
...     print(a, b, c)
...
>>> letras = 'XYZ'
>>> mostrar(*letras)
X Y Z

```


## Funções auxiliares para iteração

Três funções geradoras são úteis em muitos contextos de iteração:

### `enumerate`: numeração de itens

A chamada `enumerate(serie)` produz uma dupla de valores para cada
item da `serie`: um índice e o próprio item.

```python
>>> serie = 'abc'
>>> list(enumerate(serie))
[(0, 'a'), (1, 'b'), (2, 'c')]

```

A numeração começa em 0 por padrão, mas você pode especificar outro
número inicial:

```python
>>> for n, l in enumerate(serie, 10):
...     print(f'{n}: {l}')
...
10: a
11: b
12: c

```

### `zip`: pareamento de séries paralelas

Um zipper acopla dentes de duas fitas paralelas;
a função `zip` faz o mesmo com itens de séries paralelas.

```python
>>> valores = [3, 5, 8]
>>> letras = 'XYZ'
>>> for v, l in zip(valores, letras):
...     print(v * l)
...
XXX
YYYYY
ZZZZZZZZ

```

`zip` pode ser usado para transpor
linhas e colunas em uma matriz construída com iteráveis aninhados.
O truque é usar o prefixo `*` para desempacotar os iteráveis internos
como argumentos separados para o `zip`.
Por exemplo, começamos com uma matriz de 2 linhas e 3 colunas,
e transformamos as linhas em colunas e vice-versa:

```python
>>> m = [(1, 2, 3), (4, 5, 6)]
>>> list(zip(*m1))
[(1, 4), (2, 5), (3, 6)]

```

> **Nota**: a biblioteca NumPy suporta matrizes N-dimensionais
muito mais eficientes e compactas que iteráveis aninhados.
Esse exemplo ajuda a pensar no poder do `zip`.


O gerador `zip` aceita qualquer número de iteráveis (não apenas 2 como nos exemplos).

> **Nota:** Por padrão, o `zip` encerra assim que encontra o fim do primeiro iterável.
Esse comportamento pode ser útil em alguns casos,
mas vai contra a filosofia de Python de evitar falhas silenciosas.
Com o parâmetro nomeado `strict=True`, o `zip` levanta uma exceção caso
um dos iteráveis termine antes dos outros.


As três funções mais úteis


## A beleza do `for`

A super-poder dos computadores é repetir tarefas bilhões de vezes.
Seu programa *itera* sobre uma série de itens,
filtrando, transformando e agregando.

+++
date = '2025-04-30T23:04:21-03:00'
title = 'Picada de Python: Iteração'
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

A `serie` pode ser uma sequência (`str`, `bytes`, `list`, `array`)
ou coleção (`dict`, `set`, `deque`)
ou um gerador (`map()`, `filter()`, `groupby()`).
Todos esses são exemplos de **iteráveis** (*iterable*).


## Desempacotar iteráveis



```python
>>>

```

## Iteráveis essenciais

As três funções mais úteis


## A beleza do `for`

A super-poder dos computadores é repetir tarefas bilhões de vezes.
Seu programa *itera* sobre uma série de itens,
filtrando, transformando e agregando.

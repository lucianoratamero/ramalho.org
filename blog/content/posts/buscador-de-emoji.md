+++
date = '2025-06-08T16:38:34-03:00'
title = 'Um buscador de emoji super simples'
toc = true
draft = false
tags = ['tecnologia',]
+++

O `cf.py` é um utilitário de linha de comando para buscar caracteres unicode pelo nome.
Exemplo de uso:

```
$ ./cf.py cat eyes
U+1F638     😸       GRINNING CAT FACE WITH SMILING EYES
U+1F63B     😻       SMILING CAT FACE WITH HEART-SHAPED EYES
U+1F63D     😽       KISSING CAT FACE WITH CLOSED EYES
```

Este é um dos meus exemplos didáticos favoritos, porque é simples, interativo,
e aborda dois temas que me interessam: Unicode e conjuntos.[^1]

[^1]: Também já fiz esse exemplo em [Elixir e Go](https://github.com/ramalho/rf).
Tentei fazer em Rust mas achei muito complicado e desisti.
Quem sabe alguém faz em Rust e manda um PR lá no [repositório rf](https://github.com/ramalho/rf). 😉

O [cf.py](https://pythonfluente.com/2/#ex_cfpy) está na 2ª edição do Python Fluente.
É uma variante bem simplificada do [charfinder](https://github.com/fluentpython/example-code/tree/d5133ad6e4a48eac0980d2418ed39d7ff693edbe/18-asyncio/charfinder) que apareceu na 1ª edição do Python Fluente.

Este é o código-fonte completo do [cf.py](https://pythonfluente.com/2/#ex_cfpy):

```
#!/usr/bin/env python3
import sys
import unicodedata

START, END = ord(' '), sys.maxunicode + 1           

def find(*query_words, start=START, end=END):
    query = {w.upper() for w in query_words}        # ➊
    for code in range(start, end):
        char = chr(code)
        name = unicodedata.name(char, None)
        if name and query.issubset(name.split()):   # ➋
            print(f'U+{code:04X}\t{char}\t{name}')

def main(words):
    if words:
        find(*words)
    else:
        print('Please provide words to find.')

if __name__ == '__main__':
    main(sys.argv[1:])
```

No livro, ponto principal desse exemplo é demonstrar a utilidade
da função `unicodedata.name(x)`, que devolve o nome do caractere `x`.

Isso é óbvio, mas a sacada não óbvia é uso de um conjunto nas linhas assinaladas:

➊: Converte `query_words` em um `set` de palavras.

➋: Dado um `name`, divide em palavras e verifica se esta lista é um subconjunto de `query`.

Tratar a `query` como um conjunto permite usar o método `.issubset()` que aceita qualquer sequência como argumento.

Então, o programa exibe um resultado quando todas as palavras da `query` aparecem em `name.split()`,
independente da ordem, e mesmo que o `name` contenha outras palavras,
inclusive palavras que podem aparecer entre as palavras da consulta:

* buscando "CAT EYES" você encontra "KISSING CAT FACE WITH CLOSED EYES", e mais 2 emojis;
* buscando "FACE GRINNING" você encontra "GRINNING FACE" e mais 4 emojis.

Outro dia uma pessoa postou no LinkedIn que se inspirou neste exemplo para criar a biblioteca
e o utilitário de linha de comando [`charfinder`](https://pypi.org/project/charfinder/).

Infelizmente, o autor do pacote não captou a ideia de usar um conjunto.
Ele oferece 3 algoritmos de casamento aproximado de strings (_fuzzy maching_).
Tem até um vídeo de demonstração e muitos outros recursos,
além de estar empacotado como uma biblioteca instalável,
enquanto o `cat.py` é apenas aquele exemplo didático de 22 linhas de código,
sem dependências externas.

Mas, se você procurar "cat eyes", o `charfinder` v. 1.0.8 não encontra nada.[^2]

```
$ python3 -m charfinder -q "cat eyes"
Rebuilding Unicode name cache. This may take a few seconds...
Cache written to: unicode_name_cache.json
No matches found for query: 'cat eyes'
```

É chato criticar o trabalho dos outros.

Mas estou sendo chato aqui para falar sobre
esse problema tão comum: às vezes a gente viaja tanto nas
altas tecnolgias que esquece o básico.

A melhoria #1 que eu gostaria de fazer no `cf.py` é aceitar
consultas em português.
Mas aí não é problema de algoritmo.
É falta de dados: onde encontrar uma versão do
[unicodedata.txt](https://www.unicode.org/Public/16.0.0/ucd/UnicodeData.txt)
com os nomes em PT-BR?

Se souber, me manda a dica!

[^2]: Para não ficar só reclamando aqui, cadastrei uns
[issues lá](https://github.com/berserkhmdvhb/charfinder/issues).

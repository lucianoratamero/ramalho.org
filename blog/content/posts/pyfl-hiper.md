+++
date = '2025-05-24T15:54:37-03:00'
title = 'Python Fluente como hipertexto'
toc = true
draft = true
tags = ['livro']
+++

Sempre curti a ideia de hipertexto: um texto
que oferece caminhos além do caminho reto do
começo até o fim.

O _Fluent Python_ pode ser lido em linha reta,
mas também oferece muitos caminhos alternativos:

* Referências cruzadas: citações de outra parte do próprio livro,
tipo "Aprofundaremos esse tema na Seção 16.3", ou "Como já vimos no exemplo 3".

* Referências externas: a Segunda Edição tem mais de 1000 links
para outros livros, vídeos, artigos, código etc.

Esse post é sobre como tenho trabalhado com as referências dos dois tipos.


## Juntando referências externas

A coisa mais importante que aprendi na faculdade foi fazer pesquisa.
Ao escrever as edições do _Fluent Pyhon_,
escolho um assunto e saio pesquisando artigos, blogs, vídeos.
Sempre que ach algo interessante, copio a URL para o final do
arquivo que representa um capítulo no livro.
Às vezes a URL é relevante para um capítulo que eu nem escrevi
ainda, daí eu crio o arquivo `cap-N.adoc` só para ter onde
salvar a URL.

Daí na fase final de redação de cada capítulo eu escrevo
a seção [Para saber mais](https://pythonfluente.com/2/#_para_saber_mais_5)
(esta é do capítulo
[21—Programação assíncrona](https://pythonfluente.com/2/#ch_async)).
Ali eu compartilho com vocês os melhores materiais que encontrei
sobre aquele assunto, em alguns casos resumindo os pontos que achei
mais interessantes.

No final, acabei reunindo mais de 1000 URLs externas no livro.
Como eu sei? Fiz um script para verificar as URLs e outro
para gerar URLs e configurar URLs encurtadas no meu site `fpy.li`
que só serve para isso.

Por exemplo, esta URL seria um trambolho dentro do texto corrido
do livro impresso:

https://www.artima.com/weblogs/viewpost.jsp?thread=235725

Então criei esta URL curta que leva ao mesmo destino:

https://fpy.li/bdfl

Como o papel não é clicável, o prefixo `http://` não é
necessário, então no livro aparece um texto assim:

> Veja Guido van Rossum em _Origin of BDFL (fpi.li/bdfl)_.


## Verificando URLs


## Referências no papel x na tela


## Encurtando URLs


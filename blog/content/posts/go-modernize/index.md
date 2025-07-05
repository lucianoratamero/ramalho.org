+++
date = '2025-07-04T15:42:06-03:00'
title = 'Modernizando Go'
toc = false
draft = false
tags = ['tecnologia', 'golang', 'programming languages']
+++

Peguei os exemplos do livro «The Go Programming Language» e atualizei com a ferramenta
[modernize](https://pkg.go.dev/golang.org/x/tools/gopls/internal/analysis/modernize).

Em 2016 fiz a revisão técnica da tradução brasileira do livro
[A Linguagem de Programação Go](https://novatec.com.br/livros/linguagem-de-programacao-go/),
de Alan A. A. Donovan e Brian W. Kernighan[^1], conhecido pela sigla GOPL.
Naquele trabalho defendi a adoção da palavra "gorrotina" para traduzir "goroutine".
Talvez o GOPL da Novatec seja o primeiro livro em português a utilizar a palavra
_gorrotina_.

<!--more-->

{{< figure
  src="capa-ampliada-9788575225462.jpg"
  alt="Início de uma mão de Eleusis"
  link="[capa-ampliada-9788575225462.jpg](https://novatec.com.br/livros/linguagem-de-programacao-go/)"
  caption="Capa do livro «A Linguagem de Programação Go» de Donovan & Kernighan (Novatec, 2017)"
  width="200"
>}}

GOPL é um dos melhores livros que já li para apresentar uma nova linguagem
desde o zero, para programadoras experientes.
Ele não explica o que é "variável" ou "stack": assume que a leitora
tem bom domínio de outra linguagem de programação.

O GOPL foi lançado em 2016 nos EUA (2017 no Brasil),
então está um tanto desatualizado.
Os conceitos fundamentais estão lá, muito bem explicados,
e todo o código do GOPL funciona no Go 1.24,
mas hoje há formas melhores de codar alguns exemplos do livro
principalmente depois que Go passou a suportar generics.

Para me atualizar em Go estou revendo os exemplos do GOPL e pensando
em formas de melhorá-los com recursos mais modernos da linguagem.

## Usando modernize

O primeiro passo foi automático: apliquei a ferramenta
[modernize](https://pkg.go.dev/golang.org/x/tools/gopls/internal/analysis/modernize)
em todos os exemplos do livro, usando este comando[^2]:

```shell
go run golang.org/x/tools/gopls/internal/analysis/modernize/cmd/modernize@latest \
-fix -test ./...
```

O pacote `modernize` serve para refatorar código
para um estilo moderno de Go idiomático.
A [documentação da ferramenta](https://pkg.go.dev/golang.org/x/tools/gopls/internal/analysis/modernize)
descreve 14 categorias de diagnósticos e reparos, por exemplo:

* `for i := range n` em vez de `for i := 0; i < n; i++`;
* `any` em vez de `interface{}`;
* `min()`/`max()` em vez de `if...` para atribuir o maior/menor valor a uma variável.

No código do GOPL, o `modernize` arrumou exemplos somente nas três categorias acima.
O caso de `min/max` representa muitas melhorias da biblioteca de Go nos últimos
anos: essas funções não existiam antes da linguagem suportar generics.

Depois das mudanças automáticas do `modernize`, abri os exemplos no Visual Code e a extensão oficial
[golang.go](https://marketplace.visualstudio.com/items?itemName=golang.go) indicou um par de referências
a `io/ioutil` que hoje podem ser escritas acessando `io` direto:

* `io.ReadAll`
* `io.Discard`

Use a interface de visualizção do commit
[3fae409](https://github.com/garoago/gopl-modernized/commit/3fae409e98027a01fa851d52eedcbc99b6c6401b)
para ver todas as mudanças.

Sei que há outras oportunidades de modernização dos exemplos do GOPL.
O exemplo [IntSet](https://github.com/garoago/gopl-modernized/tree/master/ch6/intset)
na seção 6.5 pode ganhar um interador,
e também uma API genérica suportando diferentes tipos de inteiros.

Com certeza há mais exemplos que podem ser modernizados,
só que agora teremos que usar o bestunto.

Mas por agora, sextou.

Bom fim de semana!


[^1]: Esse é o mesmo Kernighan do clássico "A linguagem de programação C",
conhecido pelas iniciais K&R dos autores Kerninghan e (Dennis) Ritchie.
Kernighan foi o criador do primeiro exemplo "hello, world" da história,
[segundo a Wikipédia](https://pt.wikipedia.org/wiki/Programa_Ol%C3%A1_Mundo).

[^2]: Essa linha de comando com 98 caracteres é ridícula, mas não encontrei
outra forma de usar o modernize, exceto criando um script de shell que chamei de
[mdrnz.sh](https://github.com/garoago/gopl-modernized/blob/master/mdrnz.sh).
Eu esperava usar um comando com `go modernize` ou algo assim,
mas não encontrei uma solução pronta na Web.
Se você sabe, por gentileza manda a dica como um
[issue](https://github.com/ramalho/ramalho.org/issues) neste blog,
ou manda pra mim no Bluesky @ramalho.org ou no
Mastodon @lr@ciberlandia.pt.
Sua contribuição será muito bem-vinda!


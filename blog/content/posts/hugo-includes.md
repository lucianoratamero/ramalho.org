+++
date = '2025-05-05T17:11:02-03:00'
title = 'O problema dos includes no Hugo'
toc = true
draft = true
+++

[Hugo Borges](https://garoa.net.br/wiki/Usu%C3%A1rio:Agaelebe)
é um dos fundadores do
[Garoa Hacker Clube](https://garoa.net.br/wiki/P%C3%A1gina_principal).
Um hacker excelente que colabora com ideias, trabalho e equipamentos
para nosso latoratório comunitário. Esse texto não é sobre ele.

[Hugo](https://gohugo.io) é um gerador de páginas estáticas para sítios Web.
Foi aqui que encontrei o problema dos includes.
Esse blog eu faço com Hugo.

Além de popular, fácil de instalar e rápido,
Hugo implementa ótimas práticas sobre arquitetura da informação,
separação conteúdo/apresentação, gerenciamento/customização de temas.
Seu criador, Steve Francia, havia dedicado muito tempo
contribuindo com o Drupal[^1].
Como especialista em sistemas de gestão de conteúdo
e ex-instrutor de Plone[^2], aprecio e aproveito
as práticas de gestão de conteúdo suportadas pelo Hugo.

[^1]: Um sofisticado CMS livre escrito em PHP: https://new.drupal.org/
[^2]: Um sofisticado CMS livre escrito em Python: https://plone.org/.

Por isso me surpreende a falta de uma boa maneira de incluir um arquivo
dentro de uma página de conteúdo.

<!-- Claude me ajudou a encontrar "extensos", mas "enormes" me ocorreu depois
e é melhor. E finalmente resolvi de outro jeito
mas o brainstorm foi últil mesmo assim.
https://claude.ai/share/5a795c85-542b-4f79-9779-f06d8c3666cf
-->

## O problema

Quero mostrar várias linhas de código-fonte `.go`
dentro de um artigo em Markdown.
Minha necessidade é escrever no `.md`
apenas uma instrução tipo `❴❴incluir programa.go❵❵`
e não copiar e colar o código Go dentro do `.md`, pricipalmente
porque eu quero poder compilar o código do `.go` para testá-lo facilmente.

Em qualquer CMS, um mecanismo de *include* tem um uso principal,
que é facilitar o reaproveitamento de código HTML através
de diferentes modelos de páginas (templates), para facilitar
a navegação, e a diagramação padronizada e customizável do site.
Nesse aspecto o Hugo é sensacional.

Mas o que eu preciso, e o povo clama[^3], é um jeito de
fazer algo muito mais simples que um parser de templates
recursivo: um mísero comando para ler um arquivo do mesmo
diretório e formatá-lo como código-fonte colorizado.

[^3]: Encontrei > 3 (!!!) discussões no https://gohugo.io sobre esse tema,
começando há mais de 10 anos e continuando até recentemente.

E tal comando não existe.

https://gohugo.io/shortcodes/

https://gohugo.io/templates/shortcode/

https://gohugo.io/content-management/shortcodes/

https://gohugo.io/shortcodes/highlight/

https://ksucs-hugo.russfeld.me/shortcodes/include/

https://github.com/squidfingers/hugo-shortcodes

https://mcshelby.github.io/hugo-theme-relearn/shortcodes/include/index.html


Hugo já tem funções para ler um arquivo e para colorizar
código fonte.
Mas elas só podem ser usadas em templates,
e não no conteúdo escrito em Markdown, que é onde eu preciso.
Dentro de um `.md` no Hugo, esse tipo de lógica tem que
ser implementada como um *shortcode*, uma função escrita
na linguagem de templates, e instalada no diretório
`layouts/shortcodes`.


Poderiam ter feito um *shortcode*, comando que funciona dentro
de `.md` no Hugo, mas não fizeram. Então fui procurar.
O resto deste texto é sobre o que encontrei e
como resolvi o problema no https://ramalho.org.

## As alternativas

Passei um par de horas revirando a documentação e discussões em https://gohugo.io até
concluir que o que eu queria não existe (em 2025-05-05),
e que a melhor solução é copiar o código de algum
shortocode publicado na Web.[^4]

[^4]: Muitos usuários de Hugo que publicam códido-fonte talvez usem
algum tema pronto que já forneça o shortcode que eu preciso,
como é o caso do
[Geekdoc](https://github.com/thegeeklab/hugo-geekdoc)
(também conhecido como [Geekdocs](https://geekdocs.de/)).
Mas eu resolvi construir meu próprio tema do zero,
então às vezes preciso reinventar a roda.

Cada uma dessas páginas apresenta o código de um shortcode:

1. [Hugo: Injecting an external file into a page with syntax highlighting](https://me.micahrl.com/blog/hugo-shortcode-importcode/)

2. [How to include code examples from file with Hugo](https://marcusolsson.dev/how-to-include-code-examples-from-file-with-hugo/)

3. [Include code from a file with Hugo](https://www.marcusfolkesson.se/blog/include-code-from-a-file-with-hugo/)

4. [Include shortcode from hugo-geekdoc](https://github.com/thegeeklab/hugo-geekdoc/blob/1bb1dab866fbd0b6bf28d2f0aaeaaced7e814fc0/layouts/shortcodes/include.html)


```
# 8< trecho1:

# 8< trecho1.
```

+++
date = '2025-05-27T05:56:28-03:00'
title = 'HTTP: estes não são os androides que você procura'
toc = false
draft = true
tags = ['tecnologia', 'Web']
+++

A Web é o hipertexto universal.

Como qualquer hipertexto, é feita de conteúdos vinculados por _links_, no formato de URLs.

Em um hipertexto vivo, os textos mudam de lugar, desaparecem, são editados.

O servidor precisa ter como avisar o _user agent_[^1]
que o _link_ fornecido precisa ser atualizado ou não serve mais,
porque a localização do alvo mudou.

Para isso servem os códigos de resposta 3XX do procolo HTTP,
muito bem documentados na
[Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes).

Aqui vou comentar uns códigos interessantes.

## 301 — Mudou-se permanentemente

Se o cliente pede para ler http://bit.ly/4my8Wev
o servidor pode dizer, essa página agora está nesse outro local:
https://mitpress.mit.edu/9780262111584/the-art-of-the-metaobject-protocol/

O servidor da `bit.ly` manda a resposta 301, e _user agent_
deve atualizar seu livro de endereços para que no futuro sempre
vá direto ao `mitpress.mit.edu/...`,
porque a mudança é permanente.

O `bit.ly` não deve mais ser incomodado com essa requisição.

## 302 — No momento está aqui

No [PythonFluente.com](http://pythonfluente.com/) os links
para referências em outros sites tem essa cara:
http://fpy.li/1-1.

O servidor `fpi.li` responde ao caminho `/1-1` com o código 302 e a URL
http://hugunin.net/story_of_jython.html.

O 302 informa o _user agent_ que é um redirecionamento temporário.
Assim, se o site `hugunin.net` sair do ar, eu poderei reconfigurar
o `fpi.li` para direcionar o cliente para outro lugar,
como uma cópia da página do Internet Archive
(que
[existe](https://web.archive.org/web/20250320173953/http://hugunin.net/story_of_jython.html)).

Ao receber um 302, o _user agent_ deve seguir para a localização indicada,
mas não atualizar seu livro de endereços.
No próximo acesso ao texto "Story of Jython", o _user agent_ deve
começar acessando http://fpy.li/1-1.

Volte aqui porque talvez tenhamos um destino novo para você.

## 410 — Já era

Esse não é um código de redirecionamento,
mas tem tudo a ver com o hipertexto vivo.

A mensagem padrão do 410 é "Gone", literalmente "Já era".
O conteúdo que você procura não existe mais.
É diferente do famoso 404 "Not found", que diz:
isso que você procura nunca existiu.

O 410 informa que ali havia algo, mas não mais.

Chega a ser lírico.

## Por hoje é só

Captou?

O protocolo HTTP foi pensado para sustentar um hipertexto distribuído global,
feito por seres humanos.

Nesse contexto, é necessário que servidores e _user agents_ troquem mensagens
sobre conteúdos que mudaram de lugar ou não existem mais.

A Web é uma coisa linda.


[^1]: A Web é um sistema cliente-servidor, mas a terminologia canônica
fala de _user agent_ em vez de _client_.
Não sei a origem desse termo, mas para mim ele é útil para distinguir
o software cliente da pessoa cliente ou usuária.
_User agent_ pode ser aplcativo como um navegador, um cliente de RSS,
mas pode também ser um
servidor de cache ou um proxy em uma empresa de telecomunicações,
servidores que também são clientes.

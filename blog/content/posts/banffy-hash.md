+++
date = '2025-04-24T23:21:00-03:00'
draft = false
title = 'Bánffy e o hash criptográfico'
tags = ['senhas', 'criptografia', 'causo']
+++

Meu amigo Ricardo Bánffy
trabalhou comigo
no **Brasil Online**, o 1º portal da Abril na Web,
inaugurado em abril de 1996, um pouco antes do UOL (e uns 5 anos antes
do Webmail "BOL" que reaproveitou o domínio `bol.com.br`).

Entre os primeiros usuários do **Brasil Online** havia uns tantos
"VIPs": executivos de mídia, publicitários, e outras
pessoas que a Abril queria agradar.
Um desses VIPs esqueceu a senha e pediu para sua assistente
ligar para a Abril para recuperá-la.
O recado chegou até o meu chefe, Antonio Machado, que pediu para eu resolver.
Passei a bola para o Bánffy.

O usuário VIP estava irritado porque o nosso suporte técnico
havia dito que era impossível recuperar a
senha, e ele achava que era má vontade:
como podíamos autenticar um
login sem saber a senha?

Na verdade, a gente armazenava um hash criptográfico da
senha, por isso era inviável reconstruir a senha.[^1]

Como explicar para o cliente o que isso significa?

Bánffy fez essa analogia:

> Imagine que quando o usuário cria a conta, a gente anota a senha num pedaço de
> papel, queima o papel, e guarda as cinzas numa caixa de fósforos.
> Depois, quando o usuário digita o login e a senha, a gente pega essa
> senha, queima, e compara as cinzas com as que temos na caixa de
> fósforos. Assim a gente consegue dizer se as senhas eram iguais, mas
> não temos como reconstruir a senha a partir das cinzas.[^2]

Com essa estória o Bánffy convenceu a assistente que o patrão irritado teria mesmo
que seguir o procedimento normal para criar uma nova senha.

[^1]: Na época usávamos um hash MD5 com sal. Hoje não é mais recomendado usar MD5 para este fim.
Existem [funções de derivação de
senha](https://en.wikipedia.org/wiki/Key_derivation_function) especializadas para este caso de uso.

[^2]: Essa não é uma citação literal, mas é assim que eu lembro.
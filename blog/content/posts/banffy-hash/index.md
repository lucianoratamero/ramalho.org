+++
date = '2025-04-24T23:21:00-03:00'
draft = false
title = 'Bánffy e o hash criptográfico'
tags = ['senhas', 'criptografia', 'causo']
+++

<img src="/posts/banffy-hash/banffy-lr-dublin.jpg" width="{{< width >}}"
alt="Ricardo Bánffy e Luciano Ramalho em Dublin, durante a EuroPython 2022, 26 anos depois desse causo.">

Entre os primeiros usuários do
[Brasil Online](https://pt.wikipedia.org/wiki/Brasil_Online) havia uns tantos
"VIPs": executivos de mídia, publicitários, e outras
pessoas que a Abril queria agradar.
Um desses VIPs esqueceu a senha e pediu para sua assistente
ligar para a Abril para recuperá-la.
O recado chegou até o meu chefe, Antonio Machado, que pediu para eu resolver.

O usuário VIP estava irritado porque o nosso suporte técnico
havia dito que era impossível recuperar a senha, e ele achava que era má vontade:
como podíamos autenticar um login sem saber a senha?
Na verdade, a gente armazenava um hash criptográfico da
senha, por isso era inviável reconstruir a senha.[^1]

Passei o pepino para meu amigo, o engenheiro de software
[Ricardo Bánffy](https://www.linkedin.com/in/ricardobanffy/).
O desafio era apaziguar com educação.

E o Bánffy educou com essa analogia:

> Imagine que quando o usuário cria a conta, a gente anota a senha num pedaço de
> papel, queima o papel, e guarda as cinzas numa caixa de fósforos.
> Depois, quando o usuário digita o login e a senha, a gente anota essa
> senha, queima o papel, e compara as cinzas com as que temos na caixa de
> fósforos. Assim a gente consegue dizer se as senhas eram iguais, mas
> não temos como reconstruir a senha a partir das cinzas.[^2]

Assim o Bánffy convenceu a assistente que o patrão irritado teria mesmo
que seguir o procedimento normal para criar uma nova senha.[^3]


[^1]: Na época usávamos um hash MD5 com sal.
Hoje MD5 não é mais recomendado.
Existem [funções de derivação de
senha](https://en.wikipedia.org/wiki/Key_derivation_function)
especializadas para este caso de uso.

[^2]: Essa não é uma citação literal, mas é assim que eu lembro.

[^3]: Mistérios que Bánffy e eu nunca resolvemos: Porque a
pessoa estava tão apegada a uma senha que ela nem lembrava qual era?
Qual a utilidade de resgatar a senha esquecida em vez de criar uma nova?
Minha hipótese: gente poderosa gosta de exercitar poder,
e não aceita situações onde seu desejo não pode ser atendido.

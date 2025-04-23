+++
date = '2025-04-23T00:19:50-03:00'
draft = false
title = 'O erro fatal das applets Java'
tags = ['tecnologia']
+++

Em 1995 eu e um time excelente de jornalistas, designers e programadores na Abril S/A estávamos criando o
Brasil Online, o `bol.com.br` na sua primeira fase
(eu registrei esse domínio para a Abril;
anos depois foi reutilizado para o serviço de e-mail grauito do UOL).

A tecnologia de [applets Java](https://pt.wikipedia.org/wiki/Applet_Java)
era novidade.
Era tentador usar, porque o JavaScript a API do DOM eram
muito limitadas para fazer componentes interativos na página.

Acabamos nunca usando nas páginas principais do BOL.
Muita gente atribui o fracasso das applets à lentidão.
Realmente, elas demoravam para carregar e começar a funcionar.
Só que em 1995, tudo era muito lento na Web:
até carregar GIFs demorava.
Usávamos modems discados com banda de 28.8 Kbps
(hoje uma banda larga comum de 300 Mbs é 10417 vezes mais rápida).

Na real, o que inviabilizou usar applets no BOL não foi a lentidão.

Foi uma falha grave de interface:
antes da applet começar a funcionar,
os navegadores exibiam um retângulo cinza no lugar da applet.
Isso inevitavelmente parecia um defeito no design.
Era inaceitável porque a Abril era conhecida pela
excelente qualidade gráfica das suas publicações.

Poderia ter sido diferente...

O tag para incluir uma applet era assim:

```
<APPLET code=AnalogClock width=100 height=100></APPLET>
```

Era possível definir as dimensões do retângulo da applet,
mas não a cor. Ficava sempre cinza, até a applet
carregar e pintar o fundo de outra cor.

Se o tag `<APPLET ...>` aceitasse um parâmetro de cor,
não pareceria defeito, e talvez a gente tivesse colocado
applets na home e outras páginas importantes do site.

Faltou sensibilidade visual para os engenheiros da Sun
que inventaram a tecnologia da applet.

Quantos bilhões esse erro pode ter custado para a Sun e para a Oracle?
Se fosse possível pintar o espaço da applet de qualquer cor,
talvez o Java no navegador tivesse durado muito mais,
e o [Flash](https://pt.wikipedia.org/wiki/Adobe_Flash) nem tivesse existido. 
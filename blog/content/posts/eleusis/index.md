+++
date = '2025-04-26T18:03:20-03:00'
draft = false
title = 'Eleusis: um jogo de raciocínio indutivo'
tags = ['jogos', 'baralho']
toc = true
+++

Eleusis é um jogo de cartas que exercita o
[método indutivo](https://pt.wikipedia.org/wiki/M%C3%A9todo_indutivo)
característico da ciência.
A partir de experimentos e observações, os jogadores precisam
formular hipóteses sobre uma Regra Divina.

O jogo foi criado pelo inventor de jogos
[Robert Abott](https://en.wikipedia.org/wiki/Robert_Abbott_(game_designer))
em 1956, e depois aperfeiçoado em colaboração com
Martin D. Kruskal e John Jaworski até a versão descrita aqui, chamada Novo
Eleusis, publicada em 1977.

Minha referência foi o livro Jogos de Cartas, da coleção Todos os Jogos da Abril,
de onde vieram muitas frases neste texto.

## Objetivos

* Marcar pontos livrando-se de todas as suas cartas antes dos demais jogadores.
* Para o jogador no papel de "Deus": escrever uma regra secreta
que algumas pessoas descubram e outras não, para maximizar sua pontuação.


## Participantes

* Mínimo: 4.
* Ideal: 5 ou 6.
* Máximo: 8.

## Material

* 3 baralhos comuns (iguais);
* mesa grande (ou baralhos pequenos);
* lápis e papel para marcar pontos e registrar as Regras Divinas.

## Visão geral

Uma partida é formada por várias mãos.

A cada mão os jogadores recebem novas cartas,
e um jogador diferente faz o papel de Deus.

O Deus:

1. Escreve uma Regra Divina, sem revelar para nenhum jogador.
2. Embaralha o monte e distribui 14 cartas para cada jogador (mas não para si).
3. Abre uma carta do monte para iniciar a fila principal.

Para decidir quem começa, use o valor da carta inicial para 
contar os jogadores em sentido horário a partir do Deus (e pulando ele).

> ✋ **Importante** Quando se usam valores numéricos nas regras,
o Ás vale 1, o Valete (J) vale 11, a Dama (Q) vale 12 e o Rei (K), 13.
As outras cartas valem pelo seu próprio número.

Seguindo em sentido horário, cada jogador na sua vez apresenta uma carta
(ou mais de uma, como veremos depois).

* Se a carta atende à Regra Divina, Deus responde "Sim" e coloca a carta na fila principal.

* Se a carta não atende a Regra Divina, Deus responde "Não", coloca a carta na columa de erros,
e dá duas cartas do monte para o jogador como penitência.

> ✋ **Importante**: Deus nunca justifica suas decisões. Apenas diz "Sim" ou "Não".


## Exemplo 1: início da mão

{{< figure
  src="fila-ate03.png"
  alt="Início de uma mão de Eleusis"
  link="fila-ate03.png"
  caption="Início de uma mão de Eleusis. Clique para ampliar."
  width=800
>}}

Na figura acima, a Regra Divina é:

> Se a carta anterior for preta, jogue 7 ou maior.
Se a carta anterior for vermelha, jogue 6 ou menor. 

As três primeiras jogadas foram:

1. Deus inicia a fila principal colocando o 3 de copas.
Isso determina que o primeiro jogador será o jogador 3,
contando a partir do Deus em sentido horário.
2. Jogador 3 abre um 8 de copas.
Deus diz "Não", coloca o 8 de copas na primeira coluna de erros.
Como "penitência", o jogador 3 recebe mais duas cartas do monte.
3. Jogador 4 abre um 5 de paus.
Deus diz "Sim" e a carta é colocada na fila principal.


## Jogadas múltiplas

Um jogador que pensa ter descoberto a Regra Divina tem duas formas
de se livrar de várias cartas de uma vez.

* Declarar que não tem cartas.
* Apresentar uma sequência de cartas.


### Declarar "não tenho cartas"

Quando um jogador pensa que descobriu a Regra Divina, mas não tem nenhuma
carta que sirva para jogar, ele declara que não tem cartas e abre na mesa
todas as cartas que tem na mão.

* Se Deus confirmar que nenhuma carta serve:

  * Se o jogador tem 4 cartas ou menos, Deus recolhe as cartas do jogador.
    O jogador bateu, e a mão termina.

  * Se o jogador tem 5 ou mais cartas, Deus recolhe as cartas do jogador,
    embaralha com o resto do monte, e devolve para o jogador 4 cartas a menos
    do que ele tinha. Ex: se tinha 6 cartas na mão, o jogador recebe 2 de volta.
    Nesse caso a mão continua com o próximo jogador.

* Se houver uma ou mais cartas válidas na mão do jogador,
  Deus pega apenas uma das cartas válidas e coloca na fila principal.
  Como penitência, o jogador recebe 5 novas cartas do monte, além
  de ficar com as que já tinha.


### Apresentar uma sequência

Um jogador está confiante de saber a Regra Divina 
pode baixar uma sequência de até 4 cartas de uma vez.
A ordem das cartas é importante, mas elas devem ser apresentadas
juntas para serem julgadas pelo Deus como um conjunto.

* Se todas as cartas da sequência estão certas e na ordem certa,
Deus responde "Sim" e a sequência é colocada na fila principal,
como se fossem jogadas sucessivas.

* Se uma ou mais cartas da sequência está errada, ou a ordem está errada,
Deus responde "Não" e coloca na coluna de erros
a sequência com as cartas sobrepostas, para indicar que a sequência foi rejeitada
como um todo, mesmo que tenha alguma carta certa.
Como penitência, o jogador recebe o dobro de cartas do monte.

> ✋ **Importante**: Deus não deve apontar qual
a carta errada em uma sequência, apenas diz "Sim" ou "Não"
para a sequência inteira.


#### Exemplo 2: sequência com carta errada

{{< figure
  src="fila-ate12.png"
  alt="Sequência com uma carta errada: o valete de paus."
  link="fila-ate03.png"
  caption="Sequência com uma carta errada: o valete de paus. Clique para ampliar."
  width=800
>}}

Na figura acima, considere a mesma Regra Divina do
[Exemplo 1](#exemplo-1-início-da-mão).
No momento a última carta da fila principal é um rei de copas.

Um jogador apresenta uma sequência de 3 cartas:
4 de espadas, 9 de ouros, valete de paus.

O Deus rejeita a sequência com um "Não", sem especificar qual carta está errada.
Neste caso, 4 e o 9 estão corretos, mas o valete está errado
(depois de carta vermelha tem que ser 6 ou menor).

A sequência errada é colocada na coluna de erros como um grupo,
e o jogador recebe 6 cartas de penitência.

## Fim de uma mão

Uma mão de Eleusis pode terminar de duas maneiras:

1.  Quando alguém consegue bater (jogar todas as suas cartas).
2.  Quando todos os jogadores são eliminados por erro.


### Eliminação por erro

Após 30 cartas na mesa—certas ou erradas—cada jogador
que errar é eliminado da mão.
O jogador recebe as cartas de penitência e espera
até acabar a mão, mantendo suas cartas para a contagem de pontos.

Recomenda-se colocar-se um marcador na 30ª carta (contando-se as cartas
tanto da fileira principal como das colunas de erros),
para lembrar a todos que, a partir desse momento, quem errar será eliminado.


### Contagem de pontos de uma mão

Para contar pontos, determine a maior quantidade de cartas que sobrou na mão de um jogador.
Vamos chamar esse número de `Max`.

* Se um jogador bateu, ele marca `Max + 4` pontos.
* Demais jogadores ganham `(Max - N)` pontos, onde `N` é a quantidade de cartas na mão desse jogador.
Isso significa que o jogador que micou com mais cartas marca 0.
* O Deus ganha a mesma quantidade de pontos que o jogador que fez mais pontos.


### Exemplo de pontuação de uma mão

| Pessoa         | Cartas | Pontos | Explicação  |
|:------:|------:|------:|------------|
| **jogador 1**  |      8 | 0      | micou com mais cartas que todos (`Max = 8`)|
| **jogador 2**  |      3 | 5      | diferença: `Max - 3 = 5`   |
| **jogador 3**  |      0 | 12     | bateu, diferença + bônus: `Max + 4 = 12` |
| **Deus**       |  -     | 12     | o mesmo que **jogador 3** |


## Fim do jogo

Uma partida completa de Eleusis tem tantas mãos quanto for o
número de jogadores, para garantir que cada pessoa seja Deus uma vez.

Quando isso não for possivel, some 10 pontos na contagem final 
de cada pessoa que não foi Deus.
É uma compensação, porque o Deus faz mais pontos que a média.


## Regras sobre a Regra Divina

> ✋ **Importante**: A Regra Divina só pode se
referir às cartas da fileira principal.
Não pode se referir a cartas fora da fileira principal,
muito menos aspectos alheios ao jogo.
Por exemplo, não vale uma regra que obriga a descartar
um Ás se o jogador só tiver uma carta na mão,
ou uma regra que proíbe barbudos de jogar cartas vermelhas.

A Regra Divina deve ser redigida cuidadosamente para evitar
dúvidas em sua interpretação.
No final da mão, o Deus é obrigado a apresentá-la,
e os jogadores podem conferir as decisões.


### Dicas divinas

Fica a critério de Deus dar ou não dar dicas sobre a regra antes de
iniciar a mão. Por exemplo, pode dizer: "a regra não envolve naipes"
ou "a é sobre números".
Mas, uma vez iniciada a mão, Deus não pode dar mais nenhuma ajuda.


### Escolha da carta inicial

Ao tirar uma carta do baralho,
o Deus pode decidir que ela não é adequada à regra que ele concebeu
(por exemplo, a regra proíbe cartas pares, mas a carta é um 4).
Nesse caso ele deve colocá-la novamente no baralho,
embaralhar e retirar outra carta, até encontrar uma carta que sirva. 


### Exemplos de regras boas

Três exemplos de regras que não muito complicadas.
Regras assim tendem a dar pontos para o Deus do que regras
complicadas demais.

* Se a carta anterior for espadas, jogue ouros;
se for ouros, jogue paus; se for paus, jogue copas; se for copas, jogue
espadas (ciclo ♠→♦→♣→♥)

* A cada carta ímpar preta, deve seguir-se
uma carta par vermelha.

* Se a carta anterior for preta, jogue 7 ou
maior. Se a carta anterior for vermelha, jogue 6 ou menor. (Essa é a regra
adotada no [diagrama exemplo](eleusis#o-jogo).)

Como o objetivo do jogo é livrar-se das cartas o mais cedo possivel,
e a pontuação de Deus é a diferença de pontos entre o melhor e o
pior jogador da mão, a regra não é
muito fácil, nem muito difícil, de modo que alguns jogadores possam
descobrí-la mais rapidamente que outros.

Essa caracteristica evita que o Deus torne o jogo monótono e frustrante,
elaborando regras dificílimas que ninguém descobriria.


### Uma regra problemática

Eis uma regra problemática:

> 👎 A cada duas cartas pretas ímpares, deverá seguir-se uma carta vermelha
par e uma figura (Rei, Dama ou Valete).

Os problemas:

*   Alta dificuldade por se referir a duas cartas anteriores, e dois
    atributos delas (preta, ímpar)—as regras mais simples levam em conta
    apenas a carta anterior, e apenas um atributo (cor, naipe ou
    número).
*   Alta dificuldade ao impor limitações sobre duas cartas
    posteriores—regras mais simples limitam apenas a próxima carta.
*   Ambiguidade: não fica claro se é possível atender os dois requisitos
    de "carta vermelha e figura" com apenas uma carta, se for jogada
    uma Dama vermelha (valor 12, portanto par), ou se a regra se aplica
    sempre a duas cartas posteriores.

Resolvida essa ambiguidade, essa seria uma regra válida, mas
provavelmente muito difícil e teria pouco valor para
Deus, que marca poucos pontos quando nenhum jogador consegue desvendar a
regra (porque todos são elimitados).

### Dicas para o Deus

Robert Abbott afirma que as principais caracteristicas de um Deus são
uma avaliação correta da capacidade dos demais jogadores e a
sensibilidade para criar um tipo de regra que lhe assegure bom número de
pontos.

Nesse sentido, ele afirma que as regras que incluem apenas
cerca de ¼ das cartas do baralho, a qualquer altura do jogo, tendem a
ser mais fáceis do que as que incluem mais da metade das cartas de um
baralho.


## Regra opcional avançada: "o Profeta"

> 👉 **Dica**: Recomendamos que vocé só jogue com o
Profeta apos ter experimentado o Eleusis básico.
Os procedimentos e a contagem de pontos ficam bem mais complicadas quando há um Profeta.

Quando um jogador acha que já descobriu a regra, pode declarar-se
Profeta e assumir as funções do Deus, passando a julgar as cartas
lançadas à mesa e a punir os outros jogadores, dando-lhes mais cartas,
quando jogarem errado. Um Profeta bem-sucedido pode marcar mais pontos
que o próprio Deus.

Um jogador pode declarar-se Profeta quando tiver acabado de jogar (certo
ou errado) e antes que o jogador seguinte faça a sua jogada, desde que
existam estas três condições:

1.  Não há um outro Profeta;
2.  Esse jogador ainda não foi Profeta nessa mão;
3.  Ainda restam na mão pelo menos dois jogadores, além do Deus e
    daquele que se declara Profeta.

> ✋ **Importante**: Quando um jogador se declara Profeta
é preciso marcar a última carta jogada por ele com um objeto qualquer,
como uma peça de Xadrez.

O Profeta continua com as cartas que tinha,
mas não abaixará cartas enquanto for Profeta.
Suas cartas devem ficar à parte, até que ele seja
declarado Falso Profeta ou a mão termine.
No fim da mão suas cartas
serão importantes para a contagem de pontos.

O Deus passa para o Profeta o monte usado para punir lances errados
dos outros jogadores.

A partir de agora, quando um jogador apresenta carta(s),
é o Profeta diz "sim" ou "não".
Daí o Deus considera sua Regra Divina e
afirma "certo" ou "errado" em relação ao julgamento do Profeta. 

Se o Deus disser "errado", o Profeta é declarado na hora Falso
Profeta, e o outro objeto que marcava o inicio de suas
atividades é retirada.
Como penalidade, o Falso Profeta não poderá mais
ser Profeta naquela mão.

> Segundo Robert Abbott, criador do Eleusis,
"o Profeta é o cientista que divulga suas idéias, e o Falso Profeta, um
cientista precipitado". A derrubada do Profeta é um dos fatos mais
divertidos do jogo.

Com a queda do Profeta, o Deus reassume seu papel e completa a jogada
que derrubou o Profeta, colocando a carta ou a sequência de cartas
apresentada pelo último jogador na fileira principal ou em uma coluna de
erros. É importante frisar que se essas cartas forem erradas e o
Profeta tiver dito que eram certas, quem as jogou não é castigado.
O objetivo desta exceção é incentivar os jogadores a derrubar o Profeta,
jogando cartas erradas de propósito,
para conferir se o Profeta sabe realmente a Regra Divina.

Quando há Profeta e um jogador alega não ter cartas para jogar, pode
ocorrer:

1.  O profeta diz "sim" e o Deus confirma: "certo". O jogo segue
    normalmente.
2.  O Profeta diz "sim" e o Deus desaprova dizendo "errado". O
    Profeta cai e passa o baralho para o Deus, continuando o jogo
    normalmente. (Este é outro caso em que o jogador que errou não é
    punido.)
3.  O Profeta diz "não" e o Deus desaprova dizendo "errado" — ou
    seja, o jogador está certo. Nesse caso, cai o Profeta e o Deus dá
    prosseguimento ao jogo.
4.  O Profeta diz "não" e o Deus aprova dizendo "certo". Portanto, o
    jogador errou. O Profeta deve retirar uma das cartas apresentadas e
    coloca-la na fileira principal. Mas, se ao tirar essa carta, o
    Profeta errar, ele será imediatamente declarado Falso Profeta. Deus,
    que reassume suas funções, tirando uma carta correta do jogador e
    colocando-a na fila principal, mas sem castigar o jogador que errou.

Havendo Profeta, a eliminação de jogadores por motivo de erro acontece a
partir da 21ª carta jogada após a entrada do Profeta no jogo (daí a
importância de se marcar a entrada do Profeta).
Por isso é conveniente marcar também a 20ª
carta a partir da entrada do Profeta.

> ✋ **Importante**: Quando o Profeta é derrubado,
retira-se também o objeto que marcava sua ascensão.

Uma mão de Eleusis prossegue normalmente havendo ascensão e queda de
Profetas, mesmo que algum jogador já tenha sido eliminado.

### Pontuação do Profeta

O Profeta bem-sucedido—que não é derrubado até o final da
mão—marca pontos assim:

1. Diferença entre a quantidade de cartas da sua mão e quem tinha mais cartas (`Max`), MAIS
2. Número de cartas na fila principal desde que virou Profeta, MAIS
3. Duas vez o número de cartas nas colunas de erros desde que virou Profeta.

#### Exemplo:

* Profeta tinha 6 cartas na mão, Juca micou com 14: 8 pontos para o Profeta.
* 9 cartas na fila principal desde que virou Profeta: 9 pontos.
* 11 cartas nas colunas de erro desde que virou Profeta: 11 * 2 = 22 pontos

Total: 8 + 9 + 22 = 39

### Pontuação do Deus quando há Profeta

Quando existe Profeta ao final da mão,
o algoritmo para se pontuar Deus é assim:

1.  Vamos chamar de `P` os pontos marcados pelo jogador que fez o maior
    número de pontos (pode ser o Profeta).
2.  Conte a quantidade de cartas (certas e erradas) que antecedem a
    ascensão do Profeta e multiplique por 2. Vamos chamar
    de `A` o resultado dessa operação.
3.  Deus receberá o será o menor valor entre `P` e `A`

#### Exemplo:

* O Profeta foi o jogador que marcou mais pontos: `P = 39`

* Antes da ascenção do Profeta havia 14 cartas na mesa
(fila principal e colunas de erros), então:<br> `A = 14 × 2 = 28`

* Deus recebe 28 pontos: `min(P, A)`

> 👉 **Dica**: O Profeta é o único jogador que pode marcar mais pontos que
Deus em uma mão. E a diferença aumenta quando mais cedo o Profeta se declarar.


### Exemplo: contagem geral de pontos com Profeta

Para ilustrar a contagem de pontos do Eleusis, jogado com Profeta, damos
a seguir um exemplo com 5 participantes.

* Luis foi o Deus.
* A mão terminou quando Mario bateu.
* Rui terminou com 14 cartas
* Ana micou com 17 cartas na mão.
* Clara foi uma Profeta bem-sucedida; quando se declarou Profeta tinha 9 cartas na mão; havia 19 cartas na mesa até então.

Ao final dessa mão, a pontuação ficou assim:

| Pessoa     |Cartas |Pontos | Explicação |
|:----------:|------:|------:|------------|
| **Ana**    | 17    | 0     | Micou com a maior quantidade de cartas. `Max = 17` |
| **Rui**    | 14    | 3     | `Max` menos 14 (suas cartas). |
| **Mario**  | 0     | 21    | Bateu: ganha 4 pontos de bônus + `Max`. |
| **Clara**  | 9     | 42    | `Max` menos 9 (suas cartas) mais bônus de cartas jogadas no período em que foi Profeta: 12 cartas na fileira principal e 11 nas colunas de erros:<br>`8 + 12 + (11 × 2) = 42` |
| **Luis** (Deus)  | -     | 38    | O maior número de pontos na mão foi 42. <BR>Antes de Clara virar Profeta, havia 19 cartas na mesa: `19 × 2 = 38`<br>A pontuação do Deus é o menor entre 42 e 38.|

+++
date = '2025-04-26T18:03:20-03:00'
draft = true
title = 'Eleusis: um jogo de raciocínio indutivo'
tags = ['jogos', 'baralho']
+++

Eleusis é um jogo de cartas que exercita o
[método indutivo](https://pt.wikipedia.org/wiki/M%C3%A9todo_indutivo)
característico da ciência.
A partir de experimentos e observações, os jogadores precisam
formular hipóteses sobre uma Regra Divina.

O jogo foi criado por Robert Abott em 1956, e depois aperfeiçoado em colaboração com
Martin D. Kruskal e John Jaworski até a versão definitiva, chamada Novo
Eleusis, publicada em 1977. As regras a seguir são do Novo Eleusis.


## Participantes

Mínimo: 4.
Ideal: 5 ou 6.
Máximo: 8.

## Material

* 3 baralhos comuns (iguais);
* mesa grande (ou baralhos pequenos);
* lápis e papel para marcar pontos e registrar as Regras Divinas.

## Visão geral

Uma partida é formada por várias mãos.

A cada mão os jogadores recebem novas cartas,
e um jogador diferente faz o papel de Deus

O Deus:

1. Escreve uma Regra Divina, sem revelar para nenhum jogador.
2. Embaralha o monte e distribui 14 cartas para cada jogador (mas não para si).
3. Abre uma carta do monte iniciar a fila principal.

Em sentido horário, cada jogador na sua vez abaixa uma carta.

* Se a carta atende à Regra Divina, Deus responde "Sim" e coloca a carta na fila principal.

* Se a carta não atende a Regra Divina, Deus responde "Não", coloca a carta na columa de erros,
e dá duas cartas do monte para o jogador como penitência.

### Objetivos

* Marcar pontos livrando-se de todas as suas cartas antes dos demais jogadores.

* Para o Deus: escrever uma Regra Divina que algumas pessoas descubram e outras não,
maximizando os pontos de quem bateu, e assim maximizar sua propria pontuação.

### Exemplo 1

Na figura abaixo, a Regra Divina é:

> Se a carta anterior for preta, jogue 7 ou maior.
Se a carta anterior for vermelha, jogue 6 ou menor. 

{{< figure
  src="fila-ate03.png"
  alt="Início de uma mão de Eleusis"
  link="fila-ate03.png"
  caption="Início de uma mão de Eleusis. Clique para ampliar."
  width=800
>}}

As três primeiras jogadas foram:

1. Deus inicia a fila principal colocando o 3 de copas.
2. Jogador 1 abre um 8 de copas.
Deus diz "Não", coloca o 8 de copas na primeira coluna de erros.
Como "castigo", jogador #1 recebe mais duas cartas do monte.
3. Jogador 2 abre um 5 de paus. Deus diz "Sim" e a carta é colocada na fila principal.ß

## Final de uma mão

Uma mão de Eleusis pode terminar de duas maneiras:

1.  Quando alguém consegue bater (jogar todas as suas cartas).
2.  Quando todos os jogadores são eliminados por erro.

### Eliminação por erro

Após terem sido jogadas 30 cartas—certas ou erradas—cada jogador
que errar é eliminado da mão.
O jogador recebe as cartas de castigo e espera
até acabar a mão, mantendo suas cartas para a contagem de pontos.

Recomenda-se colocar-se um marcador na 30ª carta (contando-se as cartas
tanto da fileira principal como das colunas de erros), para que todos
saibam que, a partir desse momento, quem errar será eliminado.

### Contagem de pontos de uma mão

Para contar pontos, determine a maior quantidade de cartas que sobrou na mão de um jogador.
Vamos chamar esse número de `Max`.

* Se um jogador bateu, ele pontua `Max + 4` pontos.
* Demais jogadores ganham `(Max - N)` pontos, onde N é a quantidade de cartas na mão desse jogador.
Isso significa que o jogador que micou com mais cartas marca 0 ponto.
* O Deus ganha a mesma quantidade de pontos que o jogador fez mais pontos.


### Exemplo de pontuação de uma mão

| Pessoa         | Cartas na mão | Pontos Ganhos| Explicação  |
|----------------|--------|--------|-------------|
| **jogador 1**  |      8 | 0      | micou com mais cartas que todos (`Max = 8`)|
| **jogador 2**  |      3 | 5      | diferença: `Max - 3 = 5`   |
| **jogador 3**  |      0 | 12     | bateu, diferença + bônus: `Max + 4 = 12` |
| **Deus**       |  -     | 12     | o mesmo que **jogador 3** |


## Regras sobre a Regra Divina

Antes de distribuir as cartas, o Deus deve inventar a Regra Divina,
registrá-la por escrito, e guardá-la.
No final da mão, o Deus é obrigado a apresentá-la, e os jogadores
podem conferir as decisões.
A regra deve ser redigida cuidadosamente para evitar
dúvidas em sua interpretação.

A seguir, três exemplos de boas regras:

> Se a carta anterior for espadas, jogue ouros;
se for ouros, jogue paus; se for paus, jogue copas; se for copas, jogue
espadas (ciclo ♠→♦→♣→♥)

> A cada carta ímpar preta, deve seguir-se
uma carta par vermelha.

> Se a carta anterior for preta, jogue 7 ou
maior. Se a carta anterior for vermelha, jogue 6 ou menor. (Essa é a regra
adotada no [diagrama exemplo](eleusis#o-jogo).)

Quando se usam valores numéricos nas regras, o Ás vale 1, o Valete (J) vale
11, a Dama (Q) vale 12 e o Rei (K), 13. As outras cartas valem pelo seu próprio
número.


> ✋ **Importante**: A Regra Divina só pode se
referir às cartas da fileira principal.
Não pode se referir a cartas fora da fileira principal,
muito menos aspectos alheios ao jogo.
Por exemplo, não vale uma regra que obriga a descartar
uma carta ímpar se o jogador só tiver uma carta na mão,
ou uma regra que proíbe barbudos de jogar cartas vermelhas.

Como o objetivo do jogo é livrar-se das cartas o mais cedo possivel,
e a pontuação de Deus é a diferença de pontos entre o melhor e o
pior jogador da mão, a regra não é
muito fácil, nem muito difícil, de modo que alguns jogadores possam
descobrí-la mais rapidamente que outros.

Se não fosse essa caracteristica do jogo, Deus poderia
torná-lo monótono e frustrante, elaborando regras dificílimas que
ninguém descobriria.

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
regra (porque todos são elimitados, como veremos a seguir)

### Dicas divinas

Fica a critério de Deus dar ou não dar dicas sobre a regra antes de
iniciar a mão. Por exemplo, pode dizer: "a regra não envolve naipes"
ou "a é sobre números".
Mas, uma vez iniciada a mão, Deus não pode dar mais nenhuma ajuda.


### Exemplos de jogadas


{{< figure
  src="eleusis-exemplo.png"
  alt="Exemplo de partida de Eleusis em andamento"
  link="eleusis-exemplo.png"
  caption="Exemplo de partida de Eleusis em andamento. Clique para ampliar."
  width=800
>}}

No diagrama, note que há uma fileira horizontal
acima e algumas verticais, abaixo dela.
A fileira horizontal é a fileira principal,
formada pelas cartas certas conforme a Regra Divina,
e as fileiras verticais, chamadas de colunas dos erros,
são formadas pelas cartas erradas.

Cabe a Deus inaugurar a fileira principal com a carta inicial.
Ao tirar uma carta do baralho, o Deus pode decidir que ela não
é adequada à regra que ele concebeu (por exemplo, a regra proíbe
cartas pares, mas a carta é um 4).
Nesse caso ele deve colocá-la novamente no baralho, embaralhar e retirar
outra carta, até encontrar uma carta que sirva.
Essa é a única vez que Deus abre alguma carta sobre a mesa.
A partir de então, ele se limitará a aprovar os acertos, apontar os erros,
e distribuir cartas como penalidades para os jogadores que errarem.

O jogo desenvolve-se sempre no sentido horário, isto é, de Deus para os
jogadores a sua esquerda. Para determinar quem será o primeiro a jogar,
Deus conta o número indicado pela carta inicial, a partir do jogador a
sua esquerda, pulando a si mesmo quando completar uma volta. Ou seja, se
a primeira carta for um 8: para saber quem jogara primeiro, Deus conta
os jogadores, a partir do jogador a sua esquerda, até o número 8. O
jogador assim indicado começará a mão.

Em sua vez de jogar, cada participante escolhe uma das cartas que tem
na mão e apresenta a Deus.
Se a carta estiver correta, será colocada após a última carta da fileira principal.
Se a carta for incorreta, será colocada abaixo da última carta da fileira principal, iniciando ou aumentando uma coluna de erros.

Um jogador pode descartar uma carta, ou uma sequência de no máximo 4
cartas, ou então declarar que não tem como jogar, como veremos adiante.
Em qualquer um desses casos o jogador só pode fazer uma consulta a
Deus, mesmo que abaixe uma sequência.

Quando o jogador apresenta uma carta errada, recebe de Deus 2
cartas do baralho fechado.
Se apresentar uma sequência de 2 cartas com
uma ou ambas erradas, receberá 4 cartas do baralho; se apresentar uma
sequência de 3 cartas em que haja pelo menos uma carta errada,
receberá 6 cartas do baralho; e assim por diante.
Portanto, basta haver uma carta
incorreta na sequência para invalidá-la, e quando o jogador comete um
erro, sempre recebe do Deus o dobro
do número de cartas que apresentou.

Após um sim ou um não do Deus, a vez passa ao jogador seguinte.

> ✋ **Importante**: Deus nunca descreve o erro nem aponta qual
a carta errada em uma sequência, apenas diz "sim" ou "não".

Por exemplo, um jogador acredita que descobriu a regra e resolve
apresentar a Deus uma sequência de 4 cartas de uma vez.
Caso a sequência esteja correta, Deus dirá apenas sim.
Mas, se uma ou mais cartas da sequência forem erradas,
ou se todas forem certas porém na ordem errada,
Deus diz apenas não e coloca as cartas na coluna de erros.

A sequência incorreta deve ser colocada na coluna de erros com as cartas
parcialmente superpostas, para indicar que se trata de uma sequência.
Essa disposição está ilustrada na terceira coluna de erros do diagrama.

> ✋ **Importante**: Quando um jogador apresenta uma sequência,
ele não pode apresentar uma a uma as cartas que a compoem,
mas sim a sequência completa de uma só vez.

### Exemplo

{{< figure
  src="eleusis-exemplo.png"
  alt="Exemplo de partida de Eleusis em andamento"
  link="eleusis-exemplo.png"
  caption="Exemplo de partida de Eleusis em andamento. Clique para ampliar."
  width=800
>}}


Para facilitar a compreensão do jogo, acompanhe a sequência de jogadas
pelo diagrama acima.

Nesse exemplo, a regra é:

> Se a carta anterior for preta, jogue 7 ou maior.
Se a carta anterior for vermelha, jogue 6 ou menor.

Deus colocou o 3 de Copas como carta inicial. O primeiro jogador
tentou jogar um 8 de Copas, e errou. Por isso, a sua carta foi para
baixo da carta inicial, inaugurando a primeira coluna de erros.

O segundo jogador tentou o 5 de Espadas, e acertou.

O 9 de Ouros apresentado pelo jogador seguinte também está certo,
mas o Valete de Copas, jogado a seguir, está errado e, por isso,
oi colocado embaixo do 9 de Ouros, inaugurando a segunda coluna de erros.

A carta seguinte, o 7 de Ouros, também errada, foi colocada na coluna de erros, abaixo do Valete de Copas.
O mesmo aconteceu com próxima carta, um 8 de Espadas.

Na jogada seguinte do diagrama, um jogador acertou descartando o 5 de
Paus e o seguinte também teve sucesso com o Rei de Copas. Nesse momento,
o jogador seguinte pensou ter descoberto a regra, imaginando que ela
fosse simplesmente uma sequência de naipes: copas, espadas, ouros, paus,
copas e assim por diante. Realmente, observando as 5 primeiras cartas da
fileira principal, essa é uma hipótese viável, mas, no caso, era apenas
coincidência. Contudo, o jogador equivocado precipitou-se e apressou-se
em descartar uma sequência de 3 cartas, formada por um 4 de Espadas, um
9 de Ouros e um Valete de Paus. Como o Valete de Paus estava errado,
toda a sequência é considerada incorreta e colocada abaixo do Rei de
Copas, numa coluna de erros. E, como se tratava de uma sequência,
isso é indicado sobrepondo as 3 cartas, para assinalar que foram
jogadas juntas naquela ordem, e não individualmente.
Como penalidade, esse jogador recebee 6 cartas.

No Eleusis faz mais pontos quem fica com menos cartas na mão. O caminho
da vitória, portanto, é desvendar a Regra Divina.
No início de uma mão são poucas as informações disponiveis,
e as cartas são jogadas quase aleatoriamente.
À medida que o jogo prossegue, as
cartas certas e erradas permitem elaborar hipóteses sobre
a regra.

### Jogada sem cartas corretas

Se um jogador acha que descobriu a Regra Divina, mas não tem nenhuma
carta correta para jogar, ele diz "não tenho cartas" e abre na mesa
todas as cartas que tem na mão.

Se Deus confirmar sua declaração, e se esse jogador tiver 4 cartas ou
menos, estas cartas são recolhidas pelo Deus e a mão termina.

Se o jogador tiver 5 ou mais cartas e se Deus confirmar que ele
realmente não tem cartas para jogar, Deus recolhe a mão do jogador,
embaralhando-as com o resto do monte.
Deus então, devolve ao jogador o número de cartas que ele tinha,
menos 4 cartas.
E a mão continua.

Supondo que o jogador tivesse 10 cartas na mão, Deus lhe daria
6 novas cartas do monte reembaralhado.

Se o jogador disser "não tenho cartas" mas na verdade tiver uma ou mais
cartas corretas, Deus pega apenas uma das cartas que servem e a coloca na
fileira principal. Como castigo, o jogador recebe 5 novas cartas, além
de ficar com as que já tinha.



### Final do jogo

Uma partida inteira de Eleusis é composta de tantas mãos quanto for o
número de jogadores—isto é, termina quando todos os jogadores tiverem
sido Deus uma vez. Quando isso não for possivel, procede-se da seguinte
maneira: ao somar os pontos das mãos, acrescente mais 10 para quem não
tiver sido Deus. É uma compensação, pois o Deus faz mais pontos do que a
média.

> 👉 **Dica:** Você pode parar aqui e jogar. O restante são regras e dicas opcionais.

## Algumas sugestões

Para jogar Eleusis o ideal é usar 3 baralhos completos,
embaralhados juntos, sem os curingas.

Também é bom usar uma mesa grande ou
cartas de tamanho menor do que o convencional,
uma vez que o jogo tende a se
alongar bastante na fileira principal e nas colunas verticais.
Alternativamente, considere jogar no chão.

Robert Abbott afirma que as principais caracteristicas de um Deus são
uma avaliação correta da capacidade dos demais jogadores e a
sensibilidade para criar um tipo de regra que lhe assegure bom número de
pontos.
Nesse sentido, ele afirma que as regras que abrangem apenas
cerca de ¼ das cartas do baralho, a qualquer altura do jogo, tendem a
ser mais fáceis do que as que abrangem mais da metade das cartas de um
baralho.


## Regras avançadas: "o Profeta"

> Recomendamos que vocé só jogue com o
Profeta apos ter aprendido o Eleusis básico. Os procedimentos e a
contagem de pontos ficam bem mais complicadas quando há um Profeta.

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
é preciso marcar a última carta jogada por ele.
Use um objeto qualquer, como uma peça de Xadrez.

O Profeta continua com as cartas que tinha, mas não abaixará cartas enquanto for
Profeta.
Suas cartas devem ficar à parte, até que ele seja
declarado Falso Profeta ou a mão termine.
No fim da mão suas cartas
serão importantes para a contagem de pontos.

O Deus passa para o Profeta o baralho usado para punir lances errados
dos outros jogadores.

Uma vez declarado o Profeta, o jogo continua sem o Profeta
ou Deus abaixarem cartas. Quando um jogador apresenta carta(s), o Profeta diz "sim" ou "não" enquanto o Deus, baseado em sua regra
secreta, afirma "certo" ou "errado" em relação ao julgamento do
Profeta.

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
erros. É importante frisar que se essas cartas nforem erradas e o
Profeta tiver dito que eram certas, quem as jogou não é castigado. O objetivo
desta exceção é incentivar os jogadores a derrubar o Profeta, jogando
cartas erradas de propósito, para conferir se o Profeta sabe realmente a
Regra Divina.

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
partir da 21ª carta jogada após a entrada do Profeta no jogo. (Daí a
importância de se marcar a entrada do Profeta no jogo).
Por isso é conveniente marcar também a 20ª
carta a partir da entrada do Profeta,
de modo que fique claro para todos
os jogadores que, a partir desse momento, o erro é punido com cartas
e eliminação do jogador dessa mão.

> ✋ **Importante**: Quando o Profeta é derrubado,
retira-se também o objeto que marcava sua ascensão.

Uma mão de Eleusis prossegue normalmente havendo ascensão e queda de
Profetas, mesmo que algum jogador já tenha sido eliminado.

O Profeta bem-sucedido—ou seja, que não é derrubado até o final da
mão—marca os pontos da diferença entre a quantidade de cartas da sua
mão e quem tinha mais cartas, e ainda tem direito a uma bonificação
correspondente ao número de cartas jogadas desde que virou Profeta: um
ponto para cada carta na fileira principal, e dois pontos para cada
carta nas colunas de erros.

Quando existe Profeta, há um pequeno algoritmo para se contar o número
de pontos do Deus:

1.  Vamos chamar de M os pontos marcados pelo jogador que fez o maior
    número de pontos (pode ser o Profeta).
2.  Conte a quantidade de cartas (certas e erradas) que antecedem a
    ascensão do Profeta e multiplica-se esse total por 2. Vamos chamar
    de A o resultado dessa operação.
3.  O número de pontos do Deus será o menor valor entre M e A.

> ✋ **Importante**: Quando há um Profeta bem-sucedido, o
número de pontos do Deus em uma mão pode ser menor, ou no máximo, igual ao
maior número de pontos marcados por um dos jogadores.

### Exemplo: contagem de pontos com Profeta

Para ilustrar a contagem de pontos do Eleusis, jogado com Profeta, damos
a seguir um exemplo dos pontos ganhos em uma mão da qual participaram 5
jogadores.

Luis foi o Deus, e a mão terminou quando Mario bateu (jogou todas
suas cartas). Clara foi uma Profeta bem-sucedida, e quando se declarou
Profeta tinha 9 cartas na mão. Rui terminou com 14 cartas e Ana com 17.

Ao final dessa mão, a situação de cada jogador ficou assim:

| Pessoa | Cartas na mão | Pontos ganhos | Explicação |
|--------|---------------|---------------|------------|
| Ana    | 17            | 0             | Micou com a maior quantidade de cartas ao final da mão. |
| Rui    | 14            | 3             | 17 (cartas de Ana) menos 14 (suas cartas). |
| Mario  | 0             | 21            | Bateu: ganha 17 (cartas de Ana) menos 0 (suas cartas) mais bônus de 4 por terminar sem cartas. |
| Clara  | 9             | 42            | 17 (cartas de Ana) menos 9 (suas cartas) mais bônus de cartas jogadas no período em que foi Profeta: 12 cartas na fileira principal e 11 nas colunas de erros: 12 + 11 × 2 = 34 |
| Luis   | -             | 38            | O maior número de pontos na mão foi 42. Mas antes de Clara virar Profeta, havia 19 cartas na mesa e 19 × 2 = 38. A pontuação do Deus é o menor desses dois números.|

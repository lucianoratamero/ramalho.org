+++
date = '2025-04-29T21:02:35-03:00'
draft = false
title = 'Dadoware'
tags = ['segurança', 'senhas']
toc = true
+++


**Dadoware** é um método para criar senhas aleatórias
fortes e fáceis de lembrar usando dados ⚂ ⚃ ⚅ ⚅ ⚁, papel e lápis
para sortear palavras e formar uma **frase-senha** (*passphrase*).
Se já sabe como usar, vá direto para 
[dadoware-palavras](/dadoware-palavras).

O método original 
[Diceware™](http://world.std.com/~reinhold/diceware.html) foi inventado por Arnold G. Reinhold.
A parte mais complicada é ter uma lista de
palavras para sortear lançando 5 dados. A lista precisa ter exatamente
6<sup>5</sup> (7.776) palavras familiares.
No [site original](http://world.std.com/~reinhold/diceware.html)
não havia uma lista de palavras em português,
então eu e colegas da Thoughtworks Brasil
criamos a lista [dadoware-palavras](/dadoware-palavras).

Você pode (e deve!) usar um gerenciador de senhas para criar e armazenar
senhas fortes para todas as suas contas. Mas para abrir o gerenciador
de senhas de senhas o ideal é usar uma frase-senha.
Ela funciona como uma espécie de "chave mestra" que você
precisa memorizar.

Uma frase-senha é formada por várias palavras, e é bem mais longa que
uma senha comum. Se composta de palavras familiares, uma frase-senha
pode ser mais fácil de lembrar que um monte de caracteres estranhos. E
se todas as palavras forem escolhidas de forma aleatória, será bem
difícil de quebrar.


Há uma [tirinha do XKCD](https://xkcd.com/936/) (em inglês) que explica
matematicamente porque uma senha formada por várias palavras é melhor que uma senha
tipo `Tr0v4dor&3`.

Para praticar a digitação da sua frase-senha com segurança no terminal
do seu computador, use o [passdrill](/posts/passdrill).

## Como sortear uma frase senha

Você precisa jogar 5 dados para sortear cada palavra da [lista de palavras](/dadoware-palavras),
ou pode jogar um dado 5 vezes para cada palavra.

- Os dois primeiros dados selecionam um grupo palavras. Por
  exemplo: ⚃ ⚀ é o prefixo **41**.
- Os dados restantes definem a palavra dentro do prefixo: 41 + ⚄ ⚅
  ⚂ (41563) é "joelho". [Confira](/dadoware-palavras/#prefixo-41-).

Repita o processo para **cada** palavra da frase-senha.

### Exemplo completo: frase-senha de 6 palavras

Jogue 5 dados 6 vezes, ou um dado 30 vezes, anotando os resultados de 5
em 5. Veja este exemplo completo:

|     dados |                   prefixo              |          palavra
|:---------:|:--------------------------------------:|:------------------
| ⚂ ⚃ ⚅ ⚅ ⚁ | **[34](/dadoware-palavras#prefixo-34-)** | **34662** galera
| ⚀ ⚁ ⚃ ⚅ ⚃ | **[12](/dadoware-palavras#prefixo-12-)** | **12464** ama
| ⚂ ⚁ ⚃ ⚄ ⚃ | **[32](/dadoware-palavras#prefixo-32-)** | **32454** excitar
| ⚃ ⚄ ⚄ ⚅ ⚃ | **[45](/dadoware-palavras#prefixo-45-)** | **45564** muito
| ⚅ ⚁ ⚅ ⚄ ⚄ | **[62](/dadoware-palavras#prefixo-62-)** | **62655** subir
| ⚁ ⚂ ⚄ ⚂ ⚁ | **[23](/dadoware-palavras#prefixo-23-)** | **23532** comício

Frase-senha resultante:

    galera ama excitar muito subir comício

Para memorizar, imagine uma cena com as palavras. Por exemplo: "a galera
ama exercitar muito e subir no comício".[^1]

### Procedimento mais eficiente

O mais rápido é jogar o(s) dado(s) e ir anotando os números em grupos de
cinco, para procurar as palavras depois. No exemplo anterior, você
anotaria primeiro isso:

    34 662 – 12 464 – 32 454 – 45 564 – 62 655 – 23 532

E depois procuraria as palavras, anotando assim:

    galera – ama – excitar – muito – subir – comício


## Perguntas frequentes

### Quantas palavras deve ter uma frase-senha?

O criador do Diceware recomenda um mínimo de **6** palavras.
Com 6 palavras escolhidas de um universo de 7.776,
temos 221.073.919.720.733.357.899.776 combinações:

```python
>>> 7776 ** 6
221073919720733357899776
```

Veja a
tabela para entender como a *força da senha*[^2] aumenta de acordo com o
número de palavras:

|palavras | combinações (p)  | entropia (log<sub>2</sub>p)  |caracteres base 64  |senha equivalente
|--------:| --------------------------:| -------------------:|-------------------:|------------------------------
|5        | 7.776<sup>5</sup>= 2,8 × 10<sup>19</sup>   | 64,6                |11                  |Cp8p7VP46gk
|6        | 7.776<sup>6</sup>= 2,2 × 10<sup>23</sup>   | 77,5                |13                  |0Jv0kmu/TQvPZ
|7        | 7.776<sup>7</sup>= 1,7 × 10<sup>27</sup>   | 90,5                |16                  |4Pc529BjuW+NTrBx
|8        | 7.776<sup>8</sup>= 1,3 × 10<sup>31</sup>   | 103,4               |18                  |yKlWDbbtcb/HzR8cYO

A última coluna mostra uma senha de força equivalente gerada a partir de
64 caracteres aleatórios. O que você prefere memorizar: seis
palavras comuns ou `0Jv0kmu/TQvPZ`?

### Devo usar acentos em frases-senhas?

Você decide. Mas nem sempre o teclado está configurado corretamente
antes de fazermos login em um sistema, então é mais prático evitar
acentos. No exemplo anterior, você usaria a palavra "comicio" assim, sem
o acento.

### E se eu for obrigado a usar maiúsculas, dígitos ou caracteres especiais?

Você pode jogar um dado para escolher uma palavra da sua frase-senha e
outro dado para escolher uma letra para escrever em maiúscula dentro
daquela palavra.

Para acrescentar caracteres especiais, use um dado para escolher uma
palavra e mais dois dados para escolher um dígito ou caractere especial tabela
abaixo:

|   | ⚀  | ⚁  | ⚂  | ⚃  | ⚄  | ⚅
|:--:|:--:|:--:|:--:|:--:|:--:|:--:
| ⚀ | !  | @  | \# | \$ | \% | &
| ⚁ | \* | (  | )  | \- | \_ | \+
| ⚂ | =  | {  | }  | \[ | \] |
| ⚃ | \< | \> | ,  | .  | :  | ;
| ⚄ | 1  | 2  | 3  | 4  | 5  | 6
| ⚅ | 7  | 8  | 9  | 0  | \\ | ?

### Não seria mais seguro usar o dicionário inteiro?

Em tese, sim. Porém o método Diceware foi pensado para resolver dois
problemas práticos:

- Produzir frases-senha que sejam razoavelmente fáceis de lembrar. Para
  isso selecionamos palavras familiares.
  
- Evitar o uso do computador para fazer o sorteio, pois um software que
  gera números pode estar com defeito ou comprometido. Dados são uma
  forma fácil de gerar números, mas seu uso exige uma lista de palavras
  numerada especialmente, para facilitar.

Se você tentar usar o dicionário Houaiss para criar suas frases-senha,
vai descobrir que não é fácil sortear uma palavra de forma segura e
realmente aleatória, sem usar o computador. Além disso, a maioria das
palavras sorteadas provavelmente serão pouco familiares ou mesmo
totalmente desconhecidas para você, dificultado a memorização.

### Posso escolher palavraas da lista sem jogar dados?

Se você fizer isso, não terá palavrasa aleatórias,
e a frase-senha poderá ser muito mais fácil de adivinhar.

Ao escolher palavras intencionalmente, a tendência é formar frases
gramaticalmente corretas, com sujeito, verbo, objeto.
Isso enfraquece bastante a frase-senha.

Pelo mesmo motivo, é melhor não reordenar as palavras sorteadas,
mas sim usá-las na ordem em que foram sorteadas.

### Porque não usar um aplicativo para gerar senhas?

Na verdade, eu uso um aplicativo para gerar senhas: o
gerenciador de senhas 1Password. Mas você precisa de
uma senha para abrir o gerenciador de senhas!

Além disso, para ter máxima
confiança em uma frase-senha, prefiro não usar o computador na hora de
criá-la—porque um software pode estar comprometido de várias formas,
até mesmo a função que gera números aleatórios na sua linguagem favorita.

É por isso que a [lista de palavras](/dadoware-palavras) está
toda em uma página só: você pode imprimi-la, ou salvar o HTML para criar
senhas mesmo sem uma conexão com a internet.

## Sobre o Dadoware

O **Dadoware** foi criado por um time da ThoughtWorks Brasil em 2016 como um livreto de
40 páginas que foi distribuído na [CryptoRave](https://cryptorave.org/)
e em outros eventos.
Eu escrevi o texto e fiz o lay-out do miolo do
livreto, com a ajuda do [Denis
Costa](https://twitter.com/deniscostadsc).
Cada prefixo de dois dados era uma página na lista de palavras.
A Letícia Nunes fez a capa.
Outros colegas da ThoughtWorks ajudaram a revisar a lista de palavras.

O livreto **Dadoware** foi publicado sob a licença CC BY-NC 3.0 BR
(Creative Commons Atribuição-Não Comercial 3.0 Brasil).

Os arquivos que usamos para criar o **Dadoware** estão no
[Github](https://github.com/thoughtworks/dadoware).

[^1]: OK, tive sorte nesse exemplo. Normalmente é mais difícil formar uma frase.

[^2]: definição formal: [entropia de
    Shannon](https://pt.wikipedia.org/wiki/Entropia_da_informa%C3%A7%C3%A3o#Entropia_como_conceito_da_Teoria_da_Informa%C3%A7%C3%A3o)

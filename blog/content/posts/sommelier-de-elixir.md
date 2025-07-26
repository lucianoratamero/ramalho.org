+++
date = '2025-07-26T17:12:03-03:00'
title = 'Sommelier de Elixir'
toc = true
draft = false
tags = ['tecnologia', 'programming-languages', 'Elixir']
+++

Depois que escrevi
[Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/),
duas linguagens me chamaram a atenção:
[Elixir](https://elixir-lang.org/)
e Go.

Go e Elixir são muito diferentes,
mas ambas foram criadas desde o início
para facilitar a progamação concorrente,
executando tranquilamente centenas de milhares
de tarefas em memória ao mesmo tempo,
e usando todos os núcleos disponíveis na máquina, 
sem desculpas.[^1]

Qual estudar?
Se a prioridade fosse mudar de emprego, escolheria Go
porque tem mais vagas.
Mas quero aprender conceitos novos,
treinar programação funcional,
entender mais sobre sistemas distribuídos.
Daí não tenho dúvida que Elixir é a escolha certa.

Elixir foi criada por José Valim,
que era um colaborador importante do projeto Ruby on Rails.
Concorrência é um ponto fraco em Ruby (assim como em Python).
Valim foi pesquisar linguagens com foco em concorrência
e encontrou
[Erlang](https://www.erlang.org/), uma linguagem funcional
desenvolvida para sistemas embarcados
pela Ericsson, fabricante de equipamentos de telecomunicação.
O eco-sistema Erlang inclui uma máquina virtual com JIT,
chamada BEAM, e também o OTP—um framework para a construção
de sistemas distribuídos tolerantes a falhas,
robusto e testado em aplicações de missão crítica de alto desempenho.

Dois sistemas importantes criados com Erlang/OTP são
o WhatsApp 😲 e o switch de protocolo ATM AXD301 da Ericsson.
Essas máquinas, com mais de um milhão de linhas de Erlang,
ganharam fama de alcançar "9 zeros" de confiabilidade
(cerca de 3s de downtime por ano, se fiz a conta certa).

Tudo sensacional, exceto um aspecto: a sintaxe de Erlang
é estranha, ruidosa, e limitada.
Também é pobre em mecanismos de abstração,
forçando os desenvolvedores a escrever muito código repetitivo, *boilerplate*.[^2]
Faltava também no eco-sistema Erlang
ferramentas que esperamos em uma linguagem moderna,
como um bom sistema de gerenciamento de pacotes e dependências.

Acostumado com o conforto e a qualidade de Ruby e Rails,
Valim partiu para escrever Elixir:
criando uma sintaxe moderna e poderosa
(incluindo macros sintáticas, como Lisp!),
aproveitando e melhorando as melhores ideias de Erlang,
gerando bytecode para o BEAM,
100% compatível com todas as bibliotecas de Erlang,
inclusive o framework OTP.

Nos eventos sobre Elixir em que participei,
sempre fiquei muito impressionado com palestras e
cursos sobre projetos importantes do eco-sistema,
como o framework Web Phoenix—que facilita usar WebSockets
para criar front-ends reativos sem escrever
JavaScript—a elegante DSL [Ecto](https://hexdocs.pm/ecto/getting-started.html),
para manipular bancos de dados SQL e NoSQL,
e o framework
[Nerves](https://nerves-project.org/)—que aproveita o ferramental do Erlang/OTP
para suportar construção de sistemas embarcados robustos que podem ser
atualizados "a quente", como os switches ATM da Ericsson.

Os keynotes do Valim nas ElixirConf são fantásticos.
Ele é um grande designer de linguagens,
frameworks, ferramentas,
e um líder inspirador para a comunidade:
inteligente, sábio, e modesto.
Sabe dar espaço e elevar outros colaboradores.

Agora voltando ao mundo de Elixir,
encontro mais novidades impressionantes:
um compilador capaz de fazer inferência 
de tipos para sinalizar bugs sem que
você precise escrever anotações de tipos;
um compilador para WASM ([Popocorn](https://popcorn.swmansion.com/)),
e todo um eco-sistema de computação numérica
chamado [Nx](https://github.com/elixir-nx),
para aplicações de estatística,
aprendizado de máquina, redes neurais etc.

Para programação exploratória com Nx (ou Nerves!),
agora existe o [Livebook](https://livebook.dev/),
similar ao Jupyter Notebook,
mas com suporte a Elixir, Erlang, Python por padrão,
melhor integração com testes automatizados,
e suporte a execução concorrente de células:
você pode iniciar uma computação demorada em
uma célula e seguir computando em outras
células enquanto a primeira continua processando.

Sempre que volto a mergulhar em Elixir,
a sensação é a mesma:
parece que acordei alguns anos no futuro.

Siga-me no
[Mastodon](https://ciberlandia.pt/@lr/),
no
[Blue Sky](https://bsky.app/profile/ramalho.org),
ou no
[Github](https://github.com/ramalho)
para a gente continuar trocando ideia sobre Elixir.
Logo mais farei umas atividades lá no
[Garoa Hacker Clube](https://garoa.net.br).

Aprecie sem moderação!


[^1]: Em contraste com Python, onde temos 
[três modelos de concorrência](https://pythonfluente.com/2/#ch_concurrency_models)
na biblioteca padrão,
cada um bem limitado à sua maneira.
Processos podem usar todos os núcleos,
mas usam muita memória e a comunicação entre eles é complicada.
Threads podem se comunicar mais fácil,
mas só conseguem usar um núcleo; 
e são mais leves que processos,
mas não tão leves que dê para acionar centenas de milhares
de threads de uma vez.
Corrotinas async são muito leves,
você pode ter milhões delas ativas,
mas só usam uma thread, portanto só um núcleo.
Qualquer sistema assíncrono limitado a um núcleo da CPU
exige medições e otimizações constantes
para não se tornar cada vez mais lento
à medida que novas funcionalidades são implementadas,
aumentando o trabalho do laço de eventos.
Resta ao usuário de Python escolher
qual o modelo menos ruim em cada caso de uso.

[^2]: A plataforma Java sobre de um problema parecido:
a JVM com JIT é boa, a biblioteca padrão dá pro gasto,
mas a linguagem é pobre em mecanismos de abstração,
forçando a gente a escrever/ler/manter muito *boilerplate*.
Felizmente existe Clojure.
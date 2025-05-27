+++
date = '2025-05-26T19:33:59-03:00'
title = '"Python é interpretada ou compilada?"'
toc = true
draft = false
tags = ['programming languages', 'causo']
+++

Certa vez chegando nos EUA o agente de fronteira perguntou
qual era o propósito da minha viagem,
com aquela atitude típica de um agende de fronteira dos EUA.
Falei que ia palestrar em um evento sobre Python e ele
disparou:

— Python é interpretada ou compilada?

<!--more-->

Pensei dois segundos e respondi "Interpretada" só para não
alongar o papo naquele purgatório.
Imagino que ele tenha sido adestrado para fazer perguntinhas
para desestabilizar pessoas que podem estar mentindo.

Ele me deixou entrar, mas a resposta certa é:

— Sim!

O código-fonte Python que escrevemos é compilado
para um bytecode que então é executado por um interpretador.
Como no Java.[^1]

Desde 2011 o projeto [Pypy](https://pypy.org/) oferece também um compilador JIT.
Como no Java.[^2]

O Pypy suporta até código Python 3.11,
e é quase 3x mais rápido que o CPython (segundo [benchmarks](https://speed.pypy.org/)).
Mas é menos popular porque porque é incompatível
com as inúmeras extensões (bibliotecas binárias) 
escritas em C, C++, Fortran, e Rust,
que são a razão do sucesso da linguagem Python.

Mas desde [o Natal de 2023](https://github.com/python/cpython/pull/113465)
há um JIT crescendo dentro do CPython, descrito na
[PEP 744 – JIT Compilation](https://peps.python.org/pep-0744/).
Por enquanto, esse JIT é experimental.
Nos binários de Python 3.14 para Windows ou MacOS o
JIT pode ser habilitado
[setando uma variável de ambiente](https://docs.python.org/3.14/whatsnew/3.14.html#binary-releases-for-the-experimental-just-in-time-compiler).
Para outras plataformas, é preciso compilar os fontes do CPython
passando [uma opção](https://docs.python.org/3.14/using/configure.html#cmdoption-enable-experimental-jit)
no `./configure`.

No Python 3.14, o desempenho do JIT experimental
[é descrito](https://docs.python.org/3.14/whatsnew/3.14.html#binary-releases-for-the-experimental-just-in-time-compiler)
como "10% mais lento até 20% mais rápido, dependendo da carga."

Então, se o clima na imigração fosse mais relax, hoje eu responderia:

— Python é compilada para um bytecode que é interpretado em tempo de execução,
mas usando o Pypy ou o CPython 3.13 ou 3.14 você pode ter um compilador
JIT para acelerar a execução. Então podemos dizer que Python é compilada, interpretada e compilada!


[^1]: O programa `javac` é o compilador que transforma código-fonte `.java` em bytecodes
salvos em arquivos `.jar` ou `.class`.
Para executar, usa-se outro programa: `java`.
No Python não há essa separação: o compilador de `.py` para bytecode
e o interpretador de bytecode estão no mesmo programa, `python3` ou `pypy3`, por exemplo.
Os arquivos `.pyc` contém bytecode Python, mas raramente precisamos se preocupar com eles.

[^2]: JIT é "Just In Time", ou "na hora H" numa tradução livre.
Enquanto o interpretador executa o bytecode,
o compilador JIT analisa os bytecodes rodando,
identifica trechos "quentes" (laços com muitas voltas, por exemplo),
daí compila código de máquina equivalente,
e desvia a execução dos bytecodes
para o código de máquina, tudo no _runtime_, na hora H.


 

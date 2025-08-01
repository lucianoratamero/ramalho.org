+++
date = '2025-04-29T20:53:03-03:00'
draft = false
title = 'Passdrill: para praticar senhas fortes'
tags =['segurança', 'senhas']
+++

Você pode usar o [Dadoware](/posts/dadoware) para criar uma
frase-senha forte, mas para usá-la no dia-a-dia ainda vai precisar:

- memorizar a senha;
- aprender a digitá-lo de forma rápida e confiável.

Com **Passdrill**, você pratica a digitação de uma senha longa
em um ambiente seguro: seu console local.

O **passdrill** não salva a senha digitada, mas sim uma assinatura
digital (*hash*) derivada da senha, através dos algoritmos **scrypt** ou
**pbkdf2**—projetados para tornar os ataques de força-bruta mais
difíceis.

Veja o conteúdo do arquivo `passdrill.hash` gerado pelo exemplo abaixo:

    scrypt:UJGFquwCLGFrD+fzrqt91UvOdcrIKhB0/pEp6Un/l48=:Xg129pYzkm5pZIgx0p1SFf6bmFCvrFB5jNGxd/Y4oB+TU/tZXWraD+g7Ui0A8t4dN4CuzYXFp9+TuOLdPlzwlg==

Repositório com o programa: <https://github.com/ramalho/passdrill>

## Demonstração

Essa é uma seção de prática com o **passdrill**:

```
$ passdrill
Type q to end practice.
1:
  OK    hits=1  misses=0
2:
  wrong hits=1  misses=1
3:
  OK    hits=2  misses=1
4:
  OK    hits=3  misses=1
5:
4 exercises. 75.0% correct.
```

As linhas marcadas com `1:`, `2:`, etc. são os *prompts*, onde você
digita a senha. Por segurança, o programa não exibe um eco durante a
prática. A cada tentativa, o programa diz se a digitação foi correta ou
não, e atualiza o placar. Para encerrar, digite apenas a letra **q**.

Antes de iniciar a prática, você precisa salvar a senha, usando o
comando `passdrill -s`, assim:

    $ passdrill -s
    WARNING: the passphrase will be shown so that you can check it!
    Type passphrase to hash (it will be echoed): galera ama excitar muito subir comicio
    Passphrase to be hashed -> galera ama excitar muito subir comicio
    Confirm (y/n): y
    Passphrase hash saved to passdrill.hash

Neste exemplo, a senha a ser praticada é "galera ama excitar muito
subir comicio" (uma frase-senha forte produzida pelo método
[Dadoware](/dadoware/Dadoware).


## Sobre o desenvolvimento

Escrevi o **passdrill** primeiramente porque eu queria um programa assim
para praticar a digitação das minhas senhas mais fortes. A primeira
versão eu fiz em Python 3, e logo em seguida reescrevi em Go, para
comparar.

A versão em Go ficou cerca de 40% mais longa. Mas ela tem uma vantagem
importante: é mais fácil de instalar. Go permite que eu compile o
programa e distribua o executável em um único arquivo pronto para usar.
Mesmo para quem quer inspecionar e compilar o código-fonte, Go é mais
fácil do que Python porque as dependências externas são escritas em Go
mesmo. No caso de Python, para usar `scrypt` no final de 2017 a maioria
das pessoas vai ter que compilar um pacote externo que depende de código
em C, e isso é mais ou menos fácil no GNU/Linux, mais difícil no MacOS
X, e super complicado no Windows.

O arquivo
[README.md](https://github.com/ramalho/passdrill/blob/master/README.md)
do projeto **passdrill** no Github tem uma análise mais detalhada das
diferenças entre as versões Python e Go.

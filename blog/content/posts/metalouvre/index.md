+++
date = '2025-04-24T11:55:20-03:00'
draft = false
title = 'O grande ataque ao MetaLouvre'
tags = ['ficção', 'tecnologia', 'criptoativos']
+++

![Turistas fotografando a moldura da Mona Lisa, com o emoji "FACE SCREAMING IN FEAR" no lugar da pintura de Leonardo Da Vinci](metalouvre-grito.jpg)

Após enfrentar longas filas para entrar no MetaLouvre,
turistas do Metaverso ficaram chocados quando centenas de
pinturas nas galerias renascentistas
foram trocadas por emojis diante de seus olhos.
A Mona Lisa foi substituída pelo emoji Unicode `U+1F631`, "Rosto Gritando de Medo", inspirado na pintura "O Grito" de Edvard Munch.

Os curadores do MetaLouvre ficaram mais chocados que os turistas quando
descobriram como o ataque se desenrolou e suas consequências de longo prazo.
Os curadores sabiam que cada objeto no Metaverso era protegido por NFTs.
O que dava ao MetaLouvre o direito de exibir a imagem gêmea digital única e canônica da Mona Lisa
era a existência de um NFT vinculando a propriedade do artefato digital ao museu.
A plataforma do Metaverso usa esses NFTs para determinar
quem tem o direito de exibir cada obra de arte em seu espaço virtual.
Os NFTs são armazenadas permanentemente no blockchain, protegidas pela matemática aplicada.

No entanto, os gêmeos digitais das pinturas não eram armazenadas no próprio blockchain,
porque adicionar megabytes ao blockchain era proibitivamente caro e
agravaria os conhecidos problemas de escalabilidade desta tecnologia.
A solução oferecida pelos vendedores de NFTs era registrar só a URL de cada imagem no blockchain.
Por exemplo, a URL armazenada na NFT da Mona Lisa era `https://safevault.eth/metalouvre/Mona_Lisa_8K-3109372.jpg`
(link quebrado, explicação a seguir).

O que os curadores do MetaLouvre não sabiam era que os NFTs não continham
uma assinatura digital do conteúdo do arquivo, uma precaução básica para detectar adulterações no conteúdo supostamente protegido.
Quando os servidores da SafeVault foram invadidos,
os hackers substituíram as imagens das pinturas renascentistas por emojis,
mas não havia dados no blockchain para prevenir ou mesmo detectar tal ataque.

Os operadores da SafeVault recuperaram os arquivos originais de um backup,
então as pinturas originais ficaram visíveis novamente no MetaLouvre algumas horas depois.
Mas o dano à reputação foi fatal para uma empresa que prometia hospedagem segura de objetos do Metaverso.

Quatro meses após o ataque ao acervo digital do MetaLouvre, a SafeVault faliu.
À medida que suas operações eram encerradas,
um gestor perdeu a chave privada para gerenciar o domínio `safevault.eth`.
cujo registro é permanentemente armazenado na blockchain.

Sem a chave privada, ninguém poderia transferir o domínio para um novo proprietário.
Quando a SafeVault encerrou suas operações,
havia 128.561 NFTs apontando para URLs em `safevault.eth`, com um valor total estimado em 1,3 bilhão de dólares.
Cada um desses NFTs se tornou inútil quando o domínio `safevault.eth` expirou em dezembro de 2023,
porque suas URLs apontavam para um domínio desconfigurado que jamais poderia ser recuperado.

As consequências de longo prazo do ataque ao acervo digital do MetaLouvre nunca serão corrigidas,
graças à natureza imutável da blockchain, protegida pela matemática.

----

> Esta fábula foi inspirada no texto
[My first impressions of web3](https://moxie.org/2022/01/07/web3-first-impressions.html)
de Moxie Marlinspike, detalhando as limitações da tecnologia NFT.
Moxie Marlinspike é o criptógrafo, pesquisador de segurança de computadores,
e co-criador do protocolo Signal e do aplicativo de mensagens criptografadas.

# Instruções para operar o blog

## Criar novo documento plano em markdown

```shell
hugo new content/posts/banana.md
```

## Transformar documento plano em aninhado

Bom para colocar as imagens no mesmo diretório do texto.

```shell
$ ./aninhar.sh content/posts/banana.md
```

O texto é movido para `content/posts/banana/index.md`:

```
$ tree content
content
├── posts
│   ├── banana
│   │   ├── index.md
│   │   └── (futura imagem aqui)
┆   ┆
```

Aninhar não muda a URL da página, continua sendo:

```
https://ramalho.org/posts/banana/
```


# Instruções para operar o blog

## Criar nova página simples em markdown

```shell
hugo new content/posts/banana.md
```

## Embrulhar página

Transforma uma página simples num embrulho
([page bundle](https://gohugo.io/content-management/page-bundles/).

Bom para colocar imagens e anexos no mesmo diretório do texto.

```shell
$ ./embrulhar.sh content/posts/banana.md
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

Embrulhar não muda a URL da página.
A URL do exemplo é a mesma antes e depois de embrulhar:

```
https://ramalho.org/posts/banana/
```


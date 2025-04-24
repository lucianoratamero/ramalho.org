# Instruções para operar o blog

## Criar novo documento plano em markdown

```shell
hugo new content/posts/banana.md
```

## Transformar documento plano em aninhado

Bom para colocar as imagens no mesmo diretório do texto.

```shell
./aninhar.sh banana  # sem a extensão .md
```

O resultado fica em `content/posts/`:

```
posts
└── banana
    └── index.md
```



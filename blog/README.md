# DIÁRIO DA CONSTRUÇÃO DESTE BLOG

## Primeiros passos

### Criei a estrutura

```
% hugo new site blog 
Congratulations! Your new Hugo site was created in /Users/luciano/prj/ramalho.or
g/blog.

Just a few more steps...

1. Change the current directory to /Users/luciano/prj/ramalho.org/blog.
2. Create or install a theme:
   - Create a new theme with the command "hugo new theme <THEMENAME>"
   - Or, install a theme from https://themes.gohugo.io/
3. Edit hugo.toml, setting the "theme" property to the theme name.
4. Create new content with the command "hugo new content <SECTIONNAME>/<FILENAME
>.<FORMAT>".
5. Start the embedded web server with the command "hugo server --buildDrafts".

See documentation at https://gohugo.io/.
%
```

Seguindo o roteiro acima, o primeiro passo é entrar no diretório `./blog`.
Em seguida, examinei a estrutura com o comando
`tree` (que você talvez precise instalar; é comum mas não é padrão):

```
% cd blog
% tree
.
├── archetypes
│   └── default.md
├── assets
├── content
├── data
├── hugo.toml
├── i18n
├── layouts
├── static
└── themes

9 directories, 3 files
```

### Primeiro acesso

Agora, subir o servidor de desenvolvimeto e
acessar com `curl` em outro terminal para ver o que temos.

#### Terminal 1:

```
% hugo server
Watching for changes in /Users/luciano/prj/ramalho.org/blog/{archetypes,assets,content,data,i18n,layouts,static}
Watching for config changes in /Users/luciano/prj/ramalho.org/blog/hugo.toml
Start building sites … 
hugo v0.146.6+extended+withdeploy darwin/arm64 BuildDate=2025-04-20T10:58:40Z VendorInfo=brew

WARN  found no layout file for "html" for kind "home": You should create a template file which matches Hugo Layouts Lookup Rules for this combination.
WARN  found no layout file for "html" for kind "taxonomy": You should create a template file which matches Hugo Layouts Lookup Rules for this combination.

                   | EN  
-------------------+-----
  Pages            |  4  
  Paginator pages  |  0  
  Non-page files   |  0  
  Static files     |  0  
  Processed images |  0  
  Aliases          |  0  
  Cleaned          |  0  

Built in 1 ms
Environment: "development"
Serving pages from disk
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1) 
Press Ctrl+C to stop
```

O comando `hugo server` cria o site em memória, sem salvar nenhum arquivo estático.

Para ver o que temos, uso o `curl` em outro terminal.

#### Terminal 2:

```
% curl http://localhost:1313/ -i
HTTP/1.1 404 Not Found
X-Hugo-Redirect: true
Date: Mon, 21 Apr 2025 19:59:28 GMT
Content-Length: 24
Content-Type: text/html; charset=utf-8

<h1>Page Not Found</h1>
%
```

Acessando a raiz `/` recebo `404 Not Found`.

Porém o servidor no **terminal 1** informou `4 pages`.

Que páginas são essas?

Parei o servidor (`CTRL+C` no **terminal 1**) e
gerei as páginas estáticas com:

```
% hugo
Start building sites …

(mais linhas, parecidas com a saida de `hugo server`)
```

Agora o Hugo gerou arquivos no diretório `public`.

```
% tree public 
public
├── categories
│   └── index.xml
├── index.xml
├── sitemap.xml
└── tags
    └── index.xml

3 directories, 4 files
```

Os três `index.xml` são [RSS](https://pt.wikipedia.org/wiki/RSS).
RSS é uma tecnologia que pode nos libertar das redes sociais!

O `/sitemap.xml` é uma descrição da estrutura do site para
auxiliar a indexação do site por robôs como buscadores e
aspiradores de conteúdo para IA
(veja [Sitemap](https://pt.wikipedia.org/wiki/Sitemap)).

Rodando o servidor no **terminal 1**, posso acessar o RSS
da raiz do site pelo **terminal 2**:

```
% curl http://localhost:1313/index.xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>My New Hugo Site</title>
    <link>http://localhost:1313/</link>
    <description>Recent content on My New Hugo Site</description>
    <generator>Hugo</generator>
    <language>en-us</language>
    <atom:link href="http://localhost:1313/index.xml" rel="self" type="application/rss+xml" />
  </channel>
</rss>
%
```

E o mapa do site:

```
% curl http://localhost:1313/sitemap.xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>http://localhost:1313/categories/</loc>
  </url><url>
    <loc>http://localhost:1313/</loc>
  </url><url>
    <loc>http://localhost:1313/tags/</loc>
  </url>
</urlset>
%
```

#### Primeiras pistas da arquitetura da informação

O `sitemap.xml` aponta três caminhos:

* `/`
* `/categories/`
* `/tags`

Cada um desses caminhos tem um RSS em sua raiz.

Com base na minha experiência com sites de conteúdo
e meus estudos em biblioteconomia, imagino que
`categories` pode formar uma taxonomia hieraráquica
de temas e sub-temas, enquanto `tags` provalmente
é uma lista plana (somente um nível), como uma
classificação independente (ortogonal).

Será que estou certo?

### Criei o primeiro documento

```
% hugo new content oi.md
Content "/Users/luciano/prj/ramalho.org/blog/content/oi.md" created
```

Hugo escreveu o seguinte em `oi.md`:

```
+++
date = '2025-04-21T17:57:30-03:00'
draft = true
title = 'Oi'
+++
```

Esses metadados estruturados são chamados de
[front matter](https://gohugo.io/content-management/front-matter/)
na documentação do Hugo. O Hugo suporta sintaxe JSON, YAML e TOML
para os metadados.
TOML é o formato padrão, indicado pelos delimitadores `+++`.

Escrevi qualquer coisa abaixo dos `+++` para poder acessar depois.

Gerando o site com o comando `hugo`, percebo que nada mudou nos XML
que já vimos, e nenhum arquivo novo foi gerado em `/public`.

Agora tenho duas opções: editar o `hugo.toml` ou criar um tema.

### Criei o tema basico

Criar ou instalar um tema foi segundo passo do roteiro exibido
quando criei a estrutura com `hugo new site blog`.

Decidi criar um tema do zero, que chamei de `basico`.

```
% hugo new theme basico
Creating new theme in /Users/luciano/prj/ramalho.org/blog/themes/basico
```

Isso cria um diretório `themes/basico` com vários subdiretórios e arquivos.
Nenhum arquivo fora de `themes/basico` é modificado pelo comando.

```
% tree
.
├── README.md
├── archetypes
│   └── default.md
├── assets
├── content
├── data
├── hugo.toml
├── i18n
├── layouts
├── public
│   ├── categories
│   │   └── index.xml
│   ├── index.xml
│   ├── sitemap.xml
│   └── tags
│       └── index.xml
├── static
└── themes
    └── basico
        ├── archetypes
        │   └── default.md
        ├── assets
        │   ├── css
        │   │   └── main.css
        │   └── js
        │       └── main.js
        ├── content
        │   ├── _index.md
        │   └── posts
        │       ├── _index.md
        │       ├── post-1.md
        │       ├── post-2.md
        │       └── post-3
        │           ├── bryce-canyon.jpg
        │           └── index.md
        ├── data
        ├── hugo.toml
        ├── i18n
        ├── layouts
        │   ├── _partials
        │   │   ├── footer.html
        │   │   ├── head
        │   │   │   ├── css.html
        │   │   │   └── js.html
        │   │   ├── head.html
        │   │   ├── header.html
        │   │   ├── menu.html
        │   │   └── terms.html
        │   ├── baseof.html
        │   ├── home.html
        │   ├── list.html
        │   ├── single.html
        │   ├── taxonomy.html
        │   └── term.html
        └── static
            └── favicon.ico

26 directories, 31 files
%
```


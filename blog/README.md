# Diário da construção deste blog

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

```xml
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

```xml
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
`categories` pode formar uma taxonomia
de temas com um *vocabulário controlado*—um conjunto
de termos pré-estabelecido, como "jogos", "programação" etc.

Por outro lado, `tags` costuma ser uma
[folksonomia](https://pt.wikipedia.org/wiki/Folksonomia)
uma lista livre de termos independente das categorias,
sem um vocabulário controlado.

Será que estou certo?

### Criei o primeiro documento

```
% hugo new content oi.md
Content "/Users/luciano/prj/ramalho.org/blog/content/oi.md" created
```

Hugo escreveu o seguinte em `oi.md`:

```toml
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

Alterei o campo `draft` para `false` para que a página seja gerada.

```toml
+++
date = '2025-04-21T17:57:30-03:00'
draft = true
title = 'Oi'
+++
```

Escrevi qualquer coisa abaixo dos `+++` para poder acessar depois.

Gerando o site com o comando `hugo`,
percebo que nenhum arquivo novo foi gerado em `/public`,
e os RSS `index.html` em `categories` e `tags` não mudaram.

Mas o RSS `/index.xml` agora inclui a página `oi`:

```xml
% curl http://localhost:1313/index.xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>My New Hugo Site</title>
    <link>http://localhost:1313/</link>
    <description>Recent content on My New Hugo Site</description>
    <generator>Hugo</generator>
    <language>en-us</language>
    <lastBuildDate>Mon, 21 Apr 2025 17:57:30 -0300</lastBuildDate>
    <atom:link href="http://localhost:1313/index.xml" rel="self" type="application/rss+xml" />
    <item>
      <title>Oi</title>
      <link>http://localhost:1313/oi/</link>
      <pubDate>Mon, 21 Apr 2025 17:57:30 -0300</pubDate>
      <guid>http://localhost:1313/oi/</guid>
      <description>&lt;p&gt;&amp;ldquo;Olá, mundo!&amp;rdquo;, já diziam os antigos.&lt;/p&gt;&#xA;&lt;p&gt;Este é o primeiro conteúdo deste sítio.&lt;/p&gt;</description>
    </item>
  </channel>
</rss>
```

E ela também aparece no `sitemap.xml`:

```xml
% curl http://localhost:1313/index.xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>http://localhost:1313/</loc>
    <lastmod>2025-04-21T17:57:30-03:00</lastmod>
  </url><url>
    <loc>http://localhost:1313/oi/</loc>
    <lastmod>2025-04-21T17:57:30-03:00</lastmod>
  </url><url>
    <loc>http://localhost:1313/categories/</loc>
  </url><url>
    <loc>http://localhost:1313/tags/</loc>
  </url>
</urlset>
```

Porém, o caminho `/oi` ainda não está acessível:

```
% curl http://localhost:1313/oi/
<h1>Page Not Found</h1>
```

Imagino que o motivo é a falta de um template,
um modelo de página em geral definido em um tema.

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
% tree themes
themes
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

15 directories, 24 files

```

Para ativar o tema, preciso editar a configuração.


### Editei a configuração do site

Hugo criou o arquivo de configuração `blog/hugo.toml` assim:

```
baseURL = 'https://example.org/'
languageCode = 'en-us'
title = 'My New Hugo Site'
```

Nova configuração:

```
baseURL = 'https://ramalho.org/'
languageCode = 'pt-BR'
title = 'Blog do Ramalho.org'
theme = 'basico'
```

Agora o comando `hugo` informa 19 páginas criadas!

```
                   | EN
-------------------+-----
  Pages            | 19
  Paginator pages  |  0
  Non-page files   |  1
  Static files     |  1
  Processed images |  0
  Aliases          |  0
  Cleaned          |  0
```

Agora já é possível navegar pelo blog!

<img src="home-1.png" alt="página inicial do blog" width="400"/>

Além da página `oi` temos também `post-1`, `post-2` e `post-3`, que
foram gerados pelo Hugo no diretório `/themes/basico/content/posts/`.

A próxima missão é entender a lógica da página inicial `/`: como definir quais conteúdos aparecem aqui? No momento estão misturados os posts do tema e o meu post.

## Referências

* [Front-matter and taxonomies](https://gohugo.io/content-management/front-matter/#taxonomies)

* [Hugo: Injecting an external file into a page with syntax highlighting](https://me.micahrl.com/blog/hugo-shortcode-importcode/)

* [How to include code examples from file with Hugo](https://marcusolsson.dev/how-to-include-code-examples-from-file-with-hugo/)

* [Include code from a file with Hugo](https://www.marcusfolkesson.se/blog/include-code-from-a-file-with-hugo/)

* [Include shortcode from hugo-geekdoc](https://github.com/thegeeklab/hugo-geekdoc/blob/1bb1dab866fbd0b6bf28d2f0aaeaaced7e814fc0/layouts/shortcodes/include.html)

* [zsh functions for hugo static site generator](https://gist.github.com/RickCogley/5673669a5c6e9b05070cd4c50e4bd50f)

* [Blockquote render hooks: alerts](https://gohugo.io/render-hooks/blockquotes/#alerts)

* [Making Your RSS Feeds Automatically Discoverable](https://blog.jim-nielsen.com/2021/automatically-discoverable-rss-feeds/)
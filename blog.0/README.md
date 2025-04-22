# ramalho.org
Páginas do ramalho.org


## Notas sobre a construção do blog

### Meu guia

Estou seguindo o roteiro do livro
[Build Websites with Hugo](https://pragprog.com/titles/bhhugo/build-websites-with-hugo/)
de Brian P. Hogan (Pragmatic Programmers, 2020), doravante abreviado para BWH.

Optei por esse livro em vez da documentação oficial porque o autor mostra
a construção de um site com Hugo desde o zero, sem usar nenhum tema pronto.

Brian Hogan escreveu na p. 15 de BWH:

> Many off-the-shelf themes are fairly complex with lots of features
> that take time to configure properly.
> It’s best to understand how theming works before you dive into someone else’s code.


### Notas

### Primeiro passo

```
% hugo new site blog
Congratulations! Your new Hugo site was created in /Users/luciano/prj/ramalho.org/blog.

Just a few more steps...

1. Change the current directory to /Users/luciano/prj/ramalho.org/blog.
2. Create or install a theme:
   - Create a new theme with the command "hugo new theme <THEMENAME>"
   - Or, install a theme from https://themes.gohugo.io/
3. Edit hugo.toml, setting the "theme" property to the theme name.
4. Create new content with the command "hugo new content <SECTIONNAME>/<FILENAME>.<FORMAT>".
5. Start the embedded web server with the command "hugo server --buildDrafts".

See documentation at https://gohugo.io/.
```

#### Arquivo de configuração

* `hugo new site blog` agora cria um `hugo.toml` e não `config.toml`;
o nome mudou na versão 
([v0.110.0](https://github.com/gohugoio/hugo/releases/tag/v0.110.0))

### Aviso sobre layout faltando

* Depois de criar `layouts/index.html` e `content/_index.md`, rodei
`hugo server` mas recebi um aviso:

```
% hugo server
Watching for changes in /Users/luciano/prj/ramalho.org/blog/{archetypes,assets,content,data,i18n,layouts,static}
Watching for config changes in /Users/luciano/prj/ramalho.org/blog/hugo.toml
Start building sites … 
hugo v0.146.6+extended+withdeploy darwin/arm64 BuildDate=2025-04-20T10:58:40Z VendorInfo=brew

WARN  found no layout file for "html" for kind "taxonomy": You should create a template file which matches Hugo Layouts Lookup Rules for this combination.

                   | EN  
-------------------+-----
  Pages            |  5  
  Paginator pages  |  0  
  Non-page files   |  0  
  Static files     |  0  
  Processed images |  0  
  Aliases          |  0  
  Cleaned          |  0  

Built in 2 ms
Environment: "development"
Serving pages from disk
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1) 
Press Ctrl+C to stop
```

### O layout `single.html` 

BWH, p.10, manda criar `layouts/_default/single.html`.

Esse nome `single` parece ser especial, mas quando criei
o arquivo com o nome `simples.html` também funcionou,
talvez porque fosse o único arquivo em `layouts/_default/`.
Será?

### Tema mínimo

BWH, p. 25:

> A basic Hugo theme only needs these files:
```
layouts
├── _default
│ ├── list.html
│ └── single.html
└─── index.html
```
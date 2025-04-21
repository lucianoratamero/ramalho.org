# DIÁRIO DA CONSTRUÇÃO DESTE BLOG

## Primeiros passos

### Criando a estrutura

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





#!/bin/bash
set -e  # exit when any command fails

# build
hugo --minify

# sync
rsync -avz --delete ./public/ ramalho@ramalho.org:~/ramalho.org/public

open https://ramalho.org

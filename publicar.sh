
#!/bin/bash
set -e  # exit when any command fails

# build
cd blog
hugo   # --minify
cd ..

# sync
rsync -avz --delete blog/public/ ramalho@ramalho.org:~/ramalho.org/public

open https://ramalho.org

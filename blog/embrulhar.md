#!/bin/bash
set -e  # exit when any command fails

# Check if required arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Modo de usar: $0 <file_path>"
    exit 1
fi

# Get the full path of the file
file_path="$1"

# Extract base directory and filename
base=$(dirname "$file_path")
name_ext=$(basename "$file_path")

# Extract name without extension
name="${name_ext%.*}"

# Create target directory
mkdir -p "$base/$name"

# Move the file to the new location
mv "$base/$name_ext" "$base/$name/index.md"

echo "$name_ext aninhado como $base/$name/index.md"
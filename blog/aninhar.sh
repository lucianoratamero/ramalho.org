#!/bin/bash
set -e  # exit when any command fails

mkdir content/$1
git mv content/$1.md content/$1/index.md


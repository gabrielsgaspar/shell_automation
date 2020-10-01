#!/bin/bash

function project () {
    cd "/Users/gabrielsgaspar/Projects/personal_projects/shell_automation/code"
    source .env
    python instructions.py $1
    cd $PROJECT_PATH/$1
    git init
    git remote add origin https://github.com/$USER/$1.git
    touch README.md
    touch .gitignore
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    atom .
}

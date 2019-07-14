#!/bin/sh

if [ $# -lt 1 ]
then
    echo "ERROR : you need to give a commit message."
    exit 1
fi

tree > filelist
for f in `find ./ -iname '*.sh' -o -iname '*.py' -o -iname '*.html'`
do
    git add "${f}"
done
git add filelist
git add README.md

git commit -m "${@}"
git push -u origin master

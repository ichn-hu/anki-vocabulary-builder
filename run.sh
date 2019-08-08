#! /bin/bash
PYTHONIOENCODING=UTF-8 python vocab.py
git add .
git commit -m "update vocabulary"
cid=$(git rev-parse HEAD)
sed -i "s/const CACHE_NAME = '[a-z0-9]*'/const CACHE_NAME = '${cid}'/" sw.js
git add .
git commit -m "update cache"
git push

#!/bin/bash

set -e

python updater.py "$API_KEY"

reponame="forex-backend"
branchname="json-data"

username="altbdoor"
email="lancersupraskyline@gmail.com"

git init
git config user.name "$username"
git config user.email "$email"

timestamp=$(date '+%Y-%m-%dT%H:%M:%S%z')
git add data.json
git commit -m "[appveyor] updated $branchname on $timestamp"

git push --force --quiet "https://$username:${GH_TOKEN}@github.com/$username/$reponame.git" master:$branchname > /dev/null 2>&1

#!/usr/bin/env bash

git checkout production
git reset --hard origin/master
git push --force
git checkout master

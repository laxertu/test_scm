#!/bin/bash

REPOSITORY=$(git rev-parse --abbrev-ref HEAD)
# git describe --tags --abbrev=0
VERSION=$(python setup.py --version)

if [ "$REPOSITORY" == "master" ]; then
    if [ $(git tag -l "$VERSION") ]; then
      echo "WARNING VERSION ALREADY EXISTS"
  else
      echo "aaaaaaaa ${VERSION}"
      git tag $VERSION
  fi
fi

echo "Package version"
echo "${VERSION}"

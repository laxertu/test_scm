#!/bin/bash

REPOSITORY=$(git rev-parse --abbrev-ref HEAD)
# git describe --tags --abbrev=0
VERSION=$(python setup.py --version)

if [ "$REPOSITORY" == "master" ]; then
  echo "aaaaaaaa ${VERSION}"
  git tag $VERSION
fi

echo "Package version"
echo "${VERSION}"

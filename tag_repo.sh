#!/bin/bash

REPOSITORY=$(git rev-parse --abbrev-ref HEAD)
# git describe --tags --abbrev=0
VERSION=$(python get_version.py)

if [ "$VERSION" != ""]; then
    if [ "$REPOSITORY" == "master"]; then
    git tag $VERSION
  fi
fi

echo "Package version"
echo "${VERSION}"

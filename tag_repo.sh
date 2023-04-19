#!/bin/bash

REPOSITORY=$(git rev-parse --abbrev-ref HEAD)
# git describe --tags --abbrev=0

if [ "$REPOSITORY" = "master" ]; then
  CURRENT_VERSION = $(python setup.py --version)
  VERSION=$(python get_version.py ${CURRENT_VERSION})
  git tag $VERSION
  echo "tagged package version"
  echo "${VERSION}"
fi


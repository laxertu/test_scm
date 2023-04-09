#!/bin/bash

REPOSITORY=$(python get_current_branch.py)
VERSION=$(python get_version.py)

if [ "$REPOSITORY" == "master" ]; then
  echo "git tag ${VERSION}"
  git tag $VERSION
fi

echo "Package version"
echo "${VERSION}"

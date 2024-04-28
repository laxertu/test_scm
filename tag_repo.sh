#!/bin/bash

repository=$(git rev-parse --abbrev-ref HEAD)
# git describe --tags --abbrev=0
# git tag | xargs git tag -d
if [ "$repository" = "master" ]; then
  package_current_version=$(python setup.py --version)
  echo "${package_current_version}"

  IFS='+'
  read -ra ADDR <<<$package_current_version
  package_next_version="${ADDR[0]}"


  if [ "$package_next_version" != "" ]; then
    git tag "$package_next_version"
    echo "${package_next_version}"
  fi
fi


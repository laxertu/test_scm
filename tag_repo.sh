#!/bin/bash

repository=$(git rev-parse --abbrev-ref HEAD)
# git describe --tags --abbrev=0
# git tag | xargs git tag -d
if [ "$repository" = "master" ]; then
  package_current_version=$(python setup.py --version)
  echo "${package_current_version}"
  package_next_version=$(python get_version_to_tag.py ${package_current_version})

  if [ "$package_next_version" != "" ]; then
    git tag $package_next_version
    echo "tagged package version"
    echo "${package_next_version}"
  fi
fi


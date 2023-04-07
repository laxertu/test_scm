#!/bin/bash

VERSION=$(python get_version.py)

if [ "$VERSION" != "" ]; then
echo "${VERSION}"
echo "git tag ${VERSION}"
git tag $VERSION
git push --tags
fi

#echo "${OUTPUT}"

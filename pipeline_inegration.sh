#!/bin/bash

VERSION=$(python get_version.py)

if [ "$VERSION" != "" ]; then
echo "${VERSION}"
echo "git tag ${VERSION}"
exec git tag $VERSION
exec git push --tags
fi

#echo "${OUTPUT}"

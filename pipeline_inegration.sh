#!/bin/bash

VERSION=$(python get_version.py)

if [ "$VERSION" != "" ]; then
echo "${VERSION}"
exec git tag $VERSION
fi

#echo "${OUTPUT}"

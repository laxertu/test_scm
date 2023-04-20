#!/bin/bash

python setup.py  bdist_wheel
./tag_repo.sh

CURRENT_VERSION=$(python setup.py --version)
echo "installed version"
echo "${CURRENT_VERSION}"

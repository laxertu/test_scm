#!/bin/bash

./tag_repo.sh
python setup.py  bdist_wheel

CURRENT_VERSION=$(python setup.py --version)
echo "installed version"
echo "${CURRENT_VERSION}"

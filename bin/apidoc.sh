#!/usr/bin/env bash

CURRENT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $CURRENT_DIR/../

if [ ! -n "$1" ] ;then
apidoc
else
apidoc -o $1
fi


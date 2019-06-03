#!/usr/bin/env bash
cd "$( cd -p "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo $(pwd)
python3 -m gc2d $@
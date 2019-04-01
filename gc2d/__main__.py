#!/usr/bin/env python3 

"""
There are several ways to start the program:

The preferred way is to go to the root git directory and run `python3 -m gc2d`.

Alternative ways are running `python3 gc2d/` from the git root, or `python3 .` from the gc2d dir
You can also explicitly execute __main__.py using `python3 __main__.py` or `./__main__.py`
"""

import sys

if sys.version_info[0] < 3:
    print("Error: this program is written in python 3. You are trying to run it in python 2")
    sys.exit(-1)

if __package__ != "gc2d":
    import os.path

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from gc2d.main import main

main()

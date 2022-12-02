#!/usr/bin/env python3

"""
 Base class for all puzzles
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import os.path
import sys
from collections.abc import Callable

class Base:
    input: list = []

    def __init__(self, input_path: str = None, map_function: Callable[[str], any] = str):
        # get current day and script directory
        script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))

        # default to day input file name format
        if input_path is None:
            input_path = "input"

        abs_input_path = os.path.join(script_dir, input_path)
        assert os.path.isfile(abs_input_path)

        with open(abs_input_path, "r") as f:
            # read all lines in passing it through a cast/clean/format function e.g.
            # lambda x:x.split(" ")   or just int
            self.input = map(map_function, f.readlines())

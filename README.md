# Advent-Of-Code-2022
https://adventofcode.com/2022

## Usage

Requires python 3.9 or newer.

```shell
PYTHONPATH=$PWD python -u dayX/partX.py
```

You can run all days and parts with:
```shell
for d in day*; do echo $d; python -u $d/part1.py; python -u $d/part2.py; done
```

or in docker with:
```shell
docker run --rm $(docker build -q .)
```


## Layout

`common/base.py` contains a class that opens a text file called `input` in the relevant day directory and adds each line to the list `self.input`, it can also optionally run a function over each line for conversion and sanitisation.

Each `dayX` directory contains it's input and two parts, these parts contain a class that overrides the base class and mixes in a `def solution` method that contains the logic relevant to that part.
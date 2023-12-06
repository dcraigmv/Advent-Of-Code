#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2023"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

from copy import copy

from common.base import Base

class Map():
    ranges: list

    def __init__(self, type: str):
        self.ranges = []
        self.source, _, self.destination = type.split("-")

    def add_range(self, map_range: list):
        self.ranges.append(copy(map_range))

    def source_to_destination(self, source_id: int):
        for map_range in self.ranges:
            if source_id < map_range[1] or source_id > (map_range[1] + map_range[2]):
                continue

            return map_range[0] + (source_id - map_range[1])

        return source_id

    def __repr__(self):
        return "%s-to-%s Map with %d ranges" % (self.source, self.destination, len(self.ranges))

class Puzzle(Base):
    def solve_for_seed(self, seed: int):
        while seed < upper:
            soil = self.maps["seed-to-soil"].source_to_destination(seed)
            fert = self.maps["soil-to-fertilizer"].source_to_destination(soil)
            water = self.maps["fertilizer-to-water"].source_to_destination(fert)
            light = self.maps["water-to-light"].source_to_destination(water)
            temp = self.maps["light-to-temperature"].source_to_destination(light)
            hum = self.maps["temperature-to-humidity"].source_to_destination(temp)
            loc = self.maps["humidity-to-location"].source_to_destination(hum)

            if loc < self.closest_location:
                self.closest_location = loc

            # print([seed, soil, fert, water, light, temp, hum, loc])

            seed += 1

    def solution(self):
        self.build_maps()
        # print(self.seeds)
        # print(self.maps)

        self.closest_location = float('inf')

        for seed in self.seeds:
            self.solve_for_seed(seed)

        return self.closest_location

    def build_maps(self):
        self.seeds = []
        self.maps = {}
        current_map = None
        for line in self.input:
            if line == "":
                continue

            if line.startswith("seeds: "):
                self.seeds = [int(x) for x in line.split(" ")[1:]]

                continue

            if line.endswith(" map:"):
                current_map = line.split(" ")[0]
                continue

            if current_map not in self.maps.keys():
                self.maps[current_map] = Map(current_map)

            self.maps[current_map].add_range([int(x) for x in line.split(" ")])


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda l:l.strip())
    print(puzzle.solution())

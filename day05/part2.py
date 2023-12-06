#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2023"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import math
from copy import copy
from multiprocessing import Pool

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
            if source_id < map_range[1] or source_id > (map_range[1] + map_range[2] -1):
                continue

            # print("%s matched range: %s" % (source_id, map_range))

            return map_range[0] + (source_id - map_range[1])

        return source_id

    def __repr__(self):
        return "%s-to-%s Map with %d ranges" % (self.source, self.destination, len(self.ranges))

class SeedRange():
    ranges: list
    limit = float("inf")

    def __init__(self, limit):
        self.ranges = []
        self.limit = math.ceil(limit)

    def add_range(self, offset, limit):
        current_total = sum([x[1] for x in self.ranges])
        # print((current_total + limit, self.limit))
        if current_total + limit > self.limit:
            take = self.limit - current_total
            self.ranges.append([offset, take])

            return offset + take, limit - take
        else:
            self.ranges.append([offset, limit])
            return None, None

    def __repr__(self):
        return "SeedRange %s limit %d has ranges %s totalling %d" % (id(self), self.limit, self.ranges, sum([x[1] for x in self.ranges]))

def solve_for_seed_range(maps, seed_range: SeedRange):
    closest_location = float("inf")

    for range_frag in seed_range.ranges:
        seed = range_frag[0]

        while seed < range_frag[0] + range_frag[1]:
            soil = maps["seed-to-soil"].source_to_destination(seed)
            fert = maps["soil-to-fertilizer"].source_to_destination(soil)
            water = maps["fertilizer-to-water"].source_to_destination(fert)
            light = maps["water-to-light"].source_to_destination(water)
            temp = maps["light-to-temperature"].source_to_destination(light)
            hum = maps["temperature-to-humidity"].source_to_destination(temp)
            loc = maps["humidity-to-location"].source_to_destination(hum)

            closest_location = min(loc, closest_location)

            # print([seed, soil, fert, water, light, temp, hum, loc])

            seed += 1

    # print(closest_location)
    return closest_location


class Puzzle(Base):
    threads: int = 10

    def solution(self):
        self.build_maps()
        print("Maps built")
        print(self.seeds)
        # print(self.maps)

        print("Pool started")
        with Pool(self.threads) as pool:
            locations = pool.starmap(solve_for_seed_range, [(self.maps, seed_range) for seed_range in self.seeds])

        print("Pool finished")
        print(locations)
        return ("Closest location is %d" % min(locations))

    def build_maps(self):
        self.seeds = []
        self.maps = {}
        current_map = None
        for line in self.input:
            if line == "":
                continue

            if line.startswith("seeds: "):
                seed_pairs = [int(x) for x in line.split(" ")[1:]]
                average_range_length = sum([seed_pairs[i] for i in range(1, len(seed_pairs), 2)]) / self.threads
                print("%f seeds per thread" % average_range_length)

                seed_range = SeedRange(average_range_length)
                for i in range(0, len(seed_pairs), 2):
                    new_offset, new_limit = seed_range.add_range(seed_pairs[i], seed_pairs[i+1])

                    while new_offset is not None and new_limit is not None:
                        self.seeds.append(seed_range)
                        seed_range = SeedRange(average_range_length)
                        new_offset, new_limit = seed_range.add_range(new_offset, new_limit)

                if len(seed_range.ranges) > 0:
                    self.seeds.append(seed_range)

                for seed in self.seeds:
                    print(seed)

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

from dataclasses import dataclass
from enum import Enum

DIAL_SIZE = 100

class Direction(Enum): 
    LEFT = 'L'
    RIGHT = 'R'

@dataclass
class Rotation:
    direction: Direction
    steps: int

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    rotations = []
    for line in lines:
        direction = Direction.LEFT if line[0] == 'L' else Direction.RIGHT
        steps = int(line[1:])
        rotations.append(Rotation(direction, steps))
    return rotations

def apply_rotation(pos, rotation):
    delta = 1 if rotation.direction == Direction.RIGHT else -1
    hit_zero = 0
    for _ in range(rotation.steps):
        pos += delta
        pos %= DIAL_SIZE
        if pos == 0:
            hit_zero += 1
    return pos, hit_zero

def part1():
    rotations = load_input()
    pos = 50
    ans = 0
    for r in rotations:
        pos, _ = apply_rotation(pos, r)
        if pos == 0:
            ans += 1
    return ans

def part2():
    rotations = load_input()
    pos = 50
    ans = 0
    for r in rotations:
        pos, hit_zero = apply_rotation(pos, r)
        ans += hit_zero
    return ans

# print(part1())
print(part2())
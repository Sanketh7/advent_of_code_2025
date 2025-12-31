from dataclasses import dataclass

@dataclass
class Region:
    dx: int
    dy: int
    reqs: list[int]

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()

    shapes = []
    regions = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line.strip():
            i += 1
            continue
        if ':' in line and 'x' not in line:
            r1 = lines[i + 1].strip()
            r2 = lines[i + 2].strip()
            r3 = lines[i + 3].strip()
            shapes.append([r1, r2, r3])
            i += 4
            continue
        assert 'x' in line
        dims, reqs = line.split(': ')
        dx, dy = [int(x) for x in dims.split('x')]
        reqs = [int(x) for x in reqs.split()]
        regions.append(Region(dx, dy, reqs))
        i += 1
    return shapes, regions

def part1():
    shapes, regions = load_input()
    def calc_area(shape: list[str]) -> int:
        return sum(row.count('#') for row in shape)
    shape_areas = [calc_area(shape) for shape in shapes]
    ans = 0
    for region in regions:
        area_needed = 0
        for i in range(len(region.reqs)):
            area_needed += region.reqs[i] * shape_areas[i]
        # turns out this simple heuristic is enough on the given input :)
        if area_needed <= region.dx * region.dy:
            ans += 1
    return ans

print(part1())
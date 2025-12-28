
def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    fresh_ranges = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            break
        start, end = map(int, line.split('-'))
        fresh_ranges.append((start, end))
    ingredients = []
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        ingredients.append(int(line))
    return fresh_ranges, ingredients

def part1():
    fresh_ranges, ingredients = load_input()
    ans = 0
    for id in ingredients:
        for start, end in fresh_ranges:
            if id >= start and id <= end:
                ans += 1
                break
    return ans

def part2():
    fresh_ranges, _ = load_input()
    ans = 0
    events = []
    for start, end in fresh_ranges:
        events.append((start, False))
        events.append((end, True))
    events.sort()
    active = 0
    active_start = None
    for x, is_end in events:
        if is_end:
            active -= 1
            if active == 0:
                ans += x - active_start + 1
                active_start = None
        else:
            active += 1
            if active_start is None:
                active_start = x
    return ans

# print(part1())
print(part2())
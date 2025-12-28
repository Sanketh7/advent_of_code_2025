from collections import Counter

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def advance(grid, i, j):
    if i + 1 >= len(grid):
        return []
    if grid[i+1][j] == '.':
        return [j]
    if grid[i+1][j] == '^':
        return [j-1, j+1]

def part1():
    grid = load_input()
    cols = set([grid[0].index('S')])
    splits = 0
    for i in range(1, len(grid)-1):
        new_cols = set()
        for j in cols:
            nxt = advance(grid, i, j)
            if len(nxt) > 1:
                splits += 1
            new_cols.update(nxt)
        cols = new_cols
    return splits

def part2():
    grid = load_input()
    cols = Counter([grid[0].index('S')])
    timelines = 1
    for i in range(1, len(grid)-1):
        new_cols = Counter()
        for j, cnt in cols.items():
            nxt = advance(grid, i, j)
            if len(nxt) > 1:
                timelines += cnt
            tmp = Counter(nxt)
            new_cols += Counter({k: v * cnt for k, v in tmp.items()})
        cols = new_cols
    return timelines

# print(part1())
print(part2())
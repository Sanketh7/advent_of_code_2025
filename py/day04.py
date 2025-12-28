from collections import deque

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]

dirs = []
for di in [-1, 0, 1]:
    for dj in [-1, 0, 1]:
        if di == 0 and dj == 0:
            continue
        dirs.append((di, dj))

def count_adj(grid, i, j):
    ans = 0
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[ni]):
            if grid[ni][nj] == '@':
                ans += 1
    return ans

def accessible(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
        return False
    if grid[i][j] != '@':
        return False
    return count_adj(grid, i, j) < 4

def part1():
    grid = load_input()
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if accessible(grid, i, j):
                ans += 1
    return ans

def part2():
    grid = load_input()
    m = len(grid)
    n = len(grid[0])
    ans = [[False for _ in range(n)] for _ in range(m)]
    todo = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                todo.append((i, j))

    while len(todo) > 0:
        i, j = todo.popleft()
        if accessible(grid, i, j):
            ans[i][j] = True
            grid[i][j] = '.'
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                todo.append((ni, nj))
            
    return sum(1 for row in ans for val in row if val)

# print(part1())
print(part2())
from collections import deque

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    points = []
    for line in lines:
        x, y = map(int, line.strip().split(','))
        points.append((x, y))
    return points

def part1():
    points = load_input()
    ans = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dx = abs(points[i][0] - points[j][0]) + 1
            dy = abs(points[i][1] - points[j][1]) + 1
            ans = max(ans, dx * dy)
    return ans

def compress_points(points):
    xs = sorted(set(x for x, y in points))
    ys = sorted(set(y for x, y in points))
    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}
    return x_map, y_map

def part2():
    points = load_input()
    x_map, y_map = compress_points(points)
    max_x = max(x_map.values())
    max_y = max(y_map.values())

    compressed_points = [(x_map[x], y_map[y]) for x, y in points]
    grid = [[False for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    def connect(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for j in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][j] = True
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                grid[j][y1] = True
        else:
            assert False
    for i in range(1, len(compressed_points)):
        connect(compressed_points[i - 1], compressed_points[i])
    connect(compressed_points[-1], compressed_points[0])

    source = None
    for i in range(1, len(compressed_points) - 1):
        px, py = compressed_points[i - 1]
        x, y = compressed_points[i]
        nx, ny = compressed_points[i + 1]
        if px != x and py == y and nx == x and ny != y:
            dx = (px - x) // abs(px - x)
            dy = (ny - y) // abs(ny - y)
            source = (x + dx, y + dy)
            break
    assert source is not None

    q = deque()
    q.append(source)
    while q:
        x, y = q.popleft()
        if grid[x][y]:
            continue
        grid[x][y] = True
        for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            q.append((nx, ny))    

    prefix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    prefix[0][0] = 1 if grid[0][0] else 0
    for x in range(1, len(grid)):
        prefix[x][0] = prefix[x-1][0] + (1 if grid[x][0] else 0)
    for y in range(1, len(grid[0])):
        prefix[0][y] = prefix[0][y-1] + (1 if grid[0][y] else 0)
    for x in range(1, len(grid)):
        for y in range(1, len(grid)):
            prefix[x][y] = (1 if grid[x][y] else 0) + prefix[x-1][y] + prefix[x][y-1] - prefix[x-1][y-1]
    def get_prefix(x, y):
        if x < 0 or x >= len(prefix) or y < 0 or y >= len(prefix[x]):
            return 0
        return prefix[x][y]
    
    max_area = 0
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            pi = points[i]
            pj = points[j]
            area = (abs(pi[0] - pj[0]) + 1) * (abs(pi[1] - pj[1]) + 1)
            pic = (x_map[pi[0]], y_map[pi[1]])
            pjc = (x_map[pj[0]], y_map[pj[1]])

            x_lo, x_hi = min(pic[0], pjc[0]), max(pic[0], pjc[0])
            y_lo, y_hi = min(pic[1], pjc[1]), max(pic[1], pjc[1])

            num_filled = get_prefix(x_hi, y_hi) - get_prefix(x_lo - 1, y_hi) - get_prefix(x_hi, y_lo -1) + get_prefix(x_lo - 1, y_lo - 1)
            expected = (x_hi - x_lo + 1) * (y_hi - y_lo + 1)
            if num_filled == expected:
                max_area = max(max_area, area)
    return max_area


# print(part1())
print(part2())

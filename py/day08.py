import math
from dataclasses import dataclass

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    points = []
    for line in lines:
        x, y, z = map(int, line.strip().split(','))
        points.append((x, y, z))
    return points

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]
            return True
        return False

@dataclass
class Edge:
    u: int
    v: int
    dist: int

def calc_dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return dx*dx + dy*dy + dz*dz

def part1():
    points = load_input()
    dsu = DSU(len(points))

    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = calc_dist(points[i], points[j])
            edges.append(Edge(i, j, dist))
    edges.sort(key=lambda e: e.dist)

    for edge in edges[:1000]:
        dsu.union(edge.u, edge.v)

    sorted_sizes = sorted(dsu.size, reverse=True)
    return math.prod(sorted_sizes[:3])

def part2():
    points = load_input()
    dsu = DSU(len(points))

    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = calc_dist(points[i], points[j])
            edges.append(Edge(i, j, dist))
    edges.sort(key=lambda e: e.dist)

    connections = 0
    for edge in edges:
        if dsu.union(edge.u, edge.v):
            connections += 1
        if connections == len(points) - 1:
            return points[edge.u][0] * points[edge.v][0]
    return None

# print(part1())
print(part2())

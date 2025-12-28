import math
from dataclasses import dataclass

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    grid = []
    for line in lines[:-1]:
        row = [x.strip() for x in line.strip().split()]
        row = [int(x) for x in row if x]
        grid.append(row)
    ops = [x.strip() for x in lines[-1].strip().split()]
    ops = [x for x in ops if x]
    return grid, ops

@dataclass
class Number:
    digit_and_cols: list[(int, int)]

def load_input2():
    with open('input.txt') as f:
        lines = f.readlines()
    grid = []
    for line in lines[:-1]:
        line = line.rstrip()
        row = []
        digit_and_cols = []
        for i in range(len(line)):
            if line[i] == ' ':
                if digit_and_cols:
                    row.append(Number(digit_and_cols[:]))
                    digit_and_cols.clear()
                continue
            digit_and_cols.append((int(line[i]), i))
        if digit_and_cols:
            row.append(Number(digit_and_cols[:]))
        grid.append(row)
    ops = [x.strip() for x in lines[-1].strip().split()]
    ops = [x for x in ops if x]
    return grid, ops

def part1():
    grid, ops = load_input()
    ans = 0
    for j in range(len(grid[0])):
        vals = []
        for i in range(len(grid)):
            vals.append(grid[i][j])
        op = ops[j]
        if op == '+':
            ans += sum(vals)
        elif op == '*':
            ans += math.prod(vals)
    return ans

def part2():
    grid, ops = load_input2()
    ans = 0
    for j in range(len(grid[0])):
        nums = []
        min_col, max_col = float('inf'), -float('inf')
        for i in range(len(grid)):
            num = grid[i][j]
            for _, col in num.digit_and_cols:
                min_col = min(min_col, col)
                max_col = max(max_col, col)
            nums.append(num)
        vals = []
        for col in range(min_col, max_col + 1):
            val = 0
            for num in nums:
                for digit, dcol in num.digit_and_cols:
                    if dcol == col:
                        val = val * 10 + digit
            if val > 0:
                vals.append(val)
        op = ops[j]
        if op == '+':
            ans += sum(vals)
        elif op == '*':
            ans += math.prod(vals)
    return ans

# print(part1())
print(part2())
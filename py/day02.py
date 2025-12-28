
def load_input():
    with open('input.txt') as f:
        line = f.readline().strip()
    ranges = []
    for range in line.split(','):
        start, end = map(int, range.split('-'))
        ranges.append((start, end))
    return ranges

def is_invalid(x, k):
    s = str(x)
    n = len(s)
    if n % k != 0:
        return False
    stride = n // k
    for i in range(n):
        if i + stride >= n:
            break
        if s[i] != s[i + stride]:
            return False
    return True

def is_invalid_complex(x):
    n = len(str(x))
    for k in range(2, n+1):
        if is_invalid(x, k):
            return True
    return False

def part1():
    ranges = load_input()
    ans = 0
    for start, end in ranges:
        for x in range(start, end + 1):
            if is_invalid(x, 2):
                ans += x
    return ans

def part2():
    ranges = load_input()
    ans = 0
    for start, end in ranges:
        for x in range(start, end + 1):
            if is_invalid_complex(x):
                ans += x
    return ans

# print(part1())
print(part2())
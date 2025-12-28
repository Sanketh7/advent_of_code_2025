from functools import cache

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    banks = []
    for line in lines:
        banks.append(list(map(int, list(line.strip()))))
    return banks

def part1():
    banks = load_input()
    ans = 0
    for bank in banks:
        n = len(bank)
        max_jolt = 0
        for i in range(n):
            for j in range(i+1, n):
                jolt = bank[i] * 10 + bank[j]
                max_jolt = max(max_jolt, jolt)
        ans += max_jolt
    return ans

def calc_jolt(bank):
    n = len(bank)
    dp = [[0 for _ in range(n)] for _ in range(13)]
    dp[1][0] = bank[0]

    for i in range(1, n):
        for k in range(1, 12+1):
            dp[k][i] = max(dp[k][i], dp[k-1][i-1] * 10 + bank[i], dp[k][i-1])
    return max(dp[12])

def part2():
    banks = load_input()
    ans = 0
    for bank in banks:
        ans += calc_jolt(bank)
    return ans

# print(part1())
print(part2())

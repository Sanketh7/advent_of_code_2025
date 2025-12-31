from functools import cache

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    adj = dict()
    for line in lines:
        src, dests = line.split(':')
        dests = list(dests.strip().split())
        adj[src] = dests
    return adj

def part1():
    adj = load_input()
    @cache
    def count_paths(u: str) -> int:
        if u == 'out':
            return 1
        if u not in adj:
            return 0
        paths = 0
        for v in adj[u]:
            paths += count_paths(v)
        return paths
    return count_paths('you')

def part2():
    adj = load_input()
    @cache
    def count_paths(u: str, target: str) -> int:
        if u == target:
            return 1
        if u not in adj:
            return 0
        paths = 0
        for v in adj[u]:
            paths += count_paths(v, target)
        return paths
    svr_to_dac = count_paths('svr', 'dac')
    svr_to_fft = count_paths('svr', 'fft')
    dac_to_fft = count_paths('dac', 'fft')
    fft_to_dac = count_paths('fft', 'dac')
    dac_to_out = count_paths('dac', 'out')
    fft_to_out = count_paths('fft', 'out')
    svr_dac_fft_out = svr_to_dac * dac_to_fft * fft_to_out
    svr_fft_dac_out = svr_to_fft * fft_to_dac * dac_to_out
    return svr_dac_fft_out + svr_fft_dac_out

# print(part1())
print(part2())
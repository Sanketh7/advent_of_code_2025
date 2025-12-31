from dataclasses import dataclass
from z3 import Int, Solver, Sum, sat

@dataclass
class Machine:
    lights: list[bool]
    buttons: list[list[int]]
    joltage_reqs: list[int]

def load_input():
    with open('input.txt') as f:
        lines = f.readlines()
    machines = []
    for line in lines:
        lights = []
        buttons = []
        joltage_reqs = []
        for part in line.strip().split():
            if part.startswith('['):
                assert not lights
                lights = [c == '#' for c in part[1:-1]]
            elif part.startswith('('):
                buttons.append([int(x) for x in part[1:-1].split(',')])
            elif part.startswith('{'):
                assert not joltage_reqs
                joltage_reqs = [int(x) for x in part[1:-1].split(',')]
        machines.append(Machine(lights, buttons, joltage_reqs))
    return machines

def part1():
    machines = load_input()

    def process_machine(machine: Machine) -> int:
        fewest = float('inf')
        for mask in range(1 << len(machine.buttons)):
            state = [False] * len(machine.lights)
            presses = 0
            for i in range(len(machine.buttons)):
                if (mask >> i) & 1:
                    presses += 1
                    for x in machine.buttons[i]:
                        state[x] = not state[x]
            if state == machine.lights:
                fewest = min(fewest, presses)
        assert fewest <= len(machine.buttons)
        return fewest

    return sum(process_machine(machine) for machine in machines)

def part2():
    machines = load_input()

    def process_machine(machine: Machine, presses: int) -> int:
        n = len(machine.buttons)
        xs = [Int(f'x{i}') for i in range(n)]
        s = Solver()
        for j in range(len(machine.joltage_reqs)):
            coeffs = [j in btn for btn in machine.buttons]
            assert len(coeffs) == len(xs) == n
            s.add(Sum(coeffs[i] * xs[i] for i in range(n)) == machine.joltage_reqs[j])
        for x in xs:
            s.add(x >= 0)
        s.add(Sum(xs) == presses)
        return s.check() == sat

    ans = 0
    for machine in machines:
        max_presses = sum(machine.joltage_reqs)
        found = False
        for presses in range(1, max_presses + 1):
            if process_machine(machine, presses):
                ans += presses
                found = True
                break
        assert found
    return ans

# print(part1())
print(part2())
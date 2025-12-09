from utils import *
from math import sqrt, prod

def euc_distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b

    return sqrt((x2 - x1)**2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def solution(lines : list[str]):
    distances = {}

    for i, first in enumerate(lines):
        first = tuple(map(int, first.split(",")))
        for second in lines[i+1:]:
            second = tuple(map(int, second.split(",")))
            distances[(first, second)] = euc_distance(first, second)

    distances = sorted(distances.items(), key = lambda x: x[1])
    circuits : list[set] = []

    num_to_connect = 1000

    for i in range(num_to_connect):
        (a, b), _ = distances[i]

        a_already_in, b_already_in = False, False

        for circuit in circuits:
            if not a_already_in and a in circuit:
                a_already_in = circuit
            if not b_already_in and b in circuit:
                b_already_in = circuit
            if a_already_in and b_already_in:
                break

        if a_already_in == False and b_already_in == False:
            circuits.append({a, b})
        elif a_already_in and not b_already_in:
            a_already_in.add(b)
        elif b_already_in and not a_already_in:
            b_already_in.add(a)
        elif a_already_in == b_already_in:
            continue # Not sure why this can happen, probably not pruning well enough
        else:
            new_set = a_already_in.union(b_already_in)
            circuits.remove(a_already_in)
            circuits.remove(b_already_in)
            circuits.append(new_set)
        
    circuits.sort(key = len, reverse = True)

    return prod([len(circuit) for circuit in circuits[:3]])

if __name__ == "__main__":
    lines = read_input("2025/day8_input.txt")

    print(solution(lines))
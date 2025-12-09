from utils import *
from math import sqrt

def euc_distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b

    return sqrt((x2 - x1)**2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def solution(lines : list[str]):
    distances = {}
    circuits : list[set] = []
    for i, first in enumerate(lines):
        first = tuple(map(int, first.split(",")))
        if not {first} in circuits:
            circuits.append({first})
        for second in lines[i+1:]:
            second = tuple(map(int, second.split(","))) 
            distances[(first, second)] = euc_distance(first, second)

    distances = sorted(distances.items(), key = lambda x: x[1])

    for i in range(len(distances)):
        (a, b), _ = distances[i]

        a_circuit, b_circuit = False, False
        for circuit in circuits:
            if a in circuit:
                a_circuit = circuit
            if b in circuit:
                b_circuit = circuit
            if a_circuit and b_circuit:
                break

        if a_circuit == b_circuit: continue

        if len(circuits) == 2:
            return a[0] * b[0]
        
        new_circuit = a_circuit.union(b_circuit)
        circuits.remove(a_circuit)
        circuits.remove(b_circuit)
        circuits.append(new_circuit)
    return 0

if __name__ == "__main__":
    lines = read_input("2025/day8_input.txt")

    print(solution(lines))
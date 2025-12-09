from utils import *


def manhattan_distance(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def solution(lines : list[str]):
    total = 0

    distances = []
    for i, line_a in enumerate(lines):
        a = tuple(map(int, line_a.split(",")))
        for line_b in lines[i + 1:]:
            b = tuple(map(int, line_b.split(",")))
            distance = manhattan_distance(a, b)
            distances.append(distance)
    
    return max(distances)


    return total

if __name__ == "__main__":
    lines = read_input("2025/day9_input.txt")

    example = ["7, 1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3"]

    print(solution(example))

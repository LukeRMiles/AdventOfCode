from utils import *

def solution(lines : list[str]):
    total = 0
    print(lines)
    ranges = []

    ingredient_freshness = lines.index("")
    for line in lines[:ingredient_freshness]:
        start_index, end_index = map(int, line.split("-"))
        ranges.append((start_index, end_index))

    for line in lines[ingredient_freshness + 1:]:
        id = int(line)
        for fresh_pair in ranges:
            start, end = fresh_pair
            if id >= start and id <= end:
                total += 1
                break
    return total

if __name__ == "__main__":
    lines = read_input("2025/day5_input.txt")

    print(solution(lines))

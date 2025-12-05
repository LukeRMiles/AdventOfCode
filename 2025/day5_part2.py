from utils import *

def solution(lines: list[str]):
    ranges = []

    ingredient_freshness = lines.index("")

    for line in lines[:ingredient_freshness]:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ranges.sort()

    merged = []
    curr_start, curr_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= curr_end:
            if end > curr_end:
                curr_end = end
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = start, end

    merged.append((curr_start, curr_end))

    total = sum(end - start + 1 for start, end in merged)
    return total

if __name__ == "__main__":
    lines = read_input("2025/day5_input.txt")

    print(solution(lines))
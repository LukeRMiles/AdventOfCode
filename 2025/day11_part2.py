from utils import *
import functools

paths : dict[list] = {}

@functools.cache
def recurse(index_into_paths, has_taken_dac, has_taken_fft):
    if index_into_paths == "out":
        if has_taken_dac and has_taken_fft:
            return 1
        return 0
    elif index_into_paths == "dac":
        total = 0
        for next_path in paths[index_into_paths]:
            total += recurse(next_path, True, has_taken_fft)
        return total
    elif index_into_paths == "fft":
        total = 0
        for next_path in paths[index_into_paths]:
            total += recurse(next_path, has_taken_dac, True)
        return total
    total = 0
    for next_path in paths[index_into_paths]:
        total += recurse(next_path, has_taken_dac, has_taken_fft)
    return total

def solution(lines : list[str]):
    for line in lines:
        source = line.split(":")[0]
        targets = line.split(":")[1].split()

        if source in paths:
            for target in targets:
                paths[source].append(target)
        else:
            paths[source] = targets

    total = recurse("svr", False, False)

    return total

if __name__ == "__main__":
    lines = read_input("2025/day11.txt")

    print(solution(lines))

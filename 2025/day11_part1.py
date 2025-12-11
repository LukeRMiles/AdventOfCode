from utils import *

def recurse(found, paths, index_into_paths):
    if index_into_paths == "out": return found + 1

    for next_step in paths[index_into_paths]:
        found = recurse(found, paths, next_step)

    return found

def solution(lines : list[str]):
    total = 0

    paths : dict[list]= {}

    for line in lines:
        source = line.split(":")[0]
        targets = line.split(":")[1].split()

        if source in paths:
            for target in targets:
                paths[source].append(target)
        else:
            paths[source] = targets

    total = recurse(0, paths, "you")

    return total

if __name__ == "__main__":
    lines = read_input("2025/day11_input.txt")

    print(solution(lines))

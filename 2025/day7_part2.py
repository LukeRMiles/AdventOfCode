from utils import *

def solution(lines : list[str]):
    starting_index = lines[0].index("S")

    visited_cells : dict = {starting_index : 1}

    for i in range(1, len(lines) - 1):
        for index in range(len(lines[i])):
            if lines[i][index] == ".": continue

            if index in visited_cells:
                if index + 1 in visited_cells:
                    visited_cells[index + 1] += visited_cells[index]
                else:
                    visited_cells[index + 1] = visited_cells[index]

                if index - 1 in visited_cells:
                    visited_cells[index - 1] += visited_cells[index]
                else:
                    visited_cells[index - 1] = visited_cells[index]
                del visited_cells[index]

    return sum(visited_cells.values())

if __name__ == "__main__":
    lines = read_input("2025/day7_input.txt")

    print(solution(lines))

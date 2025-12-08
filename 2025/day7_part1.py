from utils import *

def solution(lines : list[str]):
    total = 0

    starting_index = lines[0].index("S")

    next_beams = set()
    next_beams.add((1, starting_index))

    for i in range(1, len(lines)-1):
        future_beams = set()

        for (beam_x, beam_y) in next_beams:
            right_below = lines[beam_x+1][beam_y]

            if right_below == ".":
                future_beams.add((beam_x + 1, beam_y))
            elif right_below == "^":
                total += 1
                future_beams.add((beam_x + 1, beam_y - 1))
                future_beams.add((beam_x + 1, beam_y + 1))
        next_beams = future_beams
    return total

if __name__ == "__main__":
    lines = read_input("2025/day7_input.txt")

    print(solution(lines))

def get_number_of_adjacent_rolls(lines, x, y):
    total = 0
    offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0,  -1),          (0, 1),
        (1,  -1), (1,  0), (1, 1)
    ]

    for (x_offset, y_offset) in offsets:
        x_index = x + x_offset
        y_index = y + y_offset

        if 0 > x_index or x_index > len(lines) -1:
            continue
        if 0 > y_index or y_index > len(lines[0]) -1:
            continue 

        if lines[x_index][y_index] == "@":
            total += 1
    return total

def solution(lines : list[str]):
    total = 0

    for line_x, line in enumerate(lines):
        for line_y, char in enumerate(line):
            if char == "@":
                if get_number_of_adjacent_rolls(lines, line_x, line_y) < 4:
                    total += 1
    return total

if __name__ == "__main__":
    lines = [line.strip() for line in open("day4_input.txt", 'r').readlines()]

    print(solution(lines))
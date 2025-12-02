import math

def is_invalid_id(num):
    part1 = str(num)[0:math.floor(len(str(num)) / 2)]
    part2 = str(num)[math.floor(len(str(num)) / 2):]
    return part1 == part2

def solution(line):
    ids = line.split(",")
    total = 0
    for id_range in ids:
        beginning = int(id_range.split("-")[0])
        end = int(id_range.split("-")[1])
        for i in range(beginning, end):
            if is_invalid_id(i):
                total += i
    return total

if __name__ == "__main__":
    input = open("day2_input.txt", 'r').readline()
    print(solution(input))
import re

def is_invalid_id(num):
    return bool(re.fullmatch(r"(\d+)\1+", num))

def solution(line):
    ids = line.split(",")
    total = 0
    for id_range in ids:
        beginning = int(id_range.split("-")[0])
        end = int(id_range.split("-")[1])
        for i in range(beginning, end):
            if is_invalid_id(str(i)):
                total += i
    return total

if __name__ == "__main__":
    input = open("day2_input.txt", 'r').readline()
    print(solution(input))
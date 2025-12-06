from utils import *

def solution(lines : list[str]):
    first_nums = [int(num.strip()) for num in lines[0].strip().split() if num.strip() != ""]
    second_nums = [int(num.strip()) for num in lines[1].strip().split() if num.strip() != ""]
    third_nums = [int(num.strip()) for num in lines[2].strip().split() if num.strip() != ""]
    fourth_nums = [int(num.strip()) for num in lines[3].strip().split() if num.strip() != ""]
    operations = [op.strip() for op in lines[4].split(" ") if op.strip() != ""]
    print(operations)
    total = 0
    for i in range(len(first_nums)):
        if operations[i] == "+":
            step = first_nums[i] + second_nums[i] + third_nums[i] + fourth_nums[i]
            total += step
        elif operations[i] == "*":
            step =  first_nums[i] * second_nums[i] * third_nums[i] * fourth_nums[i]
            total += step
    return total

if __name__ == "__main__":
    lines = read_input("2025/day6_input.txt")

    example = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "6 98  215 314",
        "*   +   *   + ",
    ]

    print(solution(lines))
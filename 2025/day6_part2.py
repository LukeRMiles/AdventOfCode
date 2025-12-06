from utils import *
import math

def resolve_group(operation : str, nums : list):
    if operation == "+":
        return sum(nums)
    elif operation == "*":
        return math.prod(nums)

def solution(lines : list[str]):
    group_count = 0 # Used to track which group we're on for easy indexing into their operation
    operations = [op.strip() for op in lines[4].split(" ") if op.strip() != ""]
    all_lines = [lines[0], lines[1], lines[2], lines[3]]
    total = 0

    current_nums = [] # track the current groups column numbers
    for i in range(len(lines[0])):
        digits = [line[i] for line in all_lines]
        if all([(digit == " ") for digit in digits]): 
            # Once we hit a column of " ", resolve group and move on
            total += resolve_group(operations[group_count], current_nums)
            current_nums = []
            group_count += 1
            continue
        num_to_build = int("".join(digits))
        current_nums.append(num_to_build)

    total += resolve_group(operations[group_count], current_nums) # Deal with last group

    return total

if __name__ == "__main__":
    lines = read_input("2025/day6_input.txt")
    print(solution(lines))
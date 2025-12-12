from utils import *
import itertools

def format_line(line: str):
    line = line.strip()

    light_goal = line[1:line.index("]")]
    operations = line[line.index("]") + 2: line.index("{") - 1]
    other_thing = line[line.index("{") + 1: len(line) - 1]

    buttons = []
    for operation in operations.split():
        button = eval(operation)

        if not isinstance(button, tuple):
            button = (button,)
        buttons.append(button)

    return light_goal, buttons, other_thing

def apply_button(lights : str, button):
    lights = [light for light in lights]
    for index in button:
        lights[index] = "#" if lights[index] == "." else "."
    return "".join(lights)

def all_combinations(any_list):
    return list(itertools.chain.from_iterable(
        itertools.combinations(any_list, i) 
        for i in range(len(any_list) + 1))
    )

def solve_line(goal: str, buttons: list[tuple]):
    for combo in all_combinations(buttons):
        print(combo)
        result = "." * len(goal)
        for button in combo:
            result = apply_button(result, button)
        print(result, goal)
        if result == goal:
            return len(combo)
    return 0

def solution(lines: list[str]):
    total = 0
    for line in lines:
        light_goal, buttons, _ = format_line(line)
        total += solve_line(light_goal, buttons)
    return total

if __name__ == "__main__":
    lines = read_input("2025/day10_input.txt")
    example = read_input("2025/day10_example.txt")

    print(solution(lines))
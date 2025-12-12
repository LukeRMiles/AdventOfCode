from utils import *
from z3 import Int, Optimize, Sum, sat

def format_line(line: str):
    line = line.strip()
    light_goal = line[1:line.index("]")]
    operations = line[line.index("]") + 2: line.index("{") - 1]
    goal_counts = list(map(int, line[line.index("{") + 1: len(line) - 1].split(",")))

    buttons = []
    for operation in operations.split():
        button = eval(operation)
        if not isinstance(button, tuple):
            button = (button,)
        buttons.append(button)

    return light_goal, buttons, goal_counts

def z3_solve(buttons : list[tuple], goal : list):
    light_count  = len(goal)
    button_count = len(buttons)
    opt = Optimize()

    button_vars = [Int(f"x{i}") for i in range(button_count)]

    for button_var in button_vars:
        opt.add(button_var >= 0) # No negative button presses

    for i in range(light_count):
        affect_light = [button_vars[j] for j, b in enumerate(buttons) if i in b]

        if not affect_light:
            opt.add(goal[i] == 0)
        else:
            opt.add(Sum(affect_light) == goal[i])

    opt.minimize(Sum(button_vars))

    if opt.check() != sat:
        print("UH OH")
        return -99999

    model = opt.model()
    return sum(model.eval(result).as_long() for result in button_vars)

def solution(lines: list[str]):
    total = 0
    for line in lines:
        _, buttons, goal = format_line(line)
        total += z3_solve(buttons, goal)
    return total

if __name__ == "__main__":
    lines = read_input("2025/day10_input.txt")
    example = read_input("2025/day10_example.txt")
    print(solution(lines))

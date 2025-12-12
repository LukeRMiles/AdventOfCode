from utils import *

def parse_input(lines : list[str]):
    shape_dict = {}
    for i in range(0, 30, 5):
        index = int(lines[i][0])

        shape1 = lines[i + 1]
        shape2 = lines[i + 2]
        shape3 = lines[i + 3]

        shape_offsets = []
        for i, line in enumerate((shape1, shape2, shape3)):
            i -= 1
            for j, char in enumerate(line):
                j -= 1
                if char == "#":
                    shape_offsets.append((i, j))
        shape_dict[index] = shape_offsets
    
    tree_infos : list[(tuple, list)] = []
    for i in range(30, len(lines)):
        line = lines[i]
        n = int(line[:line.index("x")])
        m = int(line[line.index("x") + 1 : line.index(":")])
        shapes = list(map(int, line.split(":")[1].split()))
        tree_infos.append(((n, m), shapes))

    return shape_dict, tree_infos
        
def solution(lines : list[str]):
    total = 0

    shape_dict, tree_infos = parse_input(lines)

    for ((n, m), present_list) in tree_infos:
        grid_area = n * m
        
        present_space = 0
        for i, val in enumerate(present_list):
            present_space += val * len(shape_dict[i])
    
        if present_space > grid_area:
            print("Not enough area")
        else:
            if present_space < grid_area and present_space * 1.1 > grid_area:
                print("Could be very close")
        if present_space < grid_area * 0.90: # wtf
            total += 1

    return total

if __name__ == "__main__":
    lines = read_input("2025/day12_input.txt")
    example = read_input("2025/day12_example.txt")

    print(solution(lines))

def solution(lines : list[str]):
    heading = 50
    total = 0
    started_from_zero = False
    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if distance > 99:
            total += distance // 100
            distance %= 100

        if direction == "L":
            heading -= distance
        elif direction == "R":
            heading += distance
        
        new_heading =  heading % 100

        if (not started_from_zero and new_heading != heading) or new_heading == 0:
            total += 1
        heading = new_heading
        if new_heading == 0:
            started_from_zero = True
        else:
            started_from_zero = False
    return total

if __name__ == "__main__":
    lines = [line.strip() for line in open("day1_input.in", 'r').readlines()]

    print(solution(lines))
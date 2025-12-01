def solution(lines : list[str]):
    heading = 50
    total = 0

    for line in lines:
        direction = line[0]
        distance = line[1:]

        if direction == "L":
            heading -= int(distance)
        elif direction == "R":
            heading += int(distance)
        heading %= 100

        if heading == 0:
            total += 1
        print(heading)
    return total

if __name__ == "__main__":
    lines = [line.strip() for line in open("day1_input.in", 'r').readlines()]

    print(solution(lines))
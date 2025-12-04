def my_solution(lines: list[str], n: int = 12):
    total = 0
    for line in lines:
        digits = [int(num) for num in line]
        result =  []
        start_index = 0
        for _ in range(n):
            remaining = n - len(result)

            max_index = len(digits) - remaining

            window = digits[start_index : max_index + 1]

            largest_digit = max(window)

            result.append(largest_digit)
            start_index = start_index + window.index(largest_digit) + 1
        total += int("".join(map(str, result)))
    return total

if __name__ == "__main__":
    lines = [line.strip() for line in open("day3_input.txt", 'r').readlines()]

    print(my_solution(lines))
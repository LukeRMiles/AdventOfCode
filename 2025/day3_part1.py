def solution(lines : list[str]):
    total = 0
    for line in lines:
        nums = [int(num) for num in line]

        biggest = max(nums)

        index_of_max = nums.index(biggest)

        if index_of_max == len(nums) - 1:
            next_biggest = max(nums[:index_of_max])
            num = int(str(next_biggest) + str(biggest))
        else:
            next_biggest = max(nums[index_of_max+1:])
            num = int(str(biggest) + str(next_biggest))
        total += num
    return total

if __name__ == "__main__":
    lines = [line.strip() for line in open("day3_input.txt", 'r').readlines()]

    print(solution(lines))
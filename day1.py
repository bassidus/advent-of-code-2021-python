def read_input():
    input = []
    with open('day1_input.txt') as file:
        for line in file:
            input.append(int(line))
    return input


def part_one(input):
    increase = 0
    prev_max = input[0]
    for v in input:
        if v > prev_max:
            increase += 1
        prev_max = v
    return increase


def part_two(input):
    increase = 0
    prev_max = sum(input[: 3])
    for i in range(len(input) - 2):
        result = sum(input[i: i + 3])
        if result > prev_max:
            increase += 1
        prev_max = result
    return increase


print('Part 1:', part_one(read_input()))
print('Part 2:', part_two(read_input()))

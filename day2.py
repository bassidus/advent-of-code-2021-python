from utils import fetch


def part_one(directions):
    horizontal = 0
    depth = 0
    for i in range(len(directions)):
        if directions[i] == 'forward':
            horizontal += int(directions[i + 1])
        elif directions[i] == 'down':
            depth += int(directions[i + 1])
        elif directions[i] == 'up':
            depth -= int(directions[i + 1])

    return f'Horizontal: {horizontal}, Depth: {depth}, Total: {horizontal * depth}'


def part_two(directions):
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(directions)):
        if directions[i] == 'forward':
            horizontal += int(directions[i + 1])
            depth += int(directions[i + 1]) * aim
        elif directions[i] == 'down':
            aim += int(directions[i + 1])
        elif directions[i] == 'up':
            aim -= int(directions[i + 1])

    return f'Horizontal: {horizontal}, Depth: {depth}, Total: {horizontal * depth}'


input = fetch('https://adventofcode.com/2021/day/2/input')
print(part_one(input))
print(part_two(input))

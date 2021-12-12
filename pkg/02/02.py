def get_input():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f]


def part_1():
    pos = sum([int(val) for cmd, val in [item.split() for item in get_input()] if cmd == 'forward'])
    depth = sum([int(val) if cmd == 'down' else -int(val) if cmd == 'up' else 0
                for cmd, val in [item.split() for item in get_input()]])
    return pos * depth


def part_2():
    pos = depth = aim = 0
    for cmd, val in [item.split() for item in get_input()]:
        val = int(val)
        if cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val
        else:
            pos += val
            depth += aim * val
    return pos * depth


print(part_1())
print(part_2())

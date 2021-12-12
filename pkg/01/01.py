def read_input():
    with open("input.txt", "r") as f:
        return [int(line.strip()) for line in f]


def part_1(depths):
    return sum([1 for i in range(len(depths)) if depths[i] > depths[i-1]])


def part_2(depths):
    return [(depths[i] + depths[i+1] + depths[i+2]) for i in range(len(depths) - 2)]


print(part_1(read_input()))
print(part_1(part_2(read_input())))
def parse_input():
    with open("input.txt", "r") as f:
        return [[[int(y) for y in x.split(',')] for x in line.strip().split(' -> ')]for line in f]


def find_vents():
    inputs = parse_input()
    part_a = {}
    part_b = {}
    for input in inputs:
        start_x, start_y = input[0]
        end_x, end_y = input[1]
        if start_x == end_x:
            if start_y > end_y: start_y, end_y = end_y, start_y
            for y in range(start_y, end_y + 1):
                part_a[(start_x, y)] = part_a.get((start_x, y), 0) + 1
                part_b[(start_x, y)] = part_b.get((start_x, y), 0) + 1
        elif start_y == end_y:
            if start_x > end_x: start_x, end_x = end_x, start_x
            for x in range(start_x, end_x + 1):
                part_a[(x, start_y)] = part_a.get((x, start_y), 0) + 1
                part_b[(x, start_y)] = part_b.get((x, start_y), 0) + 1
        else:
            x_step = 1 if start_x < end_x else -1
            y_step = 1 if start_y < end_y else -1
            cur_x, cur_y = start_x, start_y
            while (cur_x != end_x) & (cur_y != end_y):
                part_b[(cur_x, cur_y)] = part_b.get((cur_x, cur_y), 0) + 1
                cur_x += x_step
                cur_y += y_step
            part_b[(end_x, end_y)] = part_b.get((end_x, end_y), 0) + 1

    print(sum([v > 1 for v in part_a.values()]))
    print(sum([v > 1 for v in part_b.values()]))


find_vents()

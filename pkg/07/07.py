def get_positions():
    with open("input.txt", "r") as f:
        return sorted([int(x) for x in f.readline().strip().split(',')])


def get_median(positions):
    if len(positions) % 2 == 0:
        return (positions[int(len(positions) / 2)] + positions[int(len(positions) / 2) - 1]) / 2
    else:
        return positions[int(len/positions / 2)]


def get_mean(positions):
    return int(sum(positions) / len(positions))


positions = get_positions()
median = get_median(positions)
mean = get_mean(positions)

total_fuel_a = sum([abs(x - median) for x in positions])
total_fuel_b = sum([sum(range(1, abs(x - mean) + 1)) for x in positions])

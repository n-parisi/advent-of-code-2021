import sys


def get_tube_arr():
    with open("input.txt", "r") as f:
        return [[int(x) for x in [y for y in line.strip()]] for line in f]


tube_arr = get_tube_arr()
risk_level = 0
basins = []
marked = []
low_points = []


def get_basin_size(x, y, height):
    basin_size = 0
    if (x > 0) and (tube_arr[y][x - 1] != 9) and ((x - 1, y) not in marked):
        marked.append((x - 1, y))
        basin_size += 1 + get_basin_size(x - 1, y, height + 1)
    if (x < len(tube_arr[y]) - 1) and (tube_arr[y][x + 1] != 9) and ((x + 1, y) not in marked):
        marked.append((x + 1, y))
        basin_size += 1 + get_basin_size(x + 1, y, height + 1)
    if (y > 0) and (tube_arr[y - 1][x] != 9) and ((x, y - 1) not in marked):
        marked.append((x, y - 1))
        basin_size += 1 + get_basin_size(x, y - 1, height + 1)
    if (y < len(tube_arr) - 1) and (tube_arr[y + 1][x] != 9) and ((x, y + 1) not in marked):
        marked.append((x, y + 1))
        basin_size += 1 + get_basin_size(x, y + 1, height + 1)
    return basin_size


for y in range(len(tube_arr)):
    for x in range(len(tube_arr[y])):
        tube_val = tube_arr[y][x]
        tube_val_left = tube_arr[y][x - 1] if x > 0 else sys.maxsize
        tube_val_right = tube_arr[y][x + 1] if x < len(tube_arr[y]) - 1 else sys.maxsize
        tube_val_up = tube_arr[y - 1][x] if y > 0 else sys.maxsize
        tube_val_bottom = tube_arr[y + 1][x] if y < len(tube_arr) - 1 else sys.maxsize

        if ((tube_val < tube_val_left) & (tube_val < tube_val_right) &
                (tube_val < tube_val_up) & (tube_val < tube_val_bottom)):
            low_points.append((x, y))
            risk_level += tube_val + 1

print(f' low_points ---- {len(low_points)}')
for x, y in low_points:
    if ((x, y) not in marked) and (tube_arr[y][x] != 9):
        marked.append((x, y))
        basin_size = 1 + get_basin_size(x, y, tube_arr[y][x])
        basins.append(basin_size)

print(risk_level)
basins = sorted(basins, reverse=True)
print(f'magic numer: {basins[0] * basins[1] * basins[2]}')

# {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
# opens: { ( [ ( < [ }

# [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
# [ [ < [
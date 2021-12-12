import sys

with open("input.txt", "r") as f:
    octo_arr = [[int(x) for x in [y for y in line.strip()]] for line in f]

total_flashes = []


def flash(row, col):
    total_flashes.append(1)
    flashed.append((row, col))
    for n_row, n_col in [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
                         [row, col - 1], [row, col + 1],
                         [row + 1, col - 1], [row + 1, col], [row + 1, col + 1]]:
        if ((n_row >= 0) and (n_row < len(octo_arr))) and ((n_col >= 0) and (n_col < len(octo_arr[0]))):
            octo_arr[n_row][n_col] += 1
            if (octo_arr[n_row][n_col]) > 9 and ((n_row, n_col) not in flashed):
                flash(n_row, n_col)


for i in range(sys.maxsize):
    octo_arr = [[x + 1 for x in row] for row in octo_arr]
    flashed = []
    for row in range(len(octo_arr)):
        for col in range(len(octo_arr[0])):
            if ((octo_arr[row][col]) > 9) and ((row, col) not in flashed):
                flash(row, col)
    for f_row, f_col in flashed:
        octo_arr[f_row][f_col] = 0
    if all([all([1 if x == 0 else 0 for x in row]) for row in octo_arr]):
        print(f'simultaneous flash after step {i + 1}')
        break

#print(len(total_flashes))
points = []
instructions = []
with open("input.txt", "r") as f:
    for line in f:
        if 'fold' in line:
            instruction = line.strip().split()
            instructions.append(instruction[2].split('='))
        elif line.strip() != '':
            x, y = line.strip().split(',')
            points.append((int(x), int(y)))

for instruction in instructions:
    mode = 'horizontal' if instruction[0] == 'x' else 'vertical'
    fold_value = int(instruction[1])
    if mode == 'vertical':
        points = list(set([(x, (y - ((y - fold_value) * 2))) if y > fold_value else (x, y) for x, y in points]))
    elif mode == 'horizontal':
        points = list(set([((x - ((x - fold_value) * 2)), y) if x > fold_value else (x, y) for x, y in points]))

max_x = max([x for x, y in points]) + 1
max_y = max([y for x, y in points]) + 1

visual = [['.' for i in range(max_x)] for j in range(max_y)]
for x, y in points:
    visual[y][x] = '#'
for row in visual:
    print(row)

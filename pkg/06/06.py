def parse_input():
    fishes = {}
    with open("input.txt", "r") as f:
        for fish in [int(x) for x in f.readline().strip().split(',')]:
            fishes[fish] = fishes.get(fish, 0) + 1
    return fishes


fishes = parse_input()
for i in range(256):
    new_fishes = fishes.get(0, 0)
    new_fish_map = {}
    for key in fishes:
        if key != 0:
            new_fish_map[key - 1] = fishes[key]
    new_fish_map[6] = fishes.get(0, 0) + new_fish_map.get(6, 0)
    new_fish_map[8] = new_fishes
    fishes = new_fish_map
print(sum(fishes.values()))

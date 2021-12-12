def get_segments():
    with open("input.txt", "r") as f:
        return [[x.split() for x in line.strip().split(' | ')] for line in f]


segments = get_segments()
part_a = 0
part_b = 0
for segment in segments:
    # Part 1
    seg_1s = [len(output) == 2 for output in segment[1]]
    seg_4s = [len(output) == 4 for output in segment[1]]
    seg_7s = [len(output) == 3 for output in segment[1]]
    seg_8s = [len(output) == 7 for output in segment[1]]
    part_a += sum([sum(seg_1s), sum(seg_4s), sum(seg_7s), sum(seg_8s)])

    # Part 2
    # Start with knowns
    code_1 = ''.join(sorted([x for x in segment[0] if len(x) == 2][0]))
    code_4 = ''.join(sorted([x for x in segment[0] if len(x) == 4][0]))
    code_7 = ''.join(sorted([x for x in segment[0] if len(x) == 3][0]))
    code_8 = ''.join(sorted([x for x in segment[0] if len(x) == 7][0]))
    decode = {code_1: '1', code_4: '4', code_7: '7', code_8: '8'}

    # Determine len sixes
    len_sixes = [x for x in segment[0] if len(x) == 6]
    seg_6 = [x for x in len_sixes if len(set(x).intersection(code_1)) == 1][0]
    seg_9 = [x for x in len_sixes if len(set(x).intersection(code_4)) == 4][0]
    seg_0 = [x for x in len_sixes if (x != seg_6) & (x != seg_9)][0]
    decode[''.join(sorted(seg_6))] = '6'
    decode[''.join(sorted(seg_9))] = '9'
    decode[''.join(sorted(seg_0))] = '0'

    # Determine len fives
    len_fives = [x for x in segment[0] if len(x) == 5]
    seg_3 = [x for x in len_fives if len(set(x).intersection(code_1)) == 2][0]
    seg_2 = [x for x in len_fives if len(set(x).intersection(code_4)) == 2][0]
    seg_5 = [x for x in len_fives if (x != seg_2) & (x != seg_3)][0]
    decode[''.join(sorted(seg_2))] = '2'
    decode[''.join(sorted(seg_3))] = '3'
    decode[''.join(sorted(seg_5))] = '5'

    decoded_output = int(''.join([decode.get(''.join(sorted(output)), output) for output in segment[1]]))
    part_b += decoded_output

print(f'Part A is {part_a}')
print(f'Part B is {part_b}')

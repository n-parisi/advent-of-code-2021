def get_input():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f]


def part_1():
    report = get_input()
    byte_count = len(report[0])
    epsilon = [0] * byte_count
    for line in report:
        line_bytes = [int(i) for i in line]
        epsilon = [epsilon[i] + line_bytes[i] for i in range(byte_count)]
    epsilon = ['1' if epsilon[i] > len(report) / 2 else '0' for i in range(byte_count)]
    gamma = ['1' if x == '0' else '0' for x in epsilon]
    return int('0b' + ''.join(epsilon), 2) * int('0b' + ''.join(gamma), 2)


def part_2():
    ox_gen_report = c02_scrubber_report = get_input()
    byte_count = len(ox_gen_report[0])
    # find ox_gen
    for i in range(byte_count):
        count = sum([int(x[i]) for x in ox_gen_report])
        most_common = '1' if count >= len(ox_gen_report) / 2 else '0'
        # remove all without most common
        ox_gen_report = [x for x in ox_gen_report if x[i] == most_common]
        if len(ox_gen_report) == 1:
            ox_gen = ox_gen_report[0]
            break
    # find c02_scrubber
    for i in range(byte_count):
        count = sum([int(x[i]) for x in c02_scrubber_report])
        least_common = '0' if count >= len(c02_scrubber_report) / 2 else '1'
        # remove all without least common
        c02_scrubber_report = [x for x in c02_scrubber_report if x[i] == least_common]
        if len(c02_scrubber_report) == 1:
            c02_scrubber = c02_scrubber_report[0]
            break
    return int('0b' + ox_gen, 2) * int('0b' + c02_scrubber, 2)


print(part_1())
print(part_2())


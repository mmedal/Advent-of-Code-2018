import functools


def read_input(fname):
    with open(fname) as f:
        return f.readlines()


def part1():
    input_frequencies = read_input('input.txt')
    result = functools.reduce(lambda x, y: int(x) + int(y), input_frequencies)
    print(result)


def part2():
    input_frequencies = read_input('input.txt')

    seen_frequencies = [0]

    def traverse_frequencies(x, y):
        frequency = int(x) + int(y)
        if frequency in seen_frequencies:
            print(frequency)
            exit(0)
        else:
            seen_frequencies.append(frequency)
        return frequency

    current_frequency = 0
    while True:
        frequencies = [current_frequency] + input_frequencies
        current_frequency = functools.reduce(traverse_frequencies, frequencies)

input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    return [[int(c) for c in x.strip().split()] for x in input_data]


def is_safe(level):
    for i in range(-1, len(level)):
        if i == -1:
            current = level
        else:
            current = level[:i] + level[i+1:]
        diffs = [current[i] - current[i + 1] for i in range(len(current) - 1)]
        if all([1 <= d <= 3 for d in diffs]) or all([-1 >= d >= -3 for d in diffs]):
            return True
    return False


def main():
    levels = parse_input(get_input_data())
    for level in levels:
        print(level, is_safe(level))

    result = sum([is_safe(l) for l in levels])

    print('Final result:', result)


if __name__ == "__main__":
    main()

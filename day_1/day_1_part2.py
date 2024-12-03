input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    left = []
    right = []
    for line in input_data:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    return left, right


def main():
    left, right = parse_input(get_input_data())

    sorted_left = sorted(left)
    sorted_right = sorted(right)
    # print(sorted_left)
    # print(sorted_right)

    hash_map = {}

    result = []
    for l in left:
        if l not in hash_map:
            hash_map[l] = right.count(l)
        result.append(l * hash_map[l])

    print('Final result:', sum(result))


if __name__ == "__main__":
    main()
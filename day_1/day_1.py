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

    output = (abs(l - r) for l, r in zip(sorted_left, sorted_right))

    print('Final result:', sum(output))


if __name__ == "__main__":
    main()
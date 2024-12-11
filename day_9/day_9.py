from itertools import combinations

input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.read()
    return input_data


def parse_input(input_data):
    return [int(x) for x in input_data.strip()]


def visualise_grid(grid):
    print("".join([str(x) for x in grid]))


def create_file_system(inputs):
    file_system = []
    for i in range(len(inputs)):
        number = inputs[i]
        if i % 2 == 0:
            file_index = i // 2
            file_system += [file_index] * number
        else:
            file_system += ["."] * number
    return file_system


def frag_file_system(file_system):
    print("Fragging...")
    file_idx = 0
    while True:
        file_idx -= 1
        space_idx = file_system.index(".")
        if file_system[:file_idx].count(".") == 0:
            break
        file_system[space_idx] = file_system[file_idx]
        file_system[file_idx] = "."
        # visualise_grid(file_system)
    return file_system


def calculate_system_size(file_system):
    total = 0
    for i in range(len(file_system)):
        number = file_system[i]
        if number == ".":
            continue
        total += number * i
    return total


def main():
    data = parse_input(get_input_data())

    print(data)
    file_system = create_file_system(data)
    visualise_grid(file_system)
    fragged = frag_file_system(file_system)

    print("Total Size:", calculate_system_size(fragged))


if __name__ == "__main__":
    main()

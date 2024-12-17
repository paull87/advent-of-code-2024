from functools import cache

input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.read()
    return input_data


def parse_input(input_data):
    return [x for x in input_data.strip().split()]


def visualise_grid(grid):
    print(" ".join([str(x) for x in grid]))


@cache
def apply_rule(stone):
    if len(stone) % 2 == 0:
        split = int(len(stone) / 2)
        return [str(int(stone[:split])), str(int(stone[split:]))]
    elif stone == "0":
        return ["1"]
    else:
        return [str(int(stone) * 2024)]


@cache
def calculate_num_stones(stone, blinks):
    # print(blinks)
    if blinks == 0:
        return 1
    transformed_stones = apply_rule(stone)
    # print(transformed_stones, blinks)
    return sum(calculate_num_stones(num, blinks - 1) for num in transformed_stones)


def main():
    stones = parse_input(get_input_data())
    # print(stones)
    visualise_grid(stones)
    total = 0
    for stone in stones:
        total += calculate_num_stones(stone, 75)
    print("Total Stones:", total)


if __name__ == "__main__":
    main()

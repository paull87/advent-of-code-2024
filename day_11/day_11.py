from itertools import combinations

input_file = 'test_input_2.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.read()
    return input_data


def parse_input(input_data):
    return [x for x in input_data.strip().split()]


def visualise_grid(grid):
    print(" ".join([str(x) for x in grid]))


def blink(stones):
    # print(stones.count("0"))
    new_stone_order = []
    for stone in stones:
        if len(stone) % 2 == 0:
            split = int(len(stone) / 2)
            new_stone_order += [str(int(stone[:split])), str(int(stone[split:]))]
        elif stone == "0":
            new_stone_order.append("1")
        else:
            new_stone_order.append(str(int(stone) * 2024))
    return new_stone_order


def main():
    stones = parse_input(get_input_data())
    print(stones)
    visualise_grid(stones)
    for _ in range(25):
        stones = blink(stones)
        print(_, len(stones))
        visualise_grid(stones)
    print("Total Stones:", len(stones))


if __name__ == "__main__":
    main()

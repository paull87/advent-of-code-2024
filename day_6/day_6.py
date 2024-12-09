input_file = 'input.txt'

directions = {
    "^": (-1, 0),
    "V": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

direction_order = ["^", ">", "V", "<"]


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    return [[c.strip() for c in x.strip()] for x in input_data]


def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in ("^", "<", ">", "V"):
                return y, x, grid[y][x]


def change_direction(current_direction):
    dir_idx = direction_order.index(current_direction)
    dir_idx += 1
    dir_idx = dir_idx % 4
    return direction_order[dir_idx]


def direction_coords(direction):
    return directions[direction]


def visualise_grid(grid):
    for g in grid:
        print("".join(g))


def main():
    grid = parse_input(get_input_data())

    start_y, start_x, direction = find_start(grid)
    dir_y, dir_x = direction_coords(direction)

    spots = set()
    while True:
        # print(direction, start_y, start_x)
        next_y = start_y + dir_y
        next_x = start_x + dir_x
        if not 0 <= next_y < len(grid) or not 0 <= next_x < len(grid[next_y]):
            break

        if grid[next_y][next_x] != "#":
            start_y, start_x = next_y, next_x
            spots.add((start_y, start_x))
        else:
            direction = change_direction(direction)
            dir_y, dir_x = direction_coords(direction)
        grid[start_y][start_x] = "X"
        # visualise_grid(grid)
        # print("------")

    print("Steps:", len(spots))


if __name__ == "__main__":
    main()


input_file = 'test_input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    return [[int(c.strip()) for c in r.strip()] for r in input_data]


def visualise_grid(grid):
    for g in grid:
        print("".join([str(x) for x in g]))


def find_starting_moves(grid):
    valid_starts = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "0":
                valid_starts[(y, x)] = 0
    return valid_starts


def find_routes(grid):
    starts = find_starting_moves(grid)
    for start in starts:
        print(start)


def valid_routes(grid, start_moves, y, x):
    cur_num = grid[y][x]
    if cur_num == "9":
        start_moves[(y, x)] += 1

def main():
    grid = parse_input(get_input_data())
    routes = find_routes(grid)
    visualise_grid(grid)
    find_routes(grid)


if __name__ == "__main__":
    main()
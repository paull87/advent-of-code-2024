from copy import deepcopy

input_file = 'test_input2.txt'


move_map = {
    "<": (-1, 0),
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
}


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    grid = []
    moves = ""
    for line in input_data:
        if line.startswith("#"):
            grid.append([x.strip() for x in line.strip()])
        elif line.strip() == "":
            continue
        else:
            moves = moves + line.strip()

    return grid, moves


def visualise_grid(grid):
    for g in grid:
        print("".join([str(x) for x in g]))


def find_robot_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                return x, y


def move_robot(grid, rob_pos, move_pos):


def main():
    grid, moves = parse_input(get_input_data())
    visualise_grid(grid)
    print(moves)
    x, y = find_robot_start(grid)
    print(x, y)
    for move in moves:
        n_x, n_y = move_map[move]
        print(n_x, n_y)


if __name__ == '__main__':
    main()
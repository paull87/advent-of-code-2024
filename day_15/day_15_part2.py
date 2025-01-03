from copy import deepcopy

input_file = 'input.txt'


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


def explode_grid(grid):
    explode_map = {
        "#": ["#", "#"],
        "O": ["[", "]"],
        ".": [".", "."],
        "@": ["@", "."],
    }
    new_grid = []
    for r in grid:
        new_row = []
        for c in r:
            new_row += explode_map[c]
        new_grid.append(new_row)
    return new_grid


def visualise_grid(grid):
    for g in grid:
        print("".join([str(x) for x in g]))


def find_robot_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                return x, y


def move_robot(grid, current_pos, move):
    x, y = move_map[move]
    c_x, c_y = current_pos
    n_x = c_x + x
    n_y = c_y + y
    # out of bounds
    if not 0 <= n_y < len(grid):
        return current_pos
    if not 0 <= n_x < len(grid[n_y]):
        return current_pos
    if grid[n_y][n_x] == "#":
        return current_pos
    if grid[n_y][n_x] == ".":
        grid[c_y][c_x] = "."
        grid[n_y][n_x] = "@"
        return n_x, n_y
    if move == '>':
        in_front = grid[n_y][c_x:]
        if "." not in in_front:
            return current_pos
        spaces = in_front.index(".")
        if in_front.index("#") < spaces:
            return current_pos
        # print(in_front, spaces)
        for m in reversed(range(1, spaces+1)):
            # print(grid[n_y][c_x+m], grid[n_y][c_x + m - 1])
            grid[n_y][c_x+m] = grid[n_y][c_x+m-1]

        grid[c_y][c_x] = "."
    if move == '<':
        in_front = list(reversed(grid[n_y][:c_x+1]))
        if "." not in in_front:
            return current_pos
        spaces = in_front.index(".")
        if in_front.index("#") < spaces:
            return current_pos
        for m in reversed(range(0, spaces+1)):
            # print(grid[n_y][c_x-m], grid[n_y][c_x-m+1])
            grid[n_y][c_x-m] = grid[n_y][c_x-m+1]

        grid[c_y][c_x] = "."
    if move == '^':
        in_front = list(reversed([i[n_x] for i in grid[:c_y+1]]))
        if "." not in in_front:
            return current_pos
        spaces = in_front.index(".")
        if in_front.index("#") < spaces:
            return current_pos
        # print(in_front, spaces)

        # if current_pos == (5, 6):
        #     import pdb; pdb.set_trace()
        for m in reversed(range(0, spaces)):
            # print(grid[n_y-m][c_x], grid[n_y - m + 1][c_x])
            grid[n_y - m][c_x] = grid[n_y - m + 1][c_x]

        grid[c_y][c_x] = "."
    if move == 'v':
        in_front = list([i[n_x] for i in grid[c_y:]])
        if "." not in in_front:
            return current_pos
        spaces = in_front.index(".")
        if in_front.index("#") < spaces:
            return current_pos
        # import pdb; pdb.set_trace()
        for m in reversed(range(0, spaces)):
            grid[n_y+m][c_x] = grid[n_y+m-1][c_x]
        grid[c_y][c_x] = "."
    return n_x, n_y


def calculate_gps(grid):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                total += (100 * y) + x
    return total


def main():
    grid, moves = parse_input(get_input_data())
    visualise_grid(grid)
    grid = explode_grid(grid)
    visualise_grid(grid)
    # print(moves)
    # x, y = find_robot_start(grid)
    # for move in moves:
    #     print(x, y, move)
    #     x, y = move_robot(grid, (x, y), move)
    #     # visualise_grid(grid)
    # print("Total:", calculate_gps(grid))


if __name__ == '__main__':
    main()
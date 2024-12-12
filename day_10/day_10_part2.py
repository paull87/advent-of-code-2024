input_file = 'input.txt'


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
            if grid[y][x] == 0:
                valid_starts[(y, x)] = []
    return valid_starts


def find_routes(grid):
    starts = find_starting_moves(grid)
    for start in starts:
        print(start)
        path = []
        valid_routes(grid, starts, path, start[0], start[1])

    return starts


def valid_routes(grid, start_moves, path, y, x):
    # Out of bounds
    if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
        return False
    if not path:
        cur_num = -1
        next_num = grid[y][x]
    else:
        p_y, p_x = path[-1]
        cur_num = grid[p_y][p_x]
        next_num = grid[y][x]
    # Not incrementing
    if next_num - cur_num != 1:
        return False
    else:
        path.append((y, x))
        print(path)
        print([grid[x[0]][x[1]] for x in path])
    if next_num == 9:
        print("Valid")
        if not [x for x in start_moves[(path[0][0], path[0][1])] if x[-1] == (y, x)]:
            start_moves[(path[0][0], path[0][1])].append(path)
            print("New")
        return True
    # Left
    valid_routes(grid, start_moves, path.copy(), y-1, x)
    # Right
    valid_routes(grid, start_moves, path.copy(), y+1, x)
    # Up
    valid_routes(grid, start_moves, path.copy(), y, x-1)
    # Down
    valid_routes(grid, start_moves, path.copy(), y, x+1)


def main():
    grid = parse_input(get_input_data())
    routes = find_routes(grid)
    visualise_grid(grid)

    total = 0
    for s, v in routes.items():
        unique_endpoints = len(set([i[-1] for i in v]))
        endpoints = len(v)
        total += endpoints
        print(s, endpoints, unique_endpoints)
        # for r in v:
        #     print(r[-1])
        #     print([grid[x[0]][x[1]] for x in r])

    print("Total trailheads:", total)


if __name__ == "__main__":
    main()
from copy import deepcopy

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
    return None, None, None


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


def walk_grid(grid):
    direction_hash = {x: [] for x in directions}
    spots = set()
    is_loop = False
    start_y, start_x, direction = find_start(grid)
    if start_y is None:
        return spots, is_loop
    dir_y, dir_x = direction_coords(direction)

    while True:
        # print(direction, start_y, start_x)
        next_y = start_y + dir_y
        next_x = start_x + dir_x
        if not 0 <= next_y < len(grid) or not 0 <= next_x < len(grid[next_y]):
            break

        if grid[next_y][next_x] not in ("#", "O"):
            start_y, start_x = next_y, next_x
            spots.add((start_y, start_x))
        else:
            direction = change_direction(direction)
            dir_y, dir_x = direction_coords(direction)
        if (start_y, start_x) not in direction_hash[direction]:
            direction_hash[direction].append((start_y, start_x))
        else:
            is_loop = True
            break
        grid[start_y][start_x] = direction
        # visualise_grid(grid)
        # print("------")
    return spots, is_loop


def main():
    grid = parse_input(get_input_data())
    orig_grid = deepcopy(grid)
    orig_steps, _ = walk_grid(orig_grid)

    loops = []
    for ob_y, ob_x in orig_steps:
        # if ob_y == 65 and ob_x == 101:
        #     import pdb; pdb.set_trace()

        new_grid = deepcopy(grid)
        new_grid[ob_y][ob_x] = "O"
        _, is_loop = walk_grid(new_grid)
        if is_loop:
            loops.append((ob_y, ob_x))
            print(ob_y, ob_x)
            # visualise_grid(new_grid)

    print("Loops:", len(loops))


if __name__ == "__main__":
    main()


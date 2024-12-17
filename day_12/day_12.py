input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    return [[c.strip() for c in r.strip()] for r in input_data]


def visualise_grid(grid):
    for g in grid:
        print("".join(g))


def search_area(grid, area_plots, char, y, x):
    # Out of bounds
    if not 0 <= y < len(grid) or not 0 <= x < len(grid[y]):
        return False
    new_char = grid[y][x]
    if char != new_char:
        return False
    if (y, x) in area_plots:
        return False
    else:
        area_plots.append((y, x))
    # Left
    search_area(grid, area_plots, char, y-1, x)
    # Right
    search_area(grid, area_plots, char, y+1, x)
    # Up
    search_area(grid, area_plots, char, y, x-1)
    # Down
    search_area(grid, area_plots, char, y, x+1)


def find_areas(grid):
    areas = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y, x) in [a_c for a_r in areas for a_c in a_r]:
                continue
            area = []
            char = grid[y][x]
            search_area(grid, area, char, y, x)
            areas.append(area.copy())
    return areas


def calculate_fence_size(area):
    fences = 0
    for y, x in area:
        # top fences
        if (y - 1, x) not in area:
            fences += 1
        # bottom fences
        if (y + 1, x) not in area:
            fences += 1
        # left fences
        if (y, x - 1) not in area:
            fences += 1
        # right_fences
        if (y, x + 1) not in area:
            fences += 1
    return fences


def main():
    grid = parse_input(get_input_data())
    visualise_grid(grid)
    areas = find_areas(grid)
    total_cost = 0
    for a in areas:
        fences = calculate_fence_size(a)
        area = len(a)
        cost = area * fences
        print(area, fences, cost)

        total_cost += cost

    print("Total cost:", total_cost)


if __name__ == '__main__':
    main()
from itertools import accumulate
from functools import reduce


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
    sides = {k: set() for k in "LRTB"}
    edges = set()
    for y, x in area:
        # top fences
        if (y - 1, x) not in area:
            fences += 1
            # print(y, x, "Top side")
            sides["T"].add((y,x))
        # bottom fences
        if (y + 1, x) not in area:
            fences += 1
            # print(y, x, "Bottom side")
            sides["B"].add((y,x))
        # left fences
        if (y, x - 1) not in area:
            fences += 1
            # print(y, x, "Left side")
            sides["L"].add((y,x))
        # right_fences
        if (y, x + 1) not in area:
            fences += 1
            # print(y, x, "Right side")
            sides["R"].add((y,x))

    edges_count = 0
    for e in sorted(list(sides["L"]), key=lambda x: f"{x[1]}{x[0]}"):
        # print(e, edges_count)
        if (e[0]+1, e[1]) not in sides["L"]:
            edges_count += 1
    for e in sorted(list(sides["R"]), key=lambda x: f"{x[1]}{x[0]}"):
        # print(e, edges_count)
        if (e[0]+1, e[1]) not in sides["R"]:
            edges_count += 1
    for e in sorted(list(sides["T"]), key=lambda x: f"{x[0]}{x[1]}"):
        # print(e, edges_count)
        if (e[0], e[1]+1) not in sides["T"]:
            edges_count += 1
    for e in sorted(list(sides["B"]), key=lambda x: f"{x[0]}{x[1]}"):
        # print(e, edges_count)
        if (e[0], e[1]+1) not in sides["B"]:
            edges_count += 1
    return fences, edges_count


def main():
    grid = parse_input(get_input_data())
    visualise_grid(grid)
    areas = find_areas(grid)
    total_cost = 0
    for a in areas:
        # if (0, 6) not in a:
        #     continue
        fences, edges = calculate_fence_size(a)
        area = len(a)
        cost = area * edges
        print(area, fences, edges, cost)

        total_cost += cost

    print("Total cost:", total_cost)


if __name__ == '__main__':
    main()
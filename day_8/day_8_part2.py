from itertools import combinations

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


def find_antennas(grid):
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            antenna = grid[y][x]
            if antenna == ".":
                continue
            if antenna not in antennas:
                antennas[antenna] = []
            antennas[antenna].append((y, x))
    return antennas


def antenna_frequencies(antenna_locs, y_range, x_range):
    frequencies = []
    for left, right in combinations(antenna_locs, r=2):
        diff_y = left[0] - right[0]
        diff_x = left[1] - right[1]

        # left
        an_y = left[0]
        an_x = left[1]
        while True:
            if not 0 <= an_y < y_range or not 0 <= an_x < x_range:
                break
            frequencies.append((an_y, an_x))
            an_y += diff_y
            an_x += diff_x
        # right
        an_y = right[0]
        an_x = right[1]
        while True:
            if not 0 <= an_y < y_range or not 0 <= an_x < x_range:
                break
            frequencies.append((an_y, an_x))
            an_y -= diff_y
            an_x -= diff_x
    return frequencies


def main():
    grid = parse_input(get_input_data())

    visualise_grid(grid)

    antennas = find_antennas(grid)

    print(antennas)
    valid_freqs = set()
    for a, l in antennas.items():
        # print(a)
        # if a != "0":
        #     continue
        for f_y, f_x in antenna_frequencies(l, len(grid), len(grid[0])):
            print(f_y, f_x)
            # if not 0 <= f_y < len(grid):
            #     continue
            # if not 0 <= f_x < len(grid[f_y]):
            #     continue
            if grid[f_y][f_x] == ".":
                grid[f_y][f_x] = "#"
            valid_freqs.add((f_y, f_x))
    visualise_grid(grid)

    print("Antinode count:", len(valid_freqs))



if __name__ == "__main__":
    main()


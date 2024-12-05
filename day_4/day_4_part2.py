input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    return [[c.strip() for c in x.strip()] for x in input_data]


def check_word(word_locs, text_grid):
    check = "".join([text_grid[c_y][c_x] for c_y, c_x in word_locs])
    return check == WORD


def fimd_word_in_grid(text_grid):
    found = []
    start_letter = 'A'
    for y in range(1, len(text_grid) - 1):
        for x in range(1, len(text_grid[y]) - 1):
            start_point = text_grid[y][x]
            # print(start_point, y, x)
            if start_point == start_letter:
                points = [(y-1, x-1), (y-1, x+1), (y+1, x+1), (y+1, x-1)]
                letters = "".join(sorted([text_grid[c_y][c_x] for c_y, c_x in points]))
                if letters == "MMSS":
                    # if the diagonal opposites are not the same we are good
                    if text_grid[y-1][x-1] != text_grid[y+1][x+1]:
                        found.append([(y-1, x-1), (y-1, x+1), (y+1, x+1), (y-1, x-1)] + [(y, x)])
    return found


def main():
    text_grid = parse_input(get_input_data())

    found = fimd_word_in_grid(text_grid)

    for x in found:
        print(x)

    print(len(found))


if __name__ == "__main__":
    main()

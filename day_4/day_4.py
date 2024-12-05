input_file = 'input.txt'

WORD = "XMAS"


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
    start_letter = WORD[0]
    for y in range(len(text_grid)):
        for x in range(len(text_grid[y])):
            start_point = text_grid[y][x]
            # print(start_point, y, x)
            if start_point == start_letter:
                # N
                if y >= len(WORD) - 1:
                    check_locs = [(y-i, x) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
                # NW
                if y >= len(WORD) - 1 and x >= len(WORD) - 1:
                    check_locs = [(y-i, x-i) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
                # NE
                if y >= len(WORD) - 1 and len(text_grid[y]) - x >= len(WORD):
                    check_locs = [(y-i, x+i) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
                # E
                if len(text_grid[y]) - x >= len(WORD):
                    check_locs = [(y, x+i) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
                # SE
                if len(text_grid) - y >= len(WORD) and len(text_grid[y]) - x >= len(WORD):
                    check_locs = [(y+i, x+i) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
                # S
                if len(text_grid) - y >= len(WORD):
                    check_locs = [(y+i, x) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
                # SW
                if len(text_grid) - y >= len(WORD) and x >= len(WORD) - 1:
                    check_locs = [(y+i, x-i) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
                # W
                if x >= len(WORD) - 1:
                    check_locs = [(y, x-i) for i in range(len(WORD))]
                    if check_word(check_locs, text_grid):
                        found.append(check_locs)
    return found


def main():
    text_grid = parse_input(get_input_data())

    found = fimd_word_in_grid(text_grid)

    for x in found:
        print(x)

    print(len(found))


if __name__ == "__main__":
    main()

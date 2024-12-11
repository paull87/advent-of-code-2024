from itertools import zip_longest

input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.read()
    return input_data


def parse_input(input_data):
    files = []
    spaces = []
    for i in range(len(input_data.strip())):
        number = int(input_data[i])
        if i % 2 == 0:
            files.append(number)
        else:
            spaces.append(number)
    return files, spaces


def visualise_grid(grid):
    print("".join([str(x) for x in grid]))


def create_file_system(files, spaces, moves=None):
    moves = moves or {}
    file_system = []
    # extra_spaces = [0] * len(files)
    # print(extra_spaces)
    for i, pair in enumerate(zip(files, spaces)):
        f, s = pair
        # print(f, s)
        if i not in [m_f for m_s in moves.values() for m_f in m_s]:
            file_system += [i] * f
        for move_idx in moves.get(i, []):
            file_system += [move_idx] * files[move_idx]
            # extra_spaces[move_idx] += files[move_idx]
        s = s or 0
        file_system += ["."] * s
    # file_system += [i+1] * files[-1]
    return file_system


def organise_file_system(files, spaces):
    filled_space = {}
    spaces += [0]
    space_idx = 0
    for f_i in reversed(range(len(files))):
        print("Checking:", f_i, files[f_i])
        while True:
            # if f_i == 2:
            #     import pdb; pdb.set_trace()
            space = spaces[space_idx]
            file = files[f_i]
            # print("\t", space_idx, space)
            if file <= space:
                if space_idx not in filled_space:
                    filled_space[space_idx] = []
                filled_space[space_idx].append(f_i)
                spaces[space_idx] -= file
                spaces[f_i-1] += file
                print("\t Fits and moved to", space_idx)
                # print(filled_space)
                # print(spaces)
                # print(extra_spaces)
                break
            else:
                space_idx += 1
            if space_idx >= len(spaces) or space_idx >= f_i:
                print("\tDoes not move")
                break
        space_idx = 0
        # visualise_grid(create_file_system(files, spaces, moves=filled_space))
        # import pdb; pdb.set_trace()
        if space_idx > f_i:
            break

    # update space
    # for i in range(len(spaces)):
    #     spaces[i] += extra_spaces[i]
    # spaces += extra_spaces[-1:]
    return filled_space


def calculate_system_size(file_system):
    total = 0
    for i in range(len(file_system)):
        number = file_system[i]
        if number == ".":
            continue
        total += number * i
    return total


def main():
    files, spaces = parse_input(get_input_data())

    print(files)
    print(spaces)
    file_system = create_file_system(files, spaces)
    visualise_grid(file_system)
    potential_file_moves = organise_file_system(files, spaces)
    print(files)
    print(spaces)
    print(potential_file_moves)
    new_file_system = create_file_system(files, spaces, moves=potential_file_moves)

    visualise_grid(new_file_system)
    print("Total Size:", calculate_system_size(new_file_system))

# 00992111777.44.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..

if __name__ == "__main__":
    main()


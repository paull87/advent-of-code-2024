from itertools import product, zip_longest

input_file = 'input.txt'

SYMBOLS = ["+", "*", "||"]


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    outputs = []
    for line in input_data:
        result, nums = line.strip().split(":")
        outputs.append((int(result.strip()), [x.strip() for x in nums.split()]))

    return outputs


def calculate_options(expected, numbers):
    for symbol in SYMBOLS:
        if symbol == "||":
            if expected == int("".join(numbers)):
                return True
        elif expected == eval(symbol.join(numbers)):
            return True
    for combo in product(SYMBOLS, repeat=len(numbers) - 1):
        # Skip all the same as we've covered that
        if any([all([x == s for x in combo]) for s in SYMBOLS]):
            continue
        actual = numbers[0]
        for n, s in zip(numbers[1:], combo):
            if s == "||":
                actual = int(f"{actual}{n}")
            else:
                actual = eval(f"{actual}{s}{n}")
            if actual > expected:
                break
        if expected == actual:
            # calc_string = "".join([i for pair in zip_longest(numbers, combo, fillvalue="") for i in pair])
            # print(calc_string, eval(calc_string), expected)
            return True
    return False


def main():
    checks = parse_input(get_input_data())

    final_result = 0
    for result, nums in checks:
        if calculate_options(result, nums):
            print(result, nums)
            final_result += result

    print("Final Result:", final_result)


if __name__ == "__main__":
    main()


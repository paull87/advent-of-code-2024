input_file = 'input.txt'


def get_input_data():
    with open(input_file) as file:
        input_data = file.readlines()
    return input_data


def parse_input(input_data):
    outputs = []
    current = {}
    for line in input_data:
        if line.startswith("Button"):
            button, coords = line.split(":")
            button = button.strip().split()[-1]
            x, y = (int(x.split("+")[-1]) for x in coords.strip().split(","))
            current[button] = {"X": x, "Y": y}
        if line.startswith("Prize"):
            coords = line.split(":")[-1]
            x, y = (int(x.split("=")[-1]) for x in coords.strip().split(","))
            current["Prize"] = {"X": x, "Y": y}
        if line.strip() == "":
            outputs.append(current)
            current = {}
    if current:
        outputs.append(current)

    return outputs


def calculate_presses(inputs):
    x_expected = inputs["Prize"]["X"]
    y_expected = inputs["Prize"]["Y"]
    x_a = inputs["A"]["X"]
    x_b = inputs["B"]["X"]
    y_a = inputs["A"]["Y"]
    y_b = inputs["B"]["Y"]
    button_diff = x_a * y_b - y_a * x_b
    a_actual = abs(int((x_expected * y_b - y_expected * x_b) / button_diff))
    b_actual = abs(int((x_expected * y_a - y_expected * x_a) / button_diff))
    if x_a * a_actual + x_b * b_actual == x_expected and y_a * a_actual + y_b * b_actual == y_expected:
        return a_actual, b_actual
    else:
        return None, None


def calculate_press_cost(a, b):
    return a * 3 + b


def main():
    outputs = parse_input(get_input_data())
    total_cost = 0
    for o in outputs:
        print(o)
        a_press, b_press = calculate_presses(o)
        if a_press:
            cost = calculate_press_cost(a_press, b_press)
            total_cost += calculate_press_cost(a_press, b_press)
        else:
            cost = 0

    print("Total Cost:", total_cost)


if __name__ == '__main__':
    main()
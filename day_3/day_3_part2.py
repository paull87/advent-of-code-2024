import re


input_file = 'input.txt'


reg = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")


def get_input_data():
    with open(input_file) as file:
        input_data = file.read()
    return input_data


def find_matches(text):
    return reg.findall(text)


def parse_matches(matches):
    output = []
    for m in matches:
        if m.startswith("mul"):
            l, r = re.findall(r"\d+", m)
            output.append((int(l), int(r)))
        else:
            output.append(m)
    return output


def main():
    text = get_input_data()
    # print(text)
    text = text
    matches = find_matches(text)
    # print(matches)
    parsed = parse_matches(matches)
    # print(parsed)
    do = True
    result = 0
    for i in parsed:
        if i == "do()":
            do = True
        elif i == "don't()":
            do = False
        else:
            result += i[0] * i[1] if do else 0

    print(result)


if __name__ == "__main__":
    main()

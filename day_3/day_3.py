import re


input_file = 'input.txt'


reg = re.compile(r"mul\(\d+,\d+\)")


def get_input_data():
    with open(input_file) as file:
        input_data = file.read()
    return input_data


def find_matches(text):
    return reg.findall(text)


def parse_matches(matches):
    output = []
    for m in matches:
        l, r = re.findall(r"\d+", m)
        output.append((int(l), int(r)))
    return output


def main():
    text = get_input_data()
    # print(text)
    matches = find_matches(text)
    # print(matches)
    parsed = parse_matches(matches)
    # print(parsed)
    result = sum((l * r for l, r in parsed))

    print(result)


if __name__ == "__main__":
    main()

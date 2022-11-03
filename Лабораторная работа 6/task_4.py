import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', newline='\n') -> list[dict]:
    with open(filename) as f:
        csv_data = f.read()
    lines = csv_data.split(newline)
    headings = lines[0].split(delimiter)
    number_of_lines = len(lines) - 1
    number_of_headings = len(headings)
    data = [0] * number_of_lines
    for line_number in range(number_of_lines):
        data[line_number] = {headings[i]: lines[line_number + 1].split(delimiter)[i] for i in range(number_of_headings)}
    return data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

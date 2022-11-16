import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', newline='\n') -> list[dict]:
    with open(filename) as f:
        data = []
        is_heading = True
        for line in f:
            lines = line.rstrip().split(newline)
            for current_line in lines:
                if is_heading:
                    headings = current_line.split(delimiter)
                    is_heading = False
                    continue
                data.append(dict(zip(headings, current_line.split(delimiter))))
    return data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

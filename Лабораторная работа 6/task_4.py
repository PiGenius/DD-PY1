import json

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"


def csv_to_list_dict(filename, delimiter=',', newline='\n') -> list[dict]:
    with open(filename) as f:
        is_heading = True
        for line in f:
            lines = line.rstrip().split(newline)
            for current_line in lines:
                if is_heading:
                    headings = current_line.split(delimiter)
                    is_heading = False
                    continue
                yield dict(zip(headings, current_line.split(delimiter)))


with open(OUTPUT_FILE, 'w') as dst:
    for record in csv_to_list_dict(INPUT_FILE):
        json.dump(record, dst, indent=4)

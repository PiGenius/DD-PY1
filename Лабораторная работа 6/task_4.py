INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"


def csv_to_list_dict(filename, delimiter, newline) -> list[dict]:
    with open(filename) as f:
        is_heading = True
        for line in f:
            lines = line.rstrip('\n').split(newline)
            for current_line in lines:
                if is_heading:
                    headings = current_line.split(delimiter)
                    is_heading = False
                    continue
                yield dict(zip(headings, current_line.split(delimiter)))


def csv_to_json(input_file, output_file, delimiter=',', newline='\n', indent_=0):
    indent = '' + ' ' * indent_

    with open(output_file, 'w') as dst:
        dst.write("[\n")
        is_first_item_in_file = True

        for record in csv_to_list_dict(input_file, delimiter, newline):
            is_first_item_in_dict = True
            if not is_first_item_in_file:
                dst.write(',\n')
            dst.write(indent + "{\n")
            for key, value in record.items():
                if not is_first_item_in_dict:
                    dst.write(',\n')
                dst.write(f'{indent}{indent}"{key}": {value}')
                is_first_item_in_dict = False
            dst.write('\n' + indent + "}")
            is_first_item_in_file = False
        dst.write("\n]")


csv_to_json(INPUT_FILE, OUTPUT_FILE)

import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str,
                     delimiter: str = ',',
                     new_line: str = '\n') -> list[dict]:
    with open(filename, 'r') as input:
        str_data = input.read()  # not readline to support non-'\n' line delimiter
    lines = str_data.split(new_line)
    headers = lines[0].split(delimiter)
    res = []
    for l in filter(None, lines[1:]): #filter to remove empty "lines"
        values = l.split(delimiter)
        row = {headers[i]: v for i, v in enumerate(values)}
        res.append(row)
    return res


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

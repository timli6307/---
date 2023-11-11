###########第三題的函式

import json

def read_json(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def print_json(data: dict) -> None:
    print(json.dumps(data, indent=4, ensure_ascii=False))

def process_data(data: dict, discount: float) -> None:
    for category in data['categories']:
        for item in category['items']:
            item['price'] = round(item['price'] * discount)

def write_json(data: dict, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

########第二題的函式

def triangle_zhonxin(a, b, c):
    x = (a[0] + b[0] + c[0]) / 3
    y = (a[1] + b[1] + c[1]) / 3

    x = round(x)
    y = round(y)

    return x, y


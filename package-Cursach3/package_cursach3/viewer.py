import json
from datetime import datetime

def load_data(file):
    list_operation = []
    try:
        with open(file, "r", encoding="utf-8") as f:
            row_json = f.read()

    except FileNotFoundError:
        return list_operation

    list_operation = json.loads(row_json)
    while {} in list_operation:
        list_operation.remove({})

    list_operation.sort(key=lambda k: k["date"], reverse = True)

    return list_operation

def mask_kard(destination):
    str_kard = ""
    if  destination.find("Счет") != -1:
        str_kard = "Счет **" + destination[-4:]

    else:
        str_kard += f"{destination[0:-16]}"
        temp_str = destination[-16:]
        for a in range(5):
            if a == 1:
                str_kard += f"{temp_str[:4]} "
            elif a ==2:
                str_kard += f"{temp_str[4:6]}** "
            elif a == 3:
                str_kard += "**** "
            elif a == 4:
                str_kard += f"{temp_str[-4:]} "
    return str_kard


def operation_sting(i):
    string = ""
    if "from" in i.keys():
        string += f'{mask_kard(i["from"])}'

    string += f'-> {mask_kard(i["to"])}'
    return string










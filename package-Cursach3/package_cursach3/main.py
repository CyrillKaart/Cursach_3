import json
from datetime import datetime
from Functions import *

list_operation = load_data("operations.json")
count = 0

for i in list_operation:

    if count == 5:
        break

    elif i["state"] == "EXECUTED":
        information = ""
        count += 1

        date = datetime.strptime(i.get("date"), "%Y-%m-%dT%H:%M:%S.%f")
        information += f"{date.strftime('%d.%m.%Y')} {i['description']}\n"

        information += f'{operation_sting(i)}\n'

        information += f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n'

        print(information)
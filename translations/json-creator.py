import csv
import json

messages = dict()
languages = []

with open("messages-vue-helloworld.csv") as csvfile:
    reader = csv.reader(csvfile)
    first = True
    for row in reader:
        if first:
            for col in row:
                languages.append(col)
                messages[col] = dict()

            first = False

        else:
            str_key = row[0]
            for col in range(len(languages)):
                messages[languages[col]][str_key] = row[col]

for key in messages.keys():
    with open(f'{key}.json', 'w', encoding="utf8") as jsonfile:
        json.dump(messages[key], jsonfile, ensure_ascii=False, indent=4)

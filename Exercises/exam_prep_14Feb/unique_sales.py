import csv
file_path = input()

item_by_towns = {}
towns_by_items = {}
COLUMN_ITEM_ID = 0
COLUMN_TOWN = 2
COUNT_COLUMNS = 5

try:
    count_lines = 0
    with open(file_path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            count_lines += 1
            if len(line) == COUNT_COLUMNS:
                item_id = line[COLUMN_ITEM_ID].strip()
                town = line[COLUMN_TOWN].strip()

                if item_id and town:
                    if item_id not in item_by_towns:
                        item_by_towns[item_id] = set()
                    item_by_towns[item_id].add(town)
                else:
                    raise ValueError
            elif len(line) == 0:
                continue
            else:
                raise ValueError

    if count_lines == 0:
        raise ValueError("Empty file")

    item_in_one_town = list(filter(lambda item: len(item_by_towns[item]) == 1, item_by_towns))

    if not item_in_one_town:
        print("NO UNIQUE SALES")
    else:
        for item in item_in_one_town:
            current_town = list(item_by_towns[item])[0]
            if current_town not in towns_by_items:
                towns_by_items[current_town] = []
            towns_by_items[current_town].append(item)

        towns_sorted = sorted(towns_by_items.keys())
        for town in towns_sorted:
            items_list = towns_by_items[town]
            print("{},{}".format(town, ",".join(sorted(items_list))))

except Exception:
    print("INVALID INPUT")
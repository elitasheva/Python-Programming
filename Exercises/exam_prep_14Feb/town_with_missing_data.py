import csv
import iso8601
file_path = input()
towns = set()
data = dict()
try:
    count_lines = 0
    with open(file_path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if line:
                count_lines += 1
                date = iso8601.parse_date(line[0]).replace(minute=0, second=0, microsecond=0)
                town = line[1]
                temp = float(line[2])
                towns.add(town)
                if date not in data:
                    data[date] = []
                data[date].append(town)

    if count_lines == 0:
        raise ValueError("Empty file")

    dates_with_missing_towns = list(filter(lambda key: len(data[key]) < len(towns), data))
    if not dates_with_missing_towns:
        print("ALL DATA AVAILABLE")
    else:
        dates_with_missing_towns = sorted(dates_with_missing_towns)
        for current_date in dates_with_missing_towns:
            missing_towns = set(data[current_date]) ^ towns
            missing_towns = sorted(missing_towns)
            print("{},{}".format(current_date.strftime("%Y-%m-%d"), ",".join(missing_towns)))

except Exception:
    print("INVALID INPUT")
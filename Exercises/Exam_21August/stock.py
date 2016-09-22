import csv
import iso8601

try:
    path = input()
    percentage_str = input()
    prev_price = None
    percentage = float(percentage_str)
    if percentage <= 0:
        raise ValueError
    count_lines = 0
    result = list()
    with open(path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if len(line) != 2:
                raise ValueError

            count_lines += 1
            date_str = line[0]
            date = iso8601.parse_date(date_str)
            current_price = float(line[1])
            if current_price <= 0:
                raise ValueError

            if prev_price is None:
                prev_price = current_price
                continue
            else:
                difference = current_price - prev_price
                current_persentage = (difference / prev_price) * 100
                if current_persentage >= percentage:
                    result.append((date_str, current_persentage))

            prev_price = current_price

    if count_lines == 0:
        raise ValueError

    if not result:
        print("NO DRASTIC CHANGES; RECORDS COUNT: {}". format(count_lines))
    else:
        for date, per in result:
            print("{} {:.2f}".format(date, per))

except Exception:
    print("INVALID INPUT")
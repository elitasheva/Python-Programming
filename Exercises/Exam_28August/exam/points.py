import csv
import math

try:
    path = input()
    min_distance_str = input()

    min_distance = float(min_distance_str)
    if min_distance <= 0:
        raise ValueError

    count_lines = 0
    prev_x = None
    prev_y = None
    result = list()
    with open(path, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if len(line) != 3:
                raise ValueError

            count_lines += 1
            # TODO check id
            current_id = int(line[0])
            current_x = float(line[1])
            current_y = float(line[2])

            if prev_x is None and prev_y is None:
                prev_x = current_x
                prev_y = current_y
                continue

            distance = math.sqrt((prev_x - current_x) ** 2 + (prev_y - current_y) ** 2)

            if distance < min_distance:
                result.append(current_id)

            prev_x = current_x
            prev_y = current_y

    if count_lines == 0:
        raise ValueError

    if result:
        for current_id in result:
            print(current_id)
    else:
        print("NO CLOSE POINTS FOUND; RECORDS COUNT: {}".format(count_lines))



except Exception:
    print("INVALID INPUT")
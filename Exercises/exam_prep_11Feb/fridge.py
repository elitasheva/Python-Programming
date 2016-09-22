import csv
input_path = input()

with open(input_path, encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    prev_temp = None
    for line in reader:
        current_temp_str = line[-1]
        try:
            current_temp_num = float(current_temp_str)
            if prev_temp is None:
                prev_temp = current_temp_num

            if current_temp_num - prev_temp > 4:
                print(line[0])

            prev_temp = current_temp_num

        except ValueError:
            print("INVALID INPUT")

import csv
item_id = input()
path_sales = input()

min_price = None
town = None

with open(path_sales, encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        if line and item_id in line:
            current_price_str = line[-1]
            try:
                current_price_num = float(current_price_str)
                if min_price is None or current_price_num < min_price:
                    min_price = current_price_num
                    town = line[2]
            except ValueError:
                print("Невалидна цена!")
print(town)

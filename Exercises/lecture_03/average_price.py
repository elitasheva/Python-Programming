DEFAULT_COUNT_OF_COLUMNS = 7
sum_of_all_prices = 0
count_of_lines = 0
try:
    with open("./resources/catalog_full.csv") as file:
        for line in file:
            line_params = line.strip().split(",")
            if len(line_params) != DEFAULT_COUNT_OF_COLUMNS:
                raise ValueError
            else:
                price = float(line_params[len(line_params) - 1])
                sum_of_all_prices += price
                count_of_lines += 1
    average_price = sum_of_all_prices / count_of_lines
    print("{:.2f}".format(average_price))

except FileNotFoundError:
    print("Invalid file path.")
except ValueError:
    print("Invalid input data.")

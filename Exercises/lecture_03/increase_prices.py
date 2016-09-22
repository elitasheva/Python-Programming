DEFAULT_COUNT_OF_COLUMNS = 7
input_file_path = "./resources/catalog_full.csv"
output_file_path = "./resources/catalog_new_prices.csv"

new_prices_by_type = {
    'Woman': 1.75,
    'Unisex': 1.60,
    'Kid': 1.50,
    'Infant': 1.50,
    'Men': 1.25
}

try:
    with open(input_file_path) as input_file:
        with open(output_file_path, 'w') as output_file:
            for line in input_file:
                line_params = line.strip().split(",")
                if len(line_params) != DEFAULT_COUNT_OF_COLUMNS:
                    raise ValueError
                else:
                    price = float(line_params[len(line_params) - 1])
                    group_type = line_params[len(line_params) - 2]
                    new_price = price * new_prices_by_type[group_type]
                    line_params[len(line_params) - 1] = str("{:.2f}\n".format(new_price))
                    output_line = ",".join(line_params)
                    output_file.write(output_line)
except FileNotFoundError:
    print("Invalid file path.")
except ValueError:
    print("Invalid input data.")

DEFAULT_COUNT_OF_COLUMNS = 7
# in the dict: the key is the type of group;
# the value is a list with sum of the prices for this group at position 0
# and count of occupancies of the group at position 1
groups = dict()
try:
    with open("./resources/catalog_full.csv") as file:
        for line in file:
            line_params = line.strip().split(",")
            if len(line_params) != DEFAULT_COUNT_OF_COLUMNS:
                raise ValueError
            else:
                price = float(line_params[len(line_params) - 1])
                group_type = line_params[len(line_params) - 2]
                if group_type not in groups:
                    groups[group_type] = [price, 1]
                else:
                    groups[group_type][0] += price
                    groups[group_type][1] += 1

    for current_group in groups:
        average_price = groups[current_group][0] / groups[current_group][1]
        print("Group: {}: Average price: {:.2f}". format(current_group, average_price))

except FileNotFoundError:
    print("Invalid file path.")
except ValueError:
    print("Invalid input data.")

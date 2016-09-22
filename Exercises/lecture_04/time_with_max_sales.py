import iso8601

FILE_PATH = "./resources/sales.csv"

grouped_sales = {}

with open(FILE_PATH) as f_input:
    for index, currentLine in enumerate(f_input):
        data = currentLine.split(",")
        try:
            date_str = data[0]
            date_datetime = iso8601.parse_date(date_str)
            key = date_datetime.replace(minute=0, second=0, microsecond=0)
            price_str = data[1].strip()
            price_float = float(price_str)
            grouped_sales[key] = grouped_sales.get(key, 0) + price_float

        except ValueError:
            print("invalid input parameters at line: {}".format(index + 1))
        except iso8601.ParseError:
            print("invalid input parameters at line: {}".format(index + 1))

max_element = max(grouped_sales, key=grouped_sales.get)
print("Date: {}; Sales: {:.2f}".format(max_element.strftime('%Y-%m-%d at %H:%M o\'clock'), grouped_sales[max_element]))

import csv


def load_catalog(filename: str) -> dict:
    catalog_by_id = {}
    with open(filename, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            product_id = line[0]
            catalog_by_id[product_id] = line
    return catalog_by_id

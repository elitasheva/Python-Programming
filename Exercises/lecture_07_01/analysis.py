from lecture_07_01.load_data import load_catalog, load_sales
from lecture_07_01.analyzers import TotalsAnalyzer, AmountsByCategoryAnalyzer, AmountsByCityAnalyzer, AmountsByHourAnalyzer
CATALOG_FILE = "./resources/catalog.csv"
SALES_FILE = "./resources/sales-10K.csv"


def main():
    catalog = load_catalog(CATALOG_FILE)
    print("Analysis")
    print()

    analyzers = [
        TotalsAnalyzer(),
        AmountsByCategoryAnalyzer(catalog),
        AmountsByCityAnalyzer(catalog),
        AmountsByHourAnalyzer(catalog)
    ]

    load_sales_generator_object = load_sales(SALES_FILE)
    for sale in load_sales_generator_object:
        for a in analyzers:
            a.analyze_sale(sale)

    for a in analyzers:
        a.print_result()


if __name__ == '__main__':
    main()

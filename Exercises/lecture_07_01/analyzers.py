KEY_PRODUCT_ID = "product_id"
KEY_COUNTRY = "country"
KEY_TOWN = "town"
KEY_TIME = "time"
KEY_PRICE = "price"


class BaseAnalyzer:
    def analyze_sale(self, sale):
        pass

    def print_result(self):
        pass


class TotalsAnalyzer(BaseAnalyzer):
    def __init__(self):
        super().__init__()
        self.total_amount = 0
        self.total_count = 0
        self.min_timestamp = None
        self.max_timestamp = None

    def analyze_sale(self, sale):
        self.total_count += 1
        self.total_amount += sale[KEY_PRICE]

        ts = sale[KEY_TIME]
        if self.min_timestamp is None or ts < self.min_timestamp:
            self.min_timestamp = ts
        if self.max_timestamp is None or ts > self.max_timestamp:
            self.max_timestamp = ts

    def print_result(self):
        print("""Обобщение
---------
     Общ брой продажби: {total_count}
     Общо сума продажби: {total_amount:.2f} €
     Средна цена на продажба: {average_price:.2f} €
     Начало на период на данните: {min_ts}
     Край на период на данните: {max_ts}""".format(
            total_count=self.total_count,
            total_amount=self.total_amount,
            average_price=self.total_amount/ self.total_count if self.total_count else None,
            min_ts=self.min_timestamp,
            max_ts=self.max_timestamp,
        ))
        print()


class AmountsGroupedAnalyzer(BaseAnalyzer):
    group_by_title = ""

    def __init__(self, catalog):
        self.amounts_grouped = {}
        self.catalog = catalog

    def analyze_sale(self, sale):
        price = sale[KEY_PRICE]
        group_by_value = self.get_group_by_value(sale)
        if group_by_value not in self.amounts_grouped:
            self.amounts_grouped[group_by_value] = 0
        self.amounts_grouped[group_by_value] += price

    # define abstract method ???
    def get_group_by_value(self, sale):
        ...

    def print_result(self):
        amounts_grouped_sorted = list(self.amounts_grouped.items())
        amounts_grouped_sorted.sort(key=lambda kv: kv[1], reverse=True)

        print("""Сума на продажби по {} (top 5)
-----------------------------""".format(self.group_by_title))
        for category_name, total_amount in amounts_grouped_sorted[:5]:
            print("     {}: {:.2f} €".format(category_name, total_amount))
        print()


class AmountsByCategoryAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = "категории"

    def get_group_by_value(self, sale):
        item_id = sale[KEY_PRODUCT_ID]
        return self.catalog.get(item_id, None)


class AmountsByCityAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = "градове"

    def get_group_by_value(self, sale):
        return sale[KEY_TOWN]


class AmountsByHourAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = "часове"

    def get_group_by_value(self, sale):
        ts = sale[KEY_TIME]
        ts = ts.replace(minute=0, second=0, microsecond=0)
        return ts

from lecture_06.refactor_code.sales import KEY_PRICE, KEY_TIME
from functools import reduce


def print_summary(dict_sales: list):
    count_of_sales = len(dict_sales)
    total_sum = reduce((lambda x, y: x+y), list(map((lambda p: p[KEY_PRICE]), dict_sales)))
    min_time = min(list(map((lambda p: p[KEY_TIME]), dict_sales)))
    max_time = max(list(map((lambda p: p[KEY_TIME]), dict_sales)))

    print("""Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {avegage_price:.2f} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}""".format(
        total_count=count_of_sales,
        total_amount=total_sum,
        avegage_price=total_sum / count_of_sales if count_of_sales else None,
        min_ts=min_time,
        max_ts=max_time,
    ))
    print()


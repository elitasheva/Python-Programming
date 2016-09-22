from sales import KEY_PRICE, KEY_TIME


def print_summary(dict_sales: list):
    count_of_sales = len(dict_sales)
    total_sum = 0
    min_time = None
    max_time = None
    for item in dict_sales:
        total_sum += item[KEY_PRICE]
        time = item[KEY_TIME]

        if min_time is None or time < min_time:
            min_time = time

        if max_time is None or time > max_time:
             max_time = time

    print(""" Общ брой продажби: {total_count}
 Общо сума продажби: {total_amount:.2f} €
 Средна цена на продажба: {avegage_price} €
 Начало на период на данните: {min_ts}
 Край на период на данните: {max_ts}""".format(
        total_count=count_of_sales,
        total_amount=total_sum,
        avegage_price=total_sum / count_of_sales if count_of_sales else None,
        min_ts=min_time,
        max_ts=max_time,
    ))
    print()


import math


try:
    bicycle_price_str = input()
    saved_money_per_day_str = input()
    spended_money_per_ten_days_str = input()

    bicycle_price = float(bicycle_price_str.strip())
    saved_money_per_day = float(saved_money_per_day_str.strip())
    spended_money_per_ten_days = float(spended_money_per_ten_days_str.strip())

    if bicycle_price < 0 or saved_money_per_day <= 0 or spended_money_per_ten_days < 0:
        raise ValueError

    saved_money_for_ten_days = saved_money_per_day * 10
    balance_for_ten_days = saved_money_for_ten_days - spended_money_per_ten_days

    if balance_for_ten_days <= 0:
        print("NO BIKE FOR YOU")
    else:
        times_ten_days = math.trunc(bicycle_price / balance_for_ten_days)
        rest_to_save = bicycle_price - (balance_for_ten_days * times_ten_days)
        if rest_to_save == 0:
            days = balance_for_ten_days * times_ten_days
        else:
            days_needed = math.ceil(rest_to_save / saved_money_per_day)
            days = times_ten_days * 10 + days_needed

        print(days)

except Exception:
    print("INVALID INPUT")
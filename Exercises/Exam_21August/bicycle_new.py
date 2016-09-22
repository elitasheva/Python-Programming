try:
    bicycle_price_str = input()
    saved_money_per_day_str = input()
    spended_money_per_ten_days_str = input()

    bicycle_price = float(bicycle_price_str.strip())
    saved_money_per_day = float(saved_money_per_day_str.strip())
    spended_money_per_ten_days = float(spended_money_per_ten_days_str.strip())

    if bicycle_price < 0 or saved_money_per_day <= 0 or spended_money_per_ten_days < 0:
        raise ValueError

    if spended_money_per_ten_days == saved_money_per_day * 10:
        print("NO BIKE FOR YOU")
    else:

        total_sum = 0
        count_days = 0

        while total_sum < bicycle_price:
            count_days += 1
            total_sum += saved_money_per_day
            if count_days == 10 and total_sum < spended_money_per_ten_days:
                print("NO BIKE FOR YOU")
                break
            if count_days % 10 == 0:
                total_sum -= spended_money_per_ten_days
                if total_sum <= 0:
                    print("NO BIKE FOR YOU")
                    break

        print(count_days)

except Exception:
    print("INVALID INPUT")
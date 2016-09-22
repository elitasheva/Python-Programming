path_exchange = input()
path_amounts = input()
dict_exchange = {}

with open(path_exchange, encoding="utf-8") as f_exchange:
    for line in f_exchange:
        line = line.strip()
        if line:
            params_exchange = line.split()
            currency = params_exchange[0]
            exchange = None
            try:
                exchange = float(params_exchange[1])
            except ValueError:
                print("Невалиден курс!")

            dict_exchange[currency] = exchange

with open(path_amounts, encoding="utf-8") as f_amounts:
    for line in f_amounts:
        line = line.strip()
        if line:
            params_amounts = line.split()
            currency = params_amounts[1]
            amount = None
            try:
                amount = float(params_amounts[0])
            except ValueError:
                print("Невалидна сума!")

            exchange = dict_exchange.get(currency, None)
            if exchange:
                result = amount / exchange
                print("{:.2f}".format(result))
            else:
                print("Няма данни за подадената валута!")
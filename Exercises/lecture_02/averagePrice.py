prices = list()
while True:
    user_input = input("Enter a valid price (or 'stop'):")

    if user_input == "stop":
        break

    if user_input.isdigit:
        price_float = float(user_input)
        prices.append(price_float)
    else:
        continue

prices.sort()
min_element = prices[0]
while len(prices) > 0 and min_element == prices[0]:
    min_element = prices.pop(0)

# prices[:] = [pr for pr in prices if pr != min_element]
# prices = list(filter(min_element.__ne__, prices))

max_element = prices[len(prices)-1]
while len(prices) > 0 and max_element == prices[len(prices)-1]:
    max_element = prices.pop(len(prices)-1)

# prices[:] = [pr for pr in prices if pr != max_element]
# prices = list(filter(max_element.__ne__, prices))

if prices:
    sum_prices = 0
    for current_price in prices:
        sum_prices += current_price
    average_price = sum_prices / len(prices)
    print("Minimum price is: {:.2f}".format(min_element))
    print("Maximum price is: {:.2f}".format(max_element))
    print("Average price is: {:.2f}".format(average_price))
else:
    print("Not enough data")

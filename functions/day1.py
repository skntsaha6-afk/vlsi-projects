# Problem 1 — Average Price
# Write a function to compute the average of prices.
# Problem 2 — Maximum Price
# Write a function to return the highest price.
# Problem 3 — Percentage Change
# Problem 4 — Moving Average
# Important for trading strategies.
# Problem 5 — Count Price Increase Days
# Trading analysis problem.


# Problem 1 — Average Price

def avg_price(prices):
    if not prices:
        return 0
    return sum(prices)/len(prices)
print(avg_price([100, 102, 105, 110]))

#Problem 2 — Maximum Price
# #M1
def max_price_wo_max(prices):
    if not prices:
        return 0
    max_value = prices[0]
    for price in prices:
        if price >= max_value:
            max_value = price
    return max_value
print(max_price_wo_max([100, 102, 105, 110]))
#M2
def max_price_with_max(prices):
    if not prices:
        return 0
    return max(prices)
print(max_price_with_max([100, 102, 105, 110]))

#
#Problem 3 — Percentage Change
def percentage_change(old_price,new_price):
    if not old_price and new_price :
        return 0
    return  (new_price-old_price /old_price)*100 
    # need to check how to keep minus sign for decrease and plus sign for increase in price
print(percentage_change(110,100))

#Problem 4 — Moving Average
def calculate_moving_avg(prices, window):
    if not prices or not window:
        return 0
    sorted_prices = []
    for i in range(len(prices) - window+1):
        avg_price = sum(prices[i:i+window])/window
        sorted_prices.append(avg_price)
    return prices[i:i+window],sorted_prices

print(calculate_moving_avg([100,101,102,103,104],3))

#Problem 5 — Count Price Increase Days
# how many days price increase from previous days
def find_price_increase(prices):
    if not prices:
        return 0
    count = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            count += 1
    return f'No of days price got increase : {count}'

print(find_price_increase([100,102,101,105,108]))

#M2 price increase using zip method:
def find_price_increase_zip(prices):
    if not prices:
        return 0
    count = 0
    for prev, curr in zip(prices,prices[1:]):
        if curr > prev:
            count += 1
    return f'No of days price got increase : {count}'
print(find_price_increase_zip([100,102,101,105,108]))
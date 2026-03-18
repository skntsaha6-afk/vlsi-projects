#Problem 1 — Price Differences
def price_differences(prices):
    if not prices:
        return []
    differences = []
    for prev, curr in zip(prices, prices[1:]):
            diff = curr - prev
            differences.append(diff)
    return differences

print(price_differences([100,102,101,105]))

#Problem 2 — Price Increase Flag
def price_increase_flag(prices):
    if not prices:
        return []
    
    flag = []
    for prev,curr in zip(prices, prices[1:]):
        diff = curr-prev
        if diff > 0 :
             flag.append(True)
        else:
             flag.append(False)
    return flag
print(price_increase_flag([100,102,101,105]))


#Problem 3 — Largest Price Jump
#m1 : we can do it using sorted : prices[0] and prices[-1]

def largest_price_jump(prices):
    if not prices:
        return 0
    min_prices = sorted(prices)[0]
    max_prices = sorted(prices)[-1]
    return f'min_price : {min_prices} --> max_price: {max_prices}'

print(largest_price_jump([100,102,101,105]))

#Problem 4 — Consecutive Increase Streak
# idea is check the longest window where price is increased continuosly 

def longest_consecutive_increase_streak(prices):
    if not prices:
        return 0
    max_streak = 0
    current_streak = 0
    for prev, curr in zip(prices, prices[1:]):
        if curr > prev:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
    return max_streak
            
print(longest_consecutive_increase_streak([100,102,101,100,106,107,108]))

#Problem 5 — Rolling Sum
#idea is to add a certain window value 
def rolling_sum(prices,window):
    if not prices:
        return []
    window_sum = []
    for i in range(len(prices)):
        if len(prices[i:i+window]) == window : 
            window_sum.append(sum(prices[i:i+window]))
    return window_sum

print(rolling_sum([1,2,3,4,5],3))

#Problem 6 — Parse Slack Values (VLSI)
def parse_slack_values(parse_slack):
    if not parse_slack:
        return []
    
    slack_values = []
    for slack in parse_slack.split(' ')[1:]:
        print(f'Parsing slack value: {slack}')
        try: 
            slack_values.append(float(slack))
        except ValueError:
            print(f'Passed slack value {slack} is not a valid number')
    return slack_values

print(parse_slack_values("slack -0.23"))

#Problem 7 — Extract All Negative Slack
def extract_all_negative_slack(slacks):
    return [slack for slack in slacks if slack < 0]

print(extract_all_negative_slack([-0.12,0.45,-0.30]))

#Problem 8 — Count Slack Violations
def count_violation(slacks):
    neg_slack =[slack for slack in slacks if slack <0 ]
    return len(neg_slack)
print(count_violation([-0.12,0.45,-0.30]))

#Problem 9 — Normalize Prices
def normalize_price(prices):
    return [price/100 for price in prices]
print(normalize_price([100,102,105]))

#Problem 10 — Detect Local Peaks
#A peak occurs if value > neighbors.

def local_peaks(prices):
    return [curr for prev, curr in zip(prices, prices[1:]) if curr > prev]

print(local_peaks([100,105,101,110,108]))
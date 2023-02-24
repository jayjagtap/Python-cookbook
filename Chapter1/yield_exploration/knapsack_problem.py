def find_max_knapsack_profit(capacity, weights, values):
    values_length = len(values)
    if capacity <= 0 or values_length == 0 or len(weights) != values_length:
        return 0
    
    profits = [0] * (capacity + 1)
    knapsack = [[False] * values_length for _ in range(capacity + 1)]

    for i in range(values_length):
        for c in range(capacity, -1, -1):
            if weights[i] <= c:
                new_profit = profits[c - weights[i]] + values[i]
                if new_profit > profits[c]:
                    profits[c] = new_profit
                    knapsack[c][i] = True
        print("Iteration", i+1)
        print("Profits:", profits)
        print("Knapsack:", knapsack)
        print()

    selected_items = []
    total_value = 0
    c = capacity
    for i in range(values_length - 1, -1, -1):
        if knapsack[c][i]:
            selected_items.append(weights[i])
            total_value += values[i]
            c -= weights[i]

    print(f"Selected Items: {selected_items}")
    return (total_value, selected_items)


find_max_knapsack_profit(capacity=6, weights=[3,4,2,1], values=[3,6,7,3])


"""
Iteration 1
Profits: [0, 0, 0, 3, 3, 3, 3]
Knapsack: [[False, False, False, False], [False, False, False, False], [False, False, False, False], [True, False, False, False], [True, False, False, False], [True, False, False, False], [True, False, False, False]]

Iteration 2
Profits: [0, 0, 0, 3, 6, 6, 6]
Knapsack: [
[False, False, False, False], 
[False, False, False, False], 
[False, False, False, False], 
[True, False, False, False], 
[True, True, False, False], 
[True, True, False, False], 
[True, True, False, False]]

Iteration 3
Profits: [0, 0, 7, 7, 7, 10, 13]
Knapsack: [
[False, False, False, False], 
[False, False, False, False], 
[False, False, True, False], 
[True, False, True, False], 
[True, True, True, False], 
[True, True, True, False], 
[True, True, True, False]]

Iteration 4
Profits: [0, 3, 7, 10, 10, 10, 13]
Knapsack: [
[False, False, False, False], 
[False, False, False, True], 
[False, False, True, False], 
[True, False, True, True], 
[True, True, True, True], 
[True, True, True, False], 
[True, True, True, False]]

Selected Items: [2, 4]
"""
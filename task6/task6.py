def greedy_algorithm(items, budget):
    items_with_ratio = [
        (name, value["cost"], value["calories"], value["calories"] / value["cost"])
        for name, value in items.items()
    ]
    
    items_with_ratio.sort(key=lambda x: x[3], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for name, cost, calories, ratio in items_with_ratio:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    n = len(items)
    
    items_list = [(name, value["cost"], value["calories"]) for name, value in items.items()]
    
    for i in range(n):
        name, cost, calories = items_list[i]
        for b in range(budget, cost - 1, -1):
            dp[b] = max(dp[b], dp[b - cost] + calories)
    
    selected_items = []
    b = budget
    for i in range(n - 1, -1, -1):
        name, cost, calories = items_list[i]
        if b >= cost and dp[b] == dp[b - cost] + calories:
            selected_items.append(name)
            b -= cost
    
    return selected_items, dp[budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_items, greedy_calories = greedy_algorithm(items, budget)
print("Greedy Algorithm: Selected items:", greedy_items)
print("Total calories:", greedy_calories)

dp_items, dp_calories = dynamic_programming(items, budget)
print("Dynamic Programming: Selected items:", dp_items)
print("Total calories:", dp_calories)

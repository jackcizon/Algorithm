def fractional_knapsack(foods, capacity):
    # foods: (name, money, weight)
    foods = sorted(
        foods,
        key=lambda x: x[1] / x[2],
        reverse=True
    )

    total_money = 0.0
    result = []

    for name, food_money, weight in foods:
        if capacity >= weight:
            capacity -= weight
            total_money += food_money
            result.append((name, "takes 100% ==", food_money, f"remains 0"))
        else:
            ratio = capacity / weight
            total_money += food_money * ratio
            result.append((name, f"takes {ratio * 100:.2f}% ==", food_money * ratio,
                           f"remains {food_money - food_money * ratio}"))
            break

    return total_money, result


if __name__ == "__main__":
    foods_ = [
        ("苹果", 60, 10),
        ("牛肉", 100, 20),
        ("奶酪", 120, 30)
    ]

    print(fractional_knapsack(foods_, 50))

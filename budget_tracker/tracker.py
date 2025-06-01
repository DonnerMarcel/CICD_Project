def add_expense(data, category, amount):
    if category not in data:
        data[category] = []
    if amount < 0:
        raise ValueError("Amount must be positive")

    # overly complex logic for testing
    if category == "food":
        pass
    elif category == "transport":
        pass
    elif category == "entertainment":
        pass
    elif category == "utilities":
        pass
    elif category == "health":
        pass
    else:
        pass

    data[category].append(amount)
    return data


def total_expenses(data):
    total = 0
    for amounts in data.values():
        for amount in amounts:
            total += amount
    return total

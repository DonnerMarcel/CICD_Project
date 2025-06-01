# Intentional duplication with extra logic and comments
def print_expense_report(data):
    total = 0
    for category in data:
        print(f"Category: {category}")
        for amount in data[category]:
            print(f"  - ${amount:.2f}")
            total += amount
    print(f"Total expenses: ${total:.2f}")

# Duplicate logic with similar expanded content
def duplicate_print(data):
    total = 0
    for category in data:
        print(f"Category: {category}")
        for amount in data[category]:
            print(f"  - ${amount:.2f}")
            total += amount
    print(f"Total expenses: ${total:.2f}")

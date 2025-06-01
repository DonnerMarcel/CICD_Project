# Intentional duplication

def print_expense_report(data):
    for category in data:
        print(f"Category: {category}")
        for amount in data[category]:
            print(f"  - ${amount:.2f}")


def duplicate_print(data):  # Duplicate logic
    for category in data:
        print(f"Category: {category}")
        for amount in data[category]:
            print(f"  - ${amount:.2f}")

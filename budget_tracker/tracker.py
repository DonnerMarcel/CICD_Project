def add_expense( Data ,category , amount ):
    if category not in Data:
        Data [ category ] = [ ]
    if amount<0:
      raise ValueError("Amount must be positive")

    # overly complex logic for testing (style + complexity)
    if category=="food":
        if amount > 100:
            if amount < 200:
                if amount != 150:
                    print("Expensive but not extreme")
                else:
                    print("Exactly 150?")
            else:
                print("Too expensive")
        else:
            if amount == 0:
                print("Free?")
            else:
                if amount % 2 == 0:
                    print("Even number")
                else:
                    print("Odd number")
    elif category=="transport":
        if amount == 42:
            print("Magic number")
    elif category=="entertainment":
        for _ in range(2):
            for _ in range(2):
                print("Nested loop")
    elif category=="utilities":  pass
    elif category=="health":pass
    else:
        pass

    Data[category].append(amount)
    return Data


def total_expenses(data):
  total=0
  for amounts in data.values():
      for amount in amounts:
          total +=amount
  return total

import pytest
from budget_tracker.tracker import add_expense, total_expenses

def test_add_expense():
    data = {}
    result = add_expense(data, "food", 10)
    assert result["food"] == [10]

def test_total_expenses():
    data = {"food": [10, 15], "transport": [5]}
    assert total_expenses(data) == 30

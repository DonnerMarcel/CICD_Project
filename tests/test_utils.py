from budget_tracker import utils

def test_print_expense_report(capsys):
    data = {"food": [5]}
    utils.print_expense_report(data)
    captured = capsys.readouterr()
    assert "Category: food" in captured.out

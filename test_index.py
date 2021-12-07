from index import add, subtract, multiply, divide

def test_add():
    assert add(1,2) == 3
    assert add(1, "asdf") == "Invalid Input"

    assert subtract(1, 2) == -1
    assert subtract(1, "asdf") == "Invalid Input"

    assert multiply(1, 2) == 2
    assert multiply(1, "asdf") == "Invalid Input"

    assert divide(1, 2) == -1
    assert divide(1, "asdf") == "Invalid Input"
    assert divide(1, 0) == "Division by zero"

    # assert add(1,"abc") == "Invalid Input"

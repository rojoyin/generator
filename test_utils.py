def test_is_palindrome():
    number = 121
    assert is_palindrome(number)


def test_not_palindrome():
    number = 123
    assert not is_palindrome(number)


def test_one_digit_number():
    number = 1
    assert not is_palindrome(number)


def test_zero_palindrome():
    number = 0
    assert not is_palindrome(number)

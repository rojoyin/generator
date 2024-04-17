def is_palindrome(num):
    if num < 10:
        return False
    reversed_number = 0
    temp = num
    while temp > 0:
        current_digit = temp % 10
        reversed_number = 10 * reversed_number + current_digit
        temp //= 10
    return num == reversed_number

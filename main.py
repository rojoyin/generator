import math

from utils import is_palindrome


def infinite_palindrome_generator():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)  # anything we pass as argument to the `send` method will be injected here
            if i is not None:
                num = i
        num += 1


palindrome_generator = infinite_palindrome_generator()
for i in palindrome_generator:
    print(i)
    digits = math.floor(math.log10(i)+1)
    palindrome_generator.send(10**digits)

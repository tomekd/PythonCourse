
def get_fibonacci_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n < 1:
        return 0
    else:
        return get_fibonacci_number(n-1) + get_fibonacci_number(n-2)

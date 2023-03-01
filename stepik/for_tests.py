def get_even(*args):
    return [a for a in args if a % 2 == 0]

print(get_even(45, 4, 8, 11, 12, 0))
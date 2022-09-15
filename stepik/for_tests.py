def check_password(a, chars="$%!?@#"):
    for i in a:
        if len(a)>= 8 and i in chars:
            return True
    return False

#numbers = list(map(int, input().split()))
print(check_password("12345678!"))
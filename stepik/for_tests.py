def check_password(a, teg = "h1"):
    lst = f"<{teg}>{a}</{teg}>"
    return lst
#numbers = list(map(int, input().split()))
str = input()
print(check_password(str))
print(check_password(str, "div"))
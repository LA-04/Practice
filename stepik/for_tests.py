def check_password(a, teg = "div", up = True):
    if up:
        teg = teg.upper()
    return f"<{teg}>{a}</{teg}>"
#numbers = list(map(int, input().split()))
str = input()
print(check_password(str))
print(check_password(str, up=False))
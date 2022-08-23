def email(x):
    if 'a' <= x.lower() <= 'z' or '0' <= x <= '9' or x  in '_@.':
        print("ДА")
    else:
        print("НЕТ")


email(input())
def long_word(word):
    if len(word) > 10:
        return f"{word[0]}{len(word)-2}{word[-1]}"
    else:
        return word

n = int(input())
for i in range(n):
    print(long_word(input()))

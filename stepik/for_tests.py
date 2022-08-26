def how_long(words):
    short_words = []
    for word in words:
        if len(word) >= 6:
            short_words.append(word)
    return short_words


print(*how_long(input().split()))
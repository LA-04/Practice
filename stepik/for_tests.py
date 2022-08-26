def min_max(min, max):
    return min*max


numbers = list(map(int, input().split()))
print(min_max(min(numbers), max(numbers)))
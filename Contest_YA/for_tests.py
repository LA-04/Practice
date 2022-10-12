def next_level(min_point, people):
    k = 0
    max_point = people[min_point[1]-1]
    for i in range(len(people)):
        if people[i] >= max_point and people[i] > 0:
            k += 1
    return k

# min_point = list(map(int, input().split()))
# people = list(map(int, input().split()))

#print(next_level(min_point,people))
print(next_level([8,5],[10,9,8,7,7,6,5,5]))
print(next_level([4,2],[0,0,0,0]))



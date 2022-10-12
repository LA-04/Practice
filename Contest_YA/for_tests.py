def team(task, who_know):
    n = 0
    for i in range(task):
        if sum(who_know[i]) >= 2:
            n += 1
    return n


task = int(input())
who_know = []
for i in range(task):
    who_know.append(list(map(int, input().split())))

print(team(task, who_know))
print(team(2,[[1,0,0],[0,1,1]]))

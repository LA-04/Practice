def ring_line(stations):
    if 1 <= stations[0] <= 100 and stations[1] != stations[2]:
        if stations[1] < stations[2]:
            if stations[1] - 1 + stations[0] - stations[2] <= stations[2] - stations[1]:
                return stations[1] - 1 + stations[0] - stations[2]
            else:
                return stations[2] - stations[1] - 1
        else:
            if stations[2] - 1 + stations[0] - stations[1] <= stations[1] - stations[2]:
                return stations[2] - 1 + stations[0] - stations[1]
            else:
                return stations[1] - stations[2] - 1


stations = list(map(int, input().split()))

print(ring_line(stations))
# print(ring_line([100, 5, 6])) #0
# print(ring_line([10, 1, 9])) #1
# print(ring_line([20, 5, 15])) #9
# print(ring_line([10, 1, 10])) #0
# print(ring_line([10, 7, 5])) #1
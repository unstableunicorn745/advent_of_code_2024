data = [int(i) for i in open('./day1data.txt', "r+").read().split()]


distance_1 = data[::2]
distance_2 = data[1::2]

distance_1_sorted = sorted(distance_1)
distance_2_sorted = sorted(distance_2)

total_distance = 0

for i in range(len(distance_1_sorted)):
    x = distance_1_sorted[i]
    y = distance_2_sorted[i]
    total_distance += abs(x - y)

print(total_distance)

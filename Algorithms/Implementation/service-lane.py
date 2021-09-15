

def service_lane(width, start, end):
    total_vehicles = 3
    for i in range(len(width)):
        if i >= start and i <= end and width[i] < total_vehicles:
            total_vehicles = width[i]
    return total_vehicles

n,t = list(map(int, input().strip().split(' ')))
width = list(map(int, input().strip().split(' ')))
for a0 in range(t):
    i, j = [int(item) for item in input().strip().split(' ')]
    print(service_lane(width, i, j))

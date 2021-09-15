

import sys

# Get data
arr = list(map(int, input().strip().split(' ')))
n = len(arr)
values = []

# Get the minimum and maximum values
for i in range(n):
    val = 0
    for j in range(n):
        if i != j:
            val += arr[j]
    values.append(val)

# Show the results
print (str(min(values)) + " " + str(max(values))) 
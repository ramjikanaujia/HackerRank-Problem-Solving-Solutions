
n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))

for i in range(1, n + 1):
    print (arr.index(arr.index(i) + 1) + 1)

v = int(input().strip())
n = int(input().strip())
arr = [int(ar) for ar in input().strip().split(' ')]

for i in range(n):
    if arr[i] == v:
        print (i)
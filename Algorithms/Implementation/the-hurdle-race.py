

n,k = list(map(int, input().strip().split(' ')))
height = list(map(int, input().strip().split(' ')))
if max(height) > k:
    print (max(height) - k)
else:
    print (0)

n, d = list(map(int, input().split()))
arr = list(map(int, input().rstrip().split()))
print (str(sum([1 for item in arr if item + d in arr and item + d * 2 in arr])) + '\n')
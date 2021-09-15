

def solve(n, s, d, m):
    total = 0
    for i in range((n - m) + 1):
        if sum(s[i:i+m]) == d:
            total += 1
    return total

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = list(map(int, input().strip().split(' ')))
print(solve(n, s, d, m))

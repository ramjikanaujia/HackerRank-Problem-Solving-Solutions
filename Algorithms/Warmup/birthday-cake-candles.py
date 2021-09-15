
def birthdayCakeCandles(n, ar):
    max_number = max(ar)
    candles = []
    for i in range(n):
        if max_number == ar[i]:
            candles.append(ar[i])

    return len(candles)

# Get initial values
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
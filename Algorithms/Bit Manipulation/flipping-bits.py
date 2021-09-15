# Time complexity: O(1)
def flippingBits(N):
    return N^4294967295

# Start algorithm
n = int(input().strip())
for a0 in range(n):
    print(flippingBits(int(input().strip())))

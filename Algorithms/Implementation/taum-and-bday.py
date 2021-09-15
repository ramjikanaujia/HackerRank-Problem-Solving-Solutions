
t = int(input().strip())
for a in range(t):
    b,w = map(int, input().strip().split(' '))
    x,y,z = map(int, input().strip().split(' '))
    min_x = min(x, y + z)
    min_y = min(y, x + z)
    print(min_x * b + min_y * w)
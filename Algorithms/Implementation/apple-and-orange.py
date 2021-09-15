

s,t = [int(points) for points in input().strip().split(' ')]
a,b = [int(points) for points in input().strip().split(' ')]
m,n = [int(points) for points in input().strip().split(' ')]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apples_home = []
oranges_home = []
for i in range(m):
    pos_apple = a + apple[i]
    if pos_apple >= s and pos_apple <= t:
        apples_home.append(apple[i])

for i in range(n):
    pos_orange = b + orange[i]
    if pos_orange >= s and pos_orange <= t:
        oranges_home.append(orange[i])
    
print (len(apples_home))
print (len(oranges_home))
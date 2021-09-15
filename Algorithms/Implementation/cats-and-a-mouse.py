
import math

def catch_mouse(x, y, z):
    # Euclidean distance 
    cat_1 = math.sqrt((x - z) ** 2)
    cat_2 = math.sqrt((y - z) ** 2)
    if cat_1 < cat_2:
        return "Cat A"
    elif cat_2 < cat_1:
        return "Cat B"
    else:    
        return "Mouse C"

q = int(input().strip())
for a0 in range(q):
    x, y, z =  [int(points) for points in input().strip().split(' ')]
    print (catch_mouse(x, y, z))